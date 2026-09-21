from datetime import date as date
from datetime import datetime as datetime
from decimal import Decimal as Decimal
from typing import ClassVar as _ClassVar
from typing import overload as _overload


class DataType:
    """
    Base class for :class:`.Series` data types.
    """
    @classmethod
    @_overload
    def infer(cls, v: datetime) -> type["DateTime"]:
        ...

    @classmethod
    @_overload
    def infer(cls, v: date) -> type["Date"] | type["DateTime"]:
        ...

    @classmethod
    @_overload
    def infer(cls, v: int | float | Decimal) -> type["Number"]:
        ...

    @classmethod
    @_overload
    def infer(cls, v: str) -> type["Text"]:
        ...

    @classmethod
    def infer(
        cls, v: date | int | float | Decimal | str
    ) -> type["Date"] | type["DateTime"] | type["Number"] | type["Text"]:
        if isinstance(v, DateTime.types):
            return DateTime
        if isinstance(v, Date.types):
            return Date
        if isinstance(v, Number.types):
            return Number
        if isinstance(v, Text.types):
            return Text

        raise TypeError('No data type available for %s' % type(v))


class Date(DataType):
    """
    Data representing dates.
    """
    types: _ClassVar[tuple[type[date]]] = (date,)


class DateTime(DataType):
    """
    Data representing dates with times.
    """
    types: _ClassVar[tuple[type[datetime]]] = (datetime,)


class Number(DataType):
    """
    Data representing numbers.
    """
    types: _ClassVar[tuple[type[int], type[float], type[Decimal]]] = (int, float, Decimal)


class Text(DataType):
    """
    Data representing text/strings.
    """
    types: _ClassVar[tuple[type[str]]] = (str,)
