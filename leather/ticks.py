#!/usr/bin/env python

from decimal import Decimal
import math
import sys

from leather.utils import isclose

# Shorthand
ZERO = Decimal('0')
TEN = Decimal('10')

#: Normalized intervals to be tested for ticks
INTERVALS = [
    Decimal('0.1'),
    Decimal('0.15'),
    Decimal('0.2'),
    Decimal('0.25'),
    Decimal('0.5')
]

#: The default number of ticks to produce
DEFAULT_TICKS = 5

#: The minimum length of a viable tick sequence
MIN_TICK_COUNT = 4

#: The maximum length of a viable tick sequence
MAX_TICK_COUNT = 10

#: Most preferred tick intervals
BEST_INTERVALS = [Decimal('0.1')]

#: Least preferred tick intervals
WORST_INTERVALS = [Decimal('0.15')]


def optimize_ticks(domain_min, domain_max):
    """
    Attempt to find an optimal series of ticks by generating many possible
    sequences and scoring them based on several criteria. Only the best
    tick sequence is returned.

    Based an algorithm described by Austin Clemsens:
    http://austinclemens.com/blog/2016/01/09/an-algorithm-for-creating-a-graphs-axes/

    See :func:`.score` for scoring implementation.

    :param domain_min:
        Minimum value of the data series.
    :param domain_max:
        Maximum value of the data series.
    """
    force_zero = domain_min <= ZERO and domain_max >= ZERO

    interval_guess = abs(domain_max - domain_min) / (DEFAULT_TICKS - 1)
    magnitude = math.ceil(math.log10(interval_guess))

    candidate_intervals = []

    for interval in INTERVALS:
        candidate_intervals.append((interval, interval * pow(TEN, magnitude)))
        candidate_intervals.append((interval, interval * pow(TEN, magnitude - 1)))
        candidate_intervals.append((interval, interval * pow(TEN, magnitude + 1)))

    candidate_ticks = []

    for base_interval, interval in candidate_intervals:
        ticks = []

        if force_zero:
            min_steps = math.ceil(abs(domain_min) / interval)
            ticks.append(round_tick(-min_steps * interval))
        else:
            ticks.append(round_tick(math.floor(domain_min / interval) * interval))

        tick_num = 1

        while ticks[tick_num - 1] < domain_max:
            t = round_tick(ticks[0] + (interval * tick_num))

            ticks.append(t)
            tick_num += 1

        # Throw out sequences that are too short or too long
        if len(ticks) < MIN_TICK_COUNT or len(ticks) > MAX_TICK_COUNT:
            continue

        candidate_ticks.append({
            'base_interval': base_interval,
            'interval': interval,
            'ticks': ticks,
            'score': score(domain_min, domain_max, base_interval, interval, ticks)
        })

    # Order by best score, using number of ticks as a tie-breaker
    best = sorted(candidate_ticks, key=lambda c: (c['score']['total'], len(c['ticks'])))

    return best[0]['ticks']


def score(domain_min, domain_max, base_interval, interval, ticks):
    """
    Score a given tick sequence based on several criteria. This method returns
    discrete scoring components for easier debugging.

    See :func:`.optimize_ticks`.
    """
    s = {
        'pct_waste': 0,
        'interval_penalty': 0,
        'len_penalty': 0,
        'total': 0
    }

    # Penalty for wasted scale space
    waste = (domain_min - ticks[0]) + (ticks[-1] - domain_max)
    pct_waste = waste / (domain_max - domain_min)

    s['pct_waste'] = pow(10, pct_waste)

    # Penalty for choosing less optimal tick intervals
    if base_interval in BEST_INTERVALS:
        pass
    elif base_interval in WORST_INTERVALS:
        s['interval_penalty'] = 2
    else:
        s['interval_penalty'] = 1

    # Penalty for too many ticks
    if len(ticks) > 5:
        s['len_penalty'] = (len(ticks) - 5)

    s['total'] = s['pct_waste'] + s['interval_penalty'] + s['len_penalty']

    return s


def round_tick(t):
    """
    Round ticks to 0-3 decimal places, if the remaining digits do not appear
    to be significant.
    """
    for r in range(0, 4):
        exp = pow(Decimal(10), Decimal(-r))
        quantized = t.quantize(exp)

        if isclose(t, quantized):
            return quantized

    return t
