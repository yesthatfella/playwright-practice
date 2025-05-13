from enum import Enum
import logging
from tkinter.filedialog import dialogstates

import requests
from typing import Optional, Any

from accu_weather.src.models.forecast import WeatherForecast, DailyForecast
from accu_weather.src.models.location import City
from accu_weather.src.utils.data_ingestor import dict_to_dataclass

class ForecastDays(Enum):
    ONE     = 1
    FIVE    = 5
    TEN     = 10
    FIFTEEN = 15


class AccuWeather:

    API_KEY = "boMCi0xeJ7AGAxeXQkzEi6Gra2AtdV8h"
    BASE_URL = "http://dataservice.accuweather.com"
    logger = logging.getLogger('accuDebug')

    def get_city(self, search_entry) -> Optional[City]:
        url = f'{self.BASE_URL}/locations/v1/cities/search'
        # query params
        url += f'?apikey={self.API_KEY}&q={search_entry}'

        try:
            response = requests.get(url)

            if response.status_code == 200:
                res = response.json()
                if isinstance(res, list) and len(res) > 0:
                    # Returns first City in results
                    return dict_to_dataclass(res[0], City)
                self.logger.error(f'Error: Unexpected response type')
                return None
            else:
                self.logger.error(f'Error: {response.status_code}')
                return None
        except Exception:
            self.logger.error("An error has occurred when invoking Get City from AccuWeather")


    def get_n_day_forecast(self, location_id: str, days: ForecastDays) -> Optional[Any]:
        url = (f'http://dataservice.accuweather.com/forecasts/v1/daily/{days.value}day/{location_id}'
               f'?apikey={self.API_KEY}')

        try:
            response = requests.get(url)

            if response.status_code == 200:
                res = response.json()
                if isinstance(res, dict):
                    return dict_to_dataclass(res, WeatherForecast)
            elif response.status_code == 401:
                self.logger.error(f'Error: {response.status_code}')
                return response.json()
            else:
                return None
        except Exception:
            self.logger.error("An error has occurred when invoking Get One Day Forecast from  AccuWeather."
                              f"\nOccurred for Location {location_id}")


class WeatherMetrics:

    def __init__(self, daily_forecast: list[DailyForecast]):
        self.daily_forecast = daily_forecast

    def get_min_for_period(self) -> float:
        if not self.daily_forecast:
            return 0.0

        return min(i.Temperature.Minimum.Value for i in self.daily_forecast)

    def get_max_for_period(self) -> float:
        if not self.daily_forecast:
            return 0.0

        return max(i.Temperature.Maximum.Value for i in self.daily_forecast)

    def get_avg_for_period(self) -> float:
        if not self.daily_forecast:
            return 0.0

        total = sum(
            (i.Temperature.Minimum.Value + i.Temperature.Maximum.Value) / 2 for i in self.daily_forecast
        )

        return total / len(self.daily_forecast)

