import pytest
import requests

from data import Users
from generator import register_new_courier
from tests.handle import Handle
from urls import Urls


@pytest.fixture
def remove_courier():
    response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', register_new_courier)
    assert response.status_code == 201
    response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', data=Users.data_current())
    assert response.status_code == 200
    courier_id = response.json().get("id")
    yield
    response = requests.delete(f'{Urls.URL}{Handle.DELETE_COURIER.format(courier_id)}')
    assert response.status_code in [200, 404]
