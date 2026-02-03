import pytest

from generator import register_new_courier
from handle import Handle
from data import Orders


@pytest.fixture
def get_order_data_and_cancel_order():
    order_data = Orders.data_order
    yield order_data
    Handle.cancel_order(order_data['id'])


@pytest.fixture
def get_courier_data_and_remove_courier():
    """
    Генерируем данные курьера и передаём их в тест.
    После теста удаляем курьера, если он существует.
    """
    courier_data = register_new_courier()
    yield courier_data
    response = Handle.login_courier(
        request_body={
            "login": courier_data["login"],
            "password": courier_data["password"],
        }
    )
    if response.status_code == 200:
        Handle.delete_courier(courier_id=response.json().get("id"))


@pytest.fixture
def courier():
    """
    Создаёт и удаляет курьера
    """
    courier_data = register_new_courier()
    Handle.create_courier(request_body=courier_data)
    yield {"login": courier_data["login"], "password": courier_data["password"]}
    courier_data.pop("name")
    response = Handle.login_courier(request_body=courier_data)
    Handle.delete_courier(courier_id=response.json().get("id"))
