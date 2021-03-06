import pytest

from pytest_examples.class_to_test import ClassToTest

from datetime import datetime

import os 

@pytest.fixture
def any_fit():
    return ClassToTest()


class TestGetCurrent:
    def test_current_time(self, any_fit, freezer):
        freezer.move_to('2021-12-15')
        assert any_fit.get_current_time() == datetime(2021, 12, 15)

        freezer.move_to('2021-12-12')
        assert any_fit.get_current_time() == datetime(2021, 12, 12)

        freezer.move_to('2021-12-16')
        assert any_fit.get_current_time() == datetime(2021, 12, 16)

        freezer.move_to('2021-12-11')
        assert any_fit.get_current_time() == datetime(2021, 12, 11)


class TestGetApiData:
    def test_get_request(self, mocker, any_fit): 
        mock_remove = mocker.patch('pytest_examples.class_to_test.requests.get')  
        mock_remove.return_value =  {
          "number_of_requests_made": 1,
          "time_since_last_request": 'yani',
          "requests_left_this_hour": 4,
          "requests_left_today": 5,
        }

        assert any_fit.get_api_data() == "This was your 1 request."

        mock_remove.return_value =  {
          "number_of_requests_made": 3,
          "time_since_last_request": 'joe',
          "requests_left_this_hour": 3,
          "requests_left_today": 2,
        }

        assert any_fit.get_api_data() == "This was your 3 request."

       
        mock_remove.return_value =  {
          "number_of_requests_made": "3",
          "time_since_last_request": 'joe',
          "requests_left_this_hour": 3,
          "requests_left_today": 2,
        }

        assert any_fit.get_api_data() == "This was your 3 request."


         
        mock_remove.return_value =  {
          "number_of_requests_made": 3.5,
          "time_since_last_request": 'joe',
          "requests_left_this_hour": 3,
          "requests_left_today": 2,
        }

        assert any_fit.get_api_data() == "This was your 3.5 request."

    


class TestAdd:
    def test_add_strings(self, any_fit):
        with pytest.raises(TypeError):
            any_fit.add("1", "2")

    def test_add_arrays(self, any_fit):
        with pytest.raises(TypeError):
            any_fit.add([1,2,3], 1)

    def test_add_ints(self, any_fit):
        assert any_fit.add(1, 2) == 3
        assert any_fit.add(-1, 2) == 1
        assert any_fit.add(0, 0) == 0

    def test_add_floats(self, any_fit):
        assert any_fit.add(1.2, 2.1) == pytest.approx(3.3)
        assert any_fit.add(-1.1, 2.1) == pytest.approx(1)
        assert any_fit.add(0.0, 1.5) == pytest.approx(1.5)

    def test_add_floats_and_int(self, any_fit):
        assert any_fit.add(1, 2.1) == pytest.approx(3.1)


class TestMultiple:
    def test_multiple_string(self, any_fit):
        with pytest.raises(TypeError):  
            any_fit.multiply("2", "3")  

    def test_multiple_arrays(self, any_fit):
        with pytest.raises(TypeError): 
            any_fit.multiply([3, 4, 5], 1)

    def test_multiple_ints(self, any_fit):
        assert any_fit.multiply(2, 3) == 6
        assert any_fit.multiply(3, 3) == 9
        assert any_fit.multiply(6, 2) == 12
        assert any_fit.multiply(-1, 3) == -3
        assert any_fit.multiply(0, 3) == 0
        assert any_fit.multiply(-3, -4) == 12 

    def test_multiple_floats(self, any_fit):
        assert any_fit.multiply(1.2, 2.1) == pytest.approx(2.52)
        assert any_fit.multiply(-1.1, 2.1) == pytest.approx(-2.31)
        assert any_fit.multiply(0.0, 1.5) == pytest.approx(0)

    def test_multiple_floats_and_int(self, any_fit): 
        assert any_fit.multiply(1, 2.1) == pytest.approx(2.1)      



class TestDivide:
    def test_divide_string(self, any_fit):
        with pytest.raises(TypeError):
            any_fit.divide("5", "6")

    def test_divide_array(self, any_fit):
        with pytest.raises(TypeError):
            any_fit.divide([1, 6, 7], [6, 7, 8])

    def test_divide_int(self, any_fit):
        assert any_fit.divide(4, 2) == 2
        assert any_fit.divide(10, 2) == 5
        assert any_fit.divide(6, 2) == 3
        assert any_fit.divide(0, 10) == 0
        assert any_fit.divide(-2, 10) == -0.2
        with pytest.raises(ZeroDivisionError):
             any_fit.divide(5, 0)

    def test_divide_floats(self, any_fit):
        assert any_fit.divide(0.0, 1.5) == pytest.approx(0)

    def test_divide_floats_and_int(self, any_fit):
        assert any_fit.multiply(1, 2.1) == pytest.approx(2.1)


def test_get_max_value(mocker, any_fit):
    mock_remove = mocker.patch('pytest_examples.class_to_test.requests.get')  
    mock_remove.return_value = {
          "number_1": 1,
          "number_2": 2,
          "number_3": 3,
          "number_4": 4,
          "number_5": 5,
        }
    assert any_fit.get_the_maximum_value() == 5    
    
    mock_remove.return_value = {
          "number_1": 1,
          "number_2": 2,
          "number_3": 3,
          "number_4": 5,
          "number_5": 4,
        }
    assert any_fit.get_the_maximum_value() == 5

    mock_remove.return_value = {
          "number_1": 1,
          "number_2": 2,
          "number_3": 5,
          "number_4": 3,
          "number_5": 4,
        }
    assert any_fit.get_the_maximum_value() == 5

    mock_remove.return_value = {
          "number_1": 1,
          "number_2": 5,
          "number_3": 2,
          "number_4": 3,
          "number_5": 4,
        }
    assert any_fit.get_the_maximum_value() == 5


    mock_remove.return_value = {
          "number_1": 5,
          "number_2": 1,
          "number_3": 2,
          "number_4": 3,
          "number_5": 4,
        }
    assert any_fit.get_the_maximum_value() == 5



