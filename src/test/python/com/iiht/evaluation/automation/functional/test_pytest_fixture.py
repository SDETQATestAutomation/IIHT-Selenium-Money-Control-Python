import pytest


@pytest.fixture(scope="class")
def class_fixture():
    print("\nBefore class setup")
    yield
    print("\nAfter class setup")


@pytest.fixture()
def method_fixture():
    print("\nBefore method setup")
    yield
    print("\nAfter method setup")
