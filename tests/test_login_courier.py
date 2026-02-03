import allure
import pytest
from tests.handle import Handle
from data import Courier


class TestLoginCourier:

    @allure.title('Авторизация под курьером выдает id')
    def test_courier_log_in(self, courier):
        requst_body = courier
        response = Handle.login_courier(request_body=requst_body)
        assert response.status_code == 200
        assert response.json().get("id") is not None
        assert response.json().get("id") > 0

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_courier_log_negative(self, courier):
        requst_body = courier
        requst_body['login'] = "invalid_login"
        response = Handle.login_courier(request_body=requst_body)
        assert response.status_code == 404
        assert response.json().get("message") == Courier.response_login_negative

    @pytest.mark.parametrize(
        'empty_key', 
        ["login", "password"]
    )
    @allure.title('Ошибка при авторизации если не зполнить логин или пароль')
    def test_courier_log_not_all_data(self, courier, empty_key):
        requst_body = courier
        requst_body[empty_key] = ""
        response = Handle.login_courier(request_body=requst_body)
        assert response.status_code == 400
        assert response.json().get("message") == Courier.response_login_not_full_data
