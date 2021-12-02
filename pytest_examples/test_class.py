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
