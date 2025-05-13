import pytest
from ...src.weather_api import WeatherMetrics
from ...src.models.forecast import (
    DailyForecast, Day, ForecastTemperature, Night, Temperature
)

class TestWeatherMetrics:

    daily_forcast_sample = [
        DailyForecast(
            Date="2025-05-09T07:00:00-06:00",
            EpochDate=1746795600,
            Temperature=Temperature(
                Minimum=ForecastTemperature(Value=60, Unit='F', UnitType=18),
                Maximum=ForecastTemperature(Value=85, Unit='F', UnitType=18)
            ),
            Day=Day(
                Icon=16,
                IconPhrase="Partly cloudy",
                HasPrecipitation=True,
                PrecipitationType="Rain",
                PrecipitationIntensity="Light"
            ),
            Night=Night(
                Icon=15,
                IconPhrase="Clear",
                HasPrecipitation=False,
                PrecipitationType=None,
                PrecipitationIntensity=None
            ),
            Sources=["AccuWeather"],
            MobileLink="http://sample.com/mobile1",
            Link="http://sample.com/link1"
        ),
        DailyForecast(
            Date="2025-05-10T07:00:00-06:00",
            EpochDate=1746882000,
            Temperature=Temperature(
                Minimum=ForecastTemperature(Value=58, Unit='F', UnitType=18),
                Maximum=ForecastTemperature(Value=88, Unit='F', UnitType=18)
            ),
            Day=Day(
                Icon=12,
                IconPhrase="Mostly sunny",
                HasPrecipitation=False,
                PrecipitationType=None,
                PrecipitationIntensity=None
            ),
            Night=Night(
                Icon=14,
                IconPhrase="Partly cloudy",
                HasPrecipitation=False,
                PrecipitationType=None,
                PrecipitationIntensity=None
            ),
            Sources=["AccuWeather"],
            MobileLink="http://sample.com/mobile2",
            Link="http://sample.com/link2"
        ),
        DailyForecast(
            Date="2025-05-11T07:00:00-06:00",
            EpochDate=1746968400,
            Temperature=Temperature(
                Minimum=ForecastTemperature(Value=55, Unit='F', UnitType=18),
                Maximum=ForecastTemperature(Value=90, Unit='F', UnitType=18)
            ),
            Day=Day(
                Icon=20,
                IconPhrase="Thunderstorms",
                HasPrecipitation=True,
                PrecipitationType="Rain",
                PrecipitationIntensity="Moderate"
            ),
            Night=Night(
                Icon=22,
                IconPhrase="Cloudy",
                HasPrecipitation=True,
                PrecipitationType="Rain",
                PrecipitationIntensity="Heavy"
            ),
            Sources=["AccuWeather"],
            MobileLink="http://sample.com/mobile3",
            Link="http://sample.com/link3"
        ),
        DailyForecast(
            Date="2025-05-12T07:00:00-06:00",
            EpochDate=1747054800,
            Temperature=Temperature(
                Minimum=ForecastTemperature(Value=53, Unit='F', UnitType=18),
                Maximum=ForecastTemperature(Value=85, Unit='F', UnitType=18)
            ),
            Day=Day(
                Icon=10,
                IconPhrase="Sunny",
                HasPrecipitation=False,
                PrecipitationType=None,
                PrecipitationIntensity=None
            ),
            Night=Night(
                Icon=10,
                IconPhrase="Clear",
                HasPrecipitation=False,
                PrecipitationType=None,
                PrecipitationIntensity=None
            ),
            Sources=["AccuWeather"],
            MobileLink="http://sample.com/mobile4",
            Link="http://sample.com/link4"
        ),
        DailyForecast(
            Date="2025-05-13T07:00:00-06:00",
            EpochDate=1747141200,
            Temperature=Temperature(
                Minimum=ForecastTemperature(Value=50, Unit='F', UnitType=18),
                Maximum=ForecastTemperature(Value=82, Unit='F', UnitType=18)
            ),
            Day=Day(
                Icon=5,
                IconPhrase="Drizzle",
                HasPrecipitation=True,
                PrecipitationType="Rain",
                PrecipitationIntensity="Light"
            ),
            Night=Night(
                Icon=5,
                IconPhrase="Light rain",
                HasPrecipitation=True,
                PrecipitationType="Rain",
                PrecipitationIntensity="Light"
            ),
            Sources=["AccuWeather"],
            MobileLink="http://sample.com/mobile5",
            Link="http://sample.com/link5"
        )
    ]

    def test_forecast_average(self):
        weather_metrics = WeatherMetrics(self.daily_forcast_sample)
        assert weather_metrics.get_avg_for_period() == 70.6

    def test_forecast_max_temp(self):
        weather_metrics = WeatherMetrics(self.daily_forcast_sample)
        assert weather_metrics.get_max_for_period() == 90

    def test_forecast_min_temp(self):
        weather_metrics = WeatherMetrics(self.daily_forcast_sample)
        assert weather_metrics.get_min_for_period() == 50
