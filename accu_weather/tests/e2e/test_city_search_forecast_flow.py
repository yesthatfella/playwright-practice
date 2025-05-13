import pytest

from accu_weather.src.weather_api import (
    AccuWeather, ForecastDays, WeatherMetrics
)


@pytest.mark.parametrize(
    "query, city_name, country_name", [
        ("Comitan", "Comitán de Domínguez", "Mexico"),
        ("Guadalajara", "Guadalajara", "Mexico")
    ]
)
def test_city_search_and_5_days_forecast(query, city_name, country_name):
    weather_api = AccuWeather()

    city = weather_api.get_city(query)
    assert city.EnglishName == city_name
    assert city.Country.EnglishName == country_name

    forecast = weather_api.get_n_day_forecast(city.Key, ForecastDays.FIVE)

    assert len(forecast.DailyForecasts) == 5

    metrics = WeatherMetrics(forecast.DailyForecasts)
    assert 50 < metrics.get_avg_for_period() < 100
    assert 40 < metrics.get_max_for_period() < 100
    assert 30 < metrics.get_min_for_period() < 70



