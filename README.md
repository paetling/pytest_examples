## Steps for getting installing the repo

1. Clone the repo
2. Move into the newly cloned directory
3. `pip3 install -r requirements.txt`




## Steps for running tests
In this directory run `pytest pytest_examples`


## Steps to follow for this Repo
1. Add a class for testing the multiply method. Ensure you cover a representative set of inputs. Make a PR.
2. Add a class for testing the divide method. Ensure you cover a representative set of inputs. Make a PR.
3. Read up on [pytest fixtures](https://docs.pytest.org/en/6.2.x/fixture.html). Chat with alex if you have any questions.
4. Create a custom pytest fixture that gives you a class instance so that you do not have to manually create it in all tests. Change one of your tests to use it. Make a PR.
5. Add a class for testing the get_current_time method. Ensure you use the [pytest-freezegun](https://pypi.org/project/pytest-freezegun/). Make a PR.
6. Add a class for testing get_api_data and fix any bugs. Ensure that you use [pytest-mock](https://github.com/pytest-dev/pytest-mock). Make a PR.
7. Add a function for testing get_the_maximum_value and fix any bugs. Make a PR.
    1. Write down for yourself what the function is trying to do
    2. Write down what data or examples that would convince you it is working
    3. Turn those examples into tests
