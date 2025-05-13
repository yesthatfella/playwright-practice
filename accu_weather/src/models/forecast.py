from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ForecastTemperature:
    Value: float
    Unit: str
    UnitType: int

@dataclass
class Temperature:
    Minimum: ForecastTemperature
    Maximum: ForecastTemperature

@dataclass
class Day:
    Icon: int
    IconPhrase: str
    HasPrecipitation: bool
    PrecipitationType: Optional[str]
    PrecipitationIntensity: Optional[str]

@dataclass
class Night:
    Icon: int
    IconPhrase: str
    HasPrecipitation: bool
    PrecipitationType: Optional[str]
    PrecipitationIntensity: Optional[str]

@dataclass
class DailyForecast:
    Date: str
    EpochDate: int
    Temperature: Temperature
    Day: Day
    Night: Night
    Sources: List[str]
    MobileLink: str
    Link: str

@dataclass
class Headline:
    EffectiveDate: str
    EffectiveEpochDate: int
    Severity: int
    Text: str
    Category: str
    EndDate: str
    EndEpochDate: int
    MobileLink: str
    Link: str

@dataclass
class WeatherForecast:
    Headline: Headline
    DailyForecasts: List[DailyForecast]