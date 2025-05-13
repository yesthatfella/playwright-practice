from dataclasses import dataclass
from typing import Optional

@dataclass
class Region:
    ID: str
    LocalizedName: str
    EnglishName: str

@dataclass
class Country:
    ID: str
    LocalizedName: str
    EnglishName: str

@dataclass
class AdministrativeArea:
    ID: str
    LocalizedName: str
    EnglishName: str
    Level: int
    LocalizedType: str
    EnglishType: str
    CountryID: str

@dataclass
class TimeZone:
    Code: str
    Name: str
    GmtOffset: float
    IsDaylightSaving: bool
    NextOffsetChange: Optional[str]

@dataclass
class ElevationMetric:
    Value: float
    Unit: str
    UnitType: int

@dataclass
class ElevationImperial:
    Value: float
    Unit: str
    UnitType: int

@dataclass
class Elevation:
    Metric: ElevationMetric
    Imperial: ElevationImperial

@dataclass
class GeoPosition:
    Latitude: float
    Longitude: float
    Elevation: Elevation

@dataclass
class City:
    Version: int
    Key: str
    Type: str
    Rank: int
    LocalizedName: str
    EnglishName: str
    PrimaryPostalCode: str
    Region: Region
    Country: Country
    AdministrativeArea: AdministrativeArea
    TimeZone: TimeZone
    GeoPosition: GeoPosition
