import json
import allure
import pytest
import requests
from data import Orders
from tests.handle import Handle
from urls import Urls


@pytest.fixture
def remove_order():
    yield
    # удалить через API невозможно, есть только отмена заказа, а это не имеет смысла, т.к. сущность
    # продолжит существовать. Тут должно быть удаление напрямую чыерез БД.


class TestCreateOrder:
    @pytest.mark.parametrize(
        'order_data',
        [
            {"color": ["BLACK"]}, {"color": ["GREY"]},
            {"color": [""]}, {"color": ["BLACK", "GREY"]}
         ]
    )
    @allure.title('Создание заказа')
    def test_create_order(self, order_data):
        Orders.data_order.update(order_data)
        order_data = json.dumps(Orders.data_order)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{Urls.URL}{Handle.CREATE_ORDER}', data=order_data, headers=headers)
        assert response.status_code == 201
        assert response.json().get("track") is not None
        assert response.json().get("track") > 0
