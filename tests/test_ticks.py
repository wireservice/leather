from datetime import date, datetime
from decimal import Decimal

import leather
from leather import utils
from leather.ticks.score_time import ScoreTicker, ScoreTimeTicker


class TestScoreTicker(leather.LeatherTestCase):
    def test_years(self):
        ticker = ScoreTicker(Decimal(0), Decimal(10))

        self.assertIsInstance(ticker.ticks[0], Decimal)


class TestScoreTimeTicker(leather.LeatherTestCase):
    def test_years(self):
        ticker = ScoreTimeTicker(
            date(2010, 1, 1),
            date(2015, 1, 1)
        )

        self.assertIsInstance(ticker.ticks[0], date)
        self.assertIs(ticker._to_unit, utils.to_year_count)

    def test_years_datetime(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 1, 1),
            datetime(2015, 1, 1)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_year_count)

    def test_months(self):
        ticker = ScoreTimeTicker(
            date(2011, 3, 1),
            date(2011, 7, 1)
        )

        self.assertIsInstance(ticker.ticks[0], date)
        self.assertIs(ticker._to_unit, utils.to_month_count)

    def test_months_datetime(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 1),
            datetime(2011, 7, 1)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_month_count)

    def test_months_for_years(self):
        ticker = ScoreTimeTicker(
            date(2011, 1, 1),
            date(2013, 1, 1)
        )

        self.assertIsInstance(ticker.ticks[0], date)
        self.assertIs(ticker._to_unit, utils.to_month_count)

    def test_days(self):
        ticker = ScoreTimeTicker(
            date(2011, 3, 5),
            date(2011, 3, 10)
        )

        self.assertIsInstance(ticker.ticks[0], date)
        self.assertIs(ticker._to_unit, utils.to_day_count)

    def test_days_datetime(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5),
            datetime(2011, 3, 10)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_day_count)

    def test_days_for_months(self):
        ticker = ScoreTimeTicker(
            date(2011, 3, 1),
            date(2011, 5, 1)
        )

        self.assertIsInstance(ticker.ticks[0], date)
        self.assertIs(ticker._to_unit, utils.to_day_count)

    def test_hours(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5, 2),
            datetime(2011, 3, 5, 10)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_hour_count)

    def test_hours_for_days(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5),
            datetime(2011, 3, 6)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_hour_count)

    def test_minutes(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5, 2, 15),
            datetime(2011, 3, 5, 2, 45)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_minute_count)

    def test_minutes_for_hours(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5, 2),
            datetime(2011, 3, 5, 3)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_minute_count)

    def test_seconds(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5, 2, 15, 15),
            datetime(2011, 3, 5, 2, 15, 45)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_second_count)

    def test_seconds_for_minutes(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5, 2, 15),
            datetime(2011, 3, 5, 2, 18)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_second_count)

    def test_microseconds(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5, 2, 15, 15, 1000),
            datetime(2011, 3, 5, 2, 15, 15, 5000)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_microsecond_count)

    def test_microseconds_for_seconds(self):
        ticker = ScoreTimeTicker(
            datetime(2011, 3, 5, 2, 15, 15),
            datetime(2011, 3, 5, 2, 15, 17)
        )

        self.assertIsInstance(ticker.ticks[0], datetime)
        self.assertIs(ticker._to_unit, utils.to_microsecond_count)
