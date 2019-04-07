import pytest
import requests


class Client:

    def get(self, url, header=""):
        head = dict({"Content_type": header})
        return requests.get(url, head)

    def post(self, url, header):
        head = dict({"Content_type": header})
        return requests.post(url, headers=head)


@pytest.fixture
def client():
    return Client()


@pytest.fixture(scope="module", autouse=True)
def start_module(request):
    print('\nStart - module fixture')

    def fin():
        print('\nStop - module fixture')

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def start_class(request):
    print('\nStart - test class fixture')

    def fin():
        print('\nStop - test class fixture')

    request.addfinalizer(fin)

# ####################### HOME WORK 3 #################################


types = ["application/json", "text/html"]


@pytest.fixture(scope="function")
def test_dog_code():
    print('\nCheck status code')
    return "african"


@pytest.fixture(scope="function")
def test_dog_status():
    print('\nCheck status request')
    return "african"


@pytest.fixture(scope="function")
def test_dog_header():
    print('\nChecke content')
    return ["african", types]


@pytest.fixture(scope="function")
def test_brewery_status():
    page = [1, 2, 3]
    ppage = [10, 20, 30]
    pairs = [(p, pp) for p in page for pp in ppage]
    print('\ncheck status and type of id')
    return pairs


@pytest.fixture(scope="function")
def test_brewery_state():
    state = ["alabama", "california", "colorado", "arkansas"]
    print('\ncheck content')
    return state


@pytest.fixture(scope="function")
def test_header():
    lib = ["10up-sanitize.css", "1000hz-bootstrap-validator", "6to5"]
    hed = ["application/json"]
    pairs = [(p, pp) for p in lib for pp in hed]
    print('\nChecke content')
    return pairs


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


