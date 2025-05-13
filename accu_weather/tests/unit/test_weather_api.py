import pytest
from unittest.mock import patch, Mock

from accu_weather.src.models.forecast import WeatherForecast
from accu_weather.src.weather_api import AccuWeather, ForecastDays

from accu_weather.src.models.location import City

class TestAccuWeather:

    forecast_sample_res = {
        "one_day": {
            "Headline": {
                "EffectiveDate": "2025-05-09T19:00:00-06:00",
                "EffectiveEpochDate": 1746838800,
                "Severity": 5,
                "Text": "A thunderstorm this evening",
                "Category": "thunderstorm",
                "EndDate": "2025-05-10T01:00:00-06:00",
                "EndEpochDate": 1746860400,
                "MobileLink": "http://...",
                "Link": "http://..."
            },
            "DailyForecasts": [
                {
                    "Date": "2025-05-09T07:00:00-06:00",
                    "EpochDate": 1746795600,
                    "Temperature": {
                        "Minimum": {"Value": 61, "Unit": "F", "UnitType": 18},
                        "Maximum": {"Value": 86, "Unit": "F", "UnitType": 18}
                    },
                    "Day": {
                        "Icon": 16,
                        "IconPhrase": "Mostly cloudy w/ t-storms",
                        "HasPrecipitation": True,
                        "PrecipitationType": "Rain",
                        "PrecipitationIntensity": "Light"
                    },
                    "Night": {
                        "Icon": 15,
                        "IconPhrase": "Thunderstorms",
                        "HasPrecipitation": True,
                        "PrecipitationType": "Rain",
                        "PrecipitationIntensity": "Moderate"
                    },
                    "Sources": ["AccuWeather"],
                    "MobileLink": "http://...",
                    "Link": "http://..."
                }
            ]
        },
        "five_days": {
            "Headline": {
                "EffectiveDate": "2025-05-09T19:00:00-06:00",
                "EffectiveEpochDate": 1746838800,
                "Severity": 5,
                "Text": "A thunderstorm this evening",
                "Category": "thunderstorm",
                "EndDate": "2025-05-10T01:00:00-06:00",
                "EndEpochDate": 1746860400,
                "MobileLink": "http://...",
                "Link": "http://..."
            },
            "DailyForecasts": [
                {
                    "Date": "2025-05-12T07:00:00-06:00",
                    "EpochDate": 1747054800,
                    "Temperature": {
                        "Minimum": {
                            "Value": 58,
                            "Unit": "F",
                            "UnitType": 18
                        },
                        "Maximum": {
                            "Value": 86,
                            "Unit": "F",
                            "UnitType": 18
                        }
                    },
                    "Day": {
                        "Icon": 4,
                        "IconPhrase": "Intermittent clouds",
                        "HasPrecipitation": False
                    },
                    "Night": {
                        "Icon": 34,
                        "IconPhrase": "Mostly clear",
                        "HasPrecipitation": False
                    },
                    "Sources": [
                        "AccuWeather"
                    ],
                    "MobileLink": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=1&lang=en-us",
                    "Link": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=1&lang=en-us"
                },
                {
                    "Date": "2025-05-13T07:00:00-06:00",
                    "EpochDate": 1747141200,
                    "Temperature": {
                        "Minimum": {
                            "Value": 62,
                            "Unit": "F",
                            "UnitType": 18
                        },
                        "Maximum": {
                            "Value": 88,
                            "Unit": "F",
                            "UnitType": 18
                        }
                    },
                    "Day": {
                        "Icon": 15,
                        "IconPhrase": "Thunderstorms",
                        "HasPrecipitation": True,
                        "PrecipitationType": "Rain",
                        "PrecipitationIntensity": "Light"
                    },
                    "Night": {
                        "Icon": 35,
                        "IconPhrase": "Partly cloudy",
                        "HasPrecipitation": False
                    },
                    "Sources": [
                        "AccuWeather"
                    ],
                    "MobileLink": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=2&lang=en-us",
                    "Link": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=2&lang=en-us"
                },
                {
                    "Date": "2025-05-14T07:00:00-06:00",
                    "EpochDate": 1747227600,
                    "Temperature": {
                        "Minimum": {
                            "Value": 63,
                            "Unit": "F",
                            "UnitType": 18
                        },
                        "Maximum": {
                            "Value": 87,
                            "Unit": "F",
                            "UnitType": 18
                        }
                    },
                    "Day": {
                        "Icon": 3,
                        "IconPhrase": "Partly sunny",
                        "HasPrecipitation": False
                    },
                    "Night": {
                        "Icon": 35,
                        "IconPhrase": "Partly cloudy",
                        "HasPrecipitation": False
                    },
                    "Sources": [
                        "AccuWeather"
                    ],
                    "MobileLink": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=3&lang=en-us",
                    "Link": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=3&lang=en-us"
                },
                {
                    "Date": "2025-05-15T07:00:00-06:00",
                    "EpochDate": 1747314000,
                    "Temperature": {
                        "Minimum": {
                            "Value": 62,
                            "Unit": "F",
                            "UnitType": 18
                        },
                        "Maximum": {
                            "Value": 87,
                            "Unit": "F",
                            "UnitType": 18
                        }
                    },
                    "Day": {
                        "Icon": 7,
                        "IconPhrase": "Cloudy",
                        "HasPrecipitation": True,
                        "PrecipitationType": "Rain",
                        "PrecipitationIntensity": "Light"
                    },
                    "Night": {
                        "Icon": 41,
                        "IconPhrase": "Partly cloudy w/ t-storms",
                        "HasPrecipitation": True,
                        "PrecipitationType": "Rain",
                        "PrecipitationIntensity": "Light"
                    },
                    "Sources": [
                        "AccuWeather"
                    ],
                    "MobileLink": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=4&lang=en-us",
                    "Link": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=4&lang=en-us"
                },
                {
                    "Date": "2025-05-16T07:00:00-06:00",
                    "EpochDate": 1747400400,
                    "Temperature": {
                        "Minimum": {
                            "Value": 60,
                            "Unit": "F",
                            "UnitType": 18
                        },
                        "Maximum": {
                            "Value": 86,
                            "Unit": "F",
                            "UnitType": 18
                        }
                    },
                    "Day": {
                        "Icon": 3,
                        "IconPhrase": "Partly sunny",
                        "HasPrecipitation": True,
                        "PrecipitationType": "Rain",
                        "PrecipitationIntensity": "Light"
                    },
                    "Night": {
                        "Icon": 34,
                        "IconPhrase": "Mostly clear",
                        "HasPrecipitation": False
                    },
                    "Sources": [
                        "AccuWeather"
                    ],
                    "MobileLink": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=5&lang=en-us",
                    "Link": "http://www.accuweather.com/en/mx/comitan-de-dominguez/1-231934_1_al/daily-weather-forecast/1-231934_1_al?day=5&lang=en-us"
                }
            ]
        },
        "premium_days": {
            "Code": "Unauthorized",
            "Message": "Api Authorization failed",
            "Reference": "/forecasts/v1/daily/10day/1-231934_1_AL?apikey=boMC0000070000000000i60000000000"
        }
    }

    @patch('requests.get')  # Replace 'your_module' with the actual module name
    def test_get_city_success(self, mock_get):
        # Sample JSON response
        sample_response = [{
            "Key": "1234",
            "LocalizedName": "Sample City",
            # Add other City fields with test data here
        }]

        # Mock the Response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_response
        mock_get.return_value = mock_response

        accuweather = AccuWeather()
        city = accuweather.get_city("Sample")

        # Validate
        assert city is not None
        assert isinstance(city, City)
        assert city.LocalizedName == "Sample City"
        # You can add more assertions on city attributes accordingly

    @patch('requests.get')
    def test_get_city_empty_list(self, mock_get):
        # When API returns an empty list
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        accuweather = AccuWeather()
        city = accuweather.get_city("Unknown")
        assert city is None

    @patch('requests.get')
    def test_get_city_error_response(self, mock_get):
        # Simulate an error response status
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        accuweather = AccuWeather()
        city = accuweather.get_city("ErrorCity")
        assert city is None

    # MARK: Forecast tests
    @patch('requests.get')
    @pytest.mark.parametrize(
        "forecast_days, expected_response, status", [
            (ForecastDays.ONE, forecast_sample_res.get("one_day"), 200),
            (ForecastDays.FIVE, forecast_sample_res.get("five_days"), 200),
            (ForecastDays.TEN, forecast_sample_res.get("premium_days"), 401),
            (ForecastDays.FIFTEEN, forecast_sample_res.get("premium_days"), 401)
        ]
    )
    def test_get_forecast_success(self, mock_get, forecast_days: ForecastDays, expected_response: dict, status: int):
        mock_response = Mock()
        mock_response.status_code = 200 if status == 200 else 401
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        forecast = AccuWeather()  # Instantiate your class
        forecast.API_KEY = 'test_key'  # Ensure API_KEY is set
        # Call the method
        result = forecast.get_n_day_forecast('some_location', forecast_days)

        # Validate
        assert result is not None

        if status == 200:
            assert isinstance(result, WeatherForecast)
            assert result.Headline.Severity == 5
            assert result.DailyForecasts[0].Temperature.Maximum.Value == 86
        else:
            assert result["Code"] == "Unauthorized"
            assert result["Message"] == "Api Authorization failed"

    @patch('requests.get')
    def test_get_1_day_forecast_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        forecast = AccuWeather()
        forecast.API_KEY = 'test_key'
        result = forecast.get_n_day_forecast('location', ForecastDays.ONE)

        assert result is None

    @patch('requests.get')
    def test_get_1_day_forecast_exception(self, mock_get):
        mock_get.side_effect = Exception("Network error")
        forecast = AccuWeather()
        forecast.API_KEY = 'test_key'
        result = forecast.get_n_day_forecast('location', ForecastDays.ONE)
        # Depending on your actual logger implementation,
        # you might need to patch the logger to prevent errors
        assert result is None
