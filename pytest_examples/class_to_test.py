import requests
from datetime import datetime

class ClassToTest:
    def add(self, x, y):
        if (not isinstance(x, int) and not isinstance(x, float)) or (not isinstance(y, int) and not isinstance(y, float)):
            raise TypeError("x and y must be ints or floats")
        return x+y

    def multiply(self, x, y):
        if (not isinstance(x, int) and not isinstance(x, float)) or (not isinstance(y, int) and not isinstance(y, float)):
            raise TypeError("x and y must be ints or floats")
        return x*y

    def divide(self, x, y):
        if (not isinstance(x, int) and not isinstance(x, float)) or (not isinstance(y, int) and not isinstance(y, float)):
            raise TypeError("x and y must be ints or floats")
        return x/y

    def get_current_time(self):
        return datetime.now()


    def _transform_data(self, api_response):
        return f"This was your {api_response['number_of_requests_made']} request."


    # Expected return value of this function:
    # A string which has the format: "This was your <int> request. You have <int> left this hour and <int> left today."
    def get_api_data(self):
        # Response should look like:
        # {
        #   "number_of_requests_made": <int>,
        #   "time_since_last_request": <string>
        #   "requests_left_this_hour": <int>,
        #   "requests_left_today": <int>,
        # }
        response = requests.get("https://fake_api_for_data.com")
        return self._transform_data(response)

