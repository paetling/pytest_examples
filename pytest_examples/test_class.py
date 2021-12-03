import pytest

from pytest_examples.class_to_test import ClassToTest


class TestAdd:
    def test_add_strings(self):
        instance = ClassToTest()
        with pytest.raises(TypeError):
            instance.add("1", "2")

    def test_add_arrays(self):
        instance = ClassToTest()
        with pytest.raises(TypeError):
            instance.add([1,2,3], 1)

    def test_add_ints(self):
        instance = ClassToTest()
        assert instance.add(1, 2) == 3
        assert instance.add(-1, 2) == 1
        assert instance.add(0, 0) == 0

    def test_add_floats(self):
        instance = ClassToTest()
        assert instance.add(1.2, 2.1) == pytest.approx(3.3)
        assert instance.add(-1.1, 2.1) == pytest.approx(1)
        assert instance.add(0.0, 1.5) == pytest.approx(1.5)

    def test_add_floats_and_int(self):
        instance = ClassToTest()
        assert instance.add(1, 2.1) == pytest.approx(3.1)


class TestMultiple:
    def test_multiple_string(self):
        instance = ClassToTest()
        with pytest.raises(TypeError):  
            instance.multiply("2", "3")  

    def test_multiple_arrays(self):
        instance = ClassToTest()
        with pytest.raises(TypeError): 
            instance.multiply([3, 4, 5], 1)

    def test_multiple_ints(self):
        instance = ClassToTest()
        assert instance.multiply(2, 3) == 6
        assert instance.multiply(3, 3) == 9
        assert instance.multiply(6, 2) == 12

    def test_multiple_floats(self):
        instance = ClassToTest()
        instance.multiply(2.1, 3.2) 
        assert instance.multiply(1.2, 2.1) == pytest.approx(2.52)
        assert instance.multiply(-1.1, 2.1) == pytest.approx(-2.31)
        assert instance.multiply(0.0, 1.5) == pytest.approx(0)

    def test_multiple_floats_and_int(self): 
        instance = ClassToTest()
        assert instance.multiply(1, 2.1) == pytest.approx(2.1)      







