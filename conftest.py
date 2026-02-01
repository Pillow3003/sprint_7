import pytest

from data import Users
from generator import register_new_courier
from tests.handle import Handle


@pytest.fixture
def cancel_order():
    yield
    Handle.cancel_order()


@pytest.fixture
def remove_courier():
    Handle.create_courier(request_body=register_new_courier)
    response = Handle.login_courier(request_body=Users.data_current())
    courier_id = response.json().get("id")
    yield
    Handle.delete_courier(courier_id=courier_id)
