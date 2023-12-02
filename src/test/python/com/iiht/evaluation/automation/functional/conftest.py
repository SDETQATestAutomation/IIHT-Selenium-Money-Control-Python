import pytest


@pytest.fixture(scope="class")
def class_fixture():
    print("\nBefore class setup")
    yield
    print("\nAfter class setup")


@pytest.fixture()
def data():
    return ['data1', 'data2', 'data3']


@pytest.fixture(params=[
    {'user': 'user1', 'pass': 'pass1'},
    {'user': 'user2', 'pass': 'pass2'},
    {'user': 'user3', 'pass': 'pass3'}
])
def data_provider(request):
    return request.param
