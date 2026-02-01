import json
import allure
import pytest
from data import Orders
from tests.handle import Handle


class TestCreateOrder:
    @pytest.mark.parametrize(
        'order_data',
        [
            {"color": ["BLACK"]}, {"color": ["GREY"]},
            {"color": [""]}, {"color": ["BLACK", "GREY"]}
         ]
    )
    @allure.title('Создание заказа')
    def test_create_order(self, cancel_order, order_data):
        Orders.data_order.update(order_data)
        response = Handle.create_order(request_body=json.dumps(Orders.data_order), headers={'Content-Type': 'application/json'})
        assert response.status_code == 201
        assert response.json().get("track") is not None
        assert response.json().get("track") > 0
