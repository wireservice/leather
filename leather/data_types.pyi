from datetime import date as date
from datetime import datetime as datetime
from decimal import Decimal as _Decimal
from typing import ClassVar as _ClassVar
from typing import overload as _overload

Decimal: type[_Decimal]

class DataType:
    @classmethod
    @_overload
    def infer(cls, v: datetime) -> type[DateTime]: ...
    @classmethod
    @_overload
    def infer(cls, v: date) -> type[Date] | type[DateTime]: ...
    @classmethod
    @_overload
    def infer(cls, v: int | float | _Decimal) -> type[Number]: ...
    @classmethod
    @_overload
    def infer(cls, v: str) -> type[Text]: ...

class Date(DataType):
    types: _ClassVar[tuple[type[date]]]

class DateTime(DataType):
    types: _ClassVar[tuple[type[datetime]]]

class Number(DataType):
    types: _ClassVar[tuple[type[int], type[float], type[_Decimal]]]

class Text(DataType):
    types: _ClassVar[tuple[type[str]]]
