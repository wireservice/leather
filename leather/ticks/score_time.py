#!/usr/bin/env python

from datetime import date, datetime, timedelta
from decimal import Decimal
from functools import partial
import math
import sys

from leather.ticks.score import ScoreTicker
from leather import utils


#: The default number of ticks to produce
DEFAULT_TICKS = 5

#: The minimum length of a viable tick sequence
MIN_TICK_COUNT = 4

#: The maximum length of a viable tick sequence
MAX_TICK_COUNT = 10


class ScoreTimeTicker(ScoreTicker):
    """
    A variation on :class:`.ScoreTicker` that generates sequences of dates
    or datetimes.

    :param domain_min:
        Minimum value of the data series.
    :param domain_max:
        Maximum value of the data series.
    """
    def __init__(self, domain_min, domain_max):
        self._domain_min = domain_min
        self._domain_max = domain_max

        if isinstance(self._domain_min, datetime):
            self._type = datetime
        else:
            self._type = date

        # Years
        if self._domain_max.year - self._domain_min.year >= 4:
            self._to_unit = utils.to_year_count
            self._from_unit = partial(utils.from_year_count, t=self._type)
            self._fmt = '%Y'
        # Months
        elif utils.to_month_count(self._domain_max) - utils.to_month_count(self._domain_min) >= 4:
            self._to_unit = utils.to_month_count
            self._from_unit = partial(utils.from_month_count, t=self._type)

            if utils.to_year_count(self._domain_max) - utils.to_year_count(self._domain_min) >= 1:
                self._fmt = '%Y-%m'
            else:
                self._fmt = '%m'
        # Days
        elif utils.to_day_count(self._domain_max) - utils.to_day_count(self._domain_min) >= 4:
            self._to_unit = utils.to_day_count
            self._from_unit = partial(utils.from_day_count, t=self._type)

            if utils.to_month_count(self._domain_max) - utils.to_month_count(self._domain_min) >= 1:
                self._fmt = '%m-%d'
            else:
                self._fmt = '%d'
        # Hours
        elif utils.to_hour_count(self._domain_max) - utils.to_hour_count(self._domain_min) >= 4:
            self._to_unit = utils.to_hour_count
            self._from_unit = utils.from_hour_count

            if utils.to_day_count(self._domain_max) - utils.to_day_count(self._domain_min) >= 1:
                self._fmt = '%d-%H'
            else:
                self._fmt = '%H'
        # Minutes
        elif utils.to_minute_count(self._domain_max) - utils.to_minute_count(self._domain_min) >= 4:
            self._to_unit = utils.to_minute_count
            self._from_unit = utils.from_minute_count

            if utils.to_hour_count(self._domain_max) - utils.to_hour_count(self._domain_min) >= 1:
                self._fmt = '%H:%M'
            else:
                self._fmt = '%M'
        # Seconds
        elif utils.to_second_count(self._domain_max) - utils.to_second_count(self._domain_min) >= 4:
            self._to_unit = utils.to_second_count
            self._from_unit = utils.from_second_count

            if utils.to_minute_count(self._domain_max) - utils.to_minute_count(self._domain_min) >= 1:
                self._fmt = '%H:%M:%S'
            else:
                self._fmt = '%S'
        # Microseconds
        else:
            self._to_unit = utils.to_microsecond_count
            self._from_unit = utils.from_microsecond_count

            if utils.to_second_count(self._domain_max) - utils.to_second_count(self._domain_min) >= 1:
                self._fmt = '%S-%f'
            else:
                self._fmt = '%f'

        # Compute unit min and max
        self._unit_min = self._to_unit(self._domain_min)
        self._unit_max = self._to_unit(self._domain_max)

        if (self._domain_max - self._from_unit(self._unit_max)).total_seconds() > 0:
            self._unit_max += 1

        self._ticks = self._find_ticks()

        self._min = self._ticks[0]
        self._max = self._ticks[-1]

    def _find_ticks(self):
        """
        Implements the tick-finding algorithm.
        """
        delta = self._unit_max - self._unit_min

        interval_guess = int(math.ceil(delta / (DEFAULT_TICKS - 1)))

        candidate_intervals = []

        candidate_intervals.append(interval_guess)
        candidate_intervals.append(interval_guess - 1)
        candidate_intervals.append(interval_guess + 1)

        if 0 in candidate_intervals:
            candidate_intervals.remove(0)

        candidate_ticks = []

        for interval in candidate_intervals:
            ticks = []
            ticks.append(int(math.floor((self._unit_min / interval))) * interval)

            tick_num = 1

            while ticks[tick_num - 1] < self._unit_max:
                t = ticks[0] + (interval * tick_num)

                ticks.append(t)
                tick_num += 1

            # Throw out sequences that are too short or too long
            if len(ticks) < MIN_TICK_COUNT or len(ticks) > MAX_TICK_COUNT:
                continue

            candidate_ticks.append({
                'interval': interval,
                'ticks': ticks,
                'score': self._score(interval, ticks)
            })

        # Order by best score, using number of ticks as a tie-breaker
        best = sorted(candidate_ticks, key=lambda c: (c['score']['total'], len(c['ticks'])))
        ticks = best[0]['ticks']

        return [self._from_unit(t) for t in ticks]

    def _score(self, interval, ticks):
        """
        Score a given tick sequence based on several criteria. This method returns
        discrete scoring components for easier debugging.
        """
        s = {
            'pct_waste': 0,
            'interval_penalty': 0,
            'len_penalty': 0,
            'total': 0
        }

        # Penalty for wasted scale space
        waste = (self._unit_min - ticks[0]) + (ticks[-1] - self._unit_max)
        pct_waste = waste / (self._unit_max - self._unit_min)

        s['pct_waste'] = pow(10, pct_waste)

        # Penalty for too many ticks
        if len(ticks) > 5:
            s['len_penalty'] = (len(ticks) - 5)

        s['total'] = s['pct_waste'] + s['interval_penalty'] + s['len_penalty']

        return s

    def format_tick(self, tick):
        """
        Format a tick using the inferred time formatting.
        """
        return tick.strftime(self._fmt)
