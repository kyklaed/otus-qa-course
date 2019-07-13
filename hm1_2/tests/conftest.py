import pytest
import requests

head = dict({"Content_type": "application/json"})


class Client:

    def __init__(self, address='', head2=''):
        self.address = address
        if head2 == '':
            self.head = head
        else:
            self.head = head2

    def get(self, endpoint=None):
        url = "/".join([self.address, endpoint])
        print(url)
        return requests.get(url)





urls = ['https://dog.ceo/api/breeds/image/random', 'https://api.openbrewerydb.org/breweries',
        'https://api.cdnjs.com/libraries']
headers = [{"Content-type": "application/json"}]
pairs = [(url, header) for url in urls for header in headers]


@pytest.fixture(params=pairs)
def client2(request):
    return Client(request.param[0], request.param[1])


@pytest.fixture(scope="module", autouse=True)
def start_module(request):
    print('\nStart - module fixture')

    def fin():
        print('\nStop - module fixture')

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def start_class(request):
    print('\nStart - tests class fixture')

    def fin():
        print('\nStop - tests class fixture')

    request.addfinalizer(fin)



# ####################### HOME WORK 2 #################################
@pytest.fixture(scope="function")
def test_to_int():
    print("\nCheck type int")
    return 10


@pytest.fixture(scope="function")
def test_to_float():
    print("\nCheck type float")
    return 1.2


@pytest.fixture(scope="function")
def test_to_list():
    print("\nCheck type list")
    return list([1, 2, 3, 4, 5])


@pytest.fixture(scope="function")
def test_to_string():
    print("\nCheck type string")
    return "homework"


@pytest.fixture(scope="function")
def test_to_tuple():
    print("\nCheck type tuple")
    return tuple((1, 2, 3))


@pytest.fixture(scope="function")
def test_check_content():
    print("\nCheck dict")
    return {0: "0", 1: "1", 2: "2"}


@pytest.fixture(scope="function")
def test_append_in_list():
    print("\nCheck append in list")
    return list([1, 2, 3, 4, 5, 6, 7, 8, 9])


@pytest.fixture(scope="function")
def test_subtraction():
    print("\nCheck type subtraction")
    return tuple((10, 10))

@pytest.fixture(scope="function")
def test_addition_row():
    print("\nCheck addition row")
    return tuple(("home", "work"))


