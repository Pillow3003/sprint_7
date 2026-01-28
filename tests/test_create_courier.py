import allure
import requests
from tests.handle import Handle
from urls import Urls
from data import Courier
from generator import register_new_courier
from generator import register_new_courier_without_login as gen_without_login
from generator import register_new_courier_without_login as gen_without_password


class TestCreateCourier:
    @staticmethod
    def _create_courier(*, request_body: dict) -> requests.Response:
        return requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', request_body)

    @allure.title('Создание курьера')
    def test_create_courier(self, remove_courier):
        response = self._create_courier(request_body=register_new_courier())
        assert response.status_code == 201
        assert response.json() == Courier.response_create_ok

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_was_created(self, remove_courier):
        response = self._create_courier(request_body=register_new_courier())
        assert response.status_code == 409
        assert response.json().get("message", "") == Courier.response_create_duplicate

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self, remove_courier):
        response = self._create_courier(request_body=gen_without_login())
        assert response.status_code == 400
        assert response.json().get("message", "") == Courier.response_create_not_full_data

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self, remove_courier):
        response = self._create_courier(request_body=gen_without_password())
        assert response.status_code == 400
        assert response.json().get("message", "") == Courier.response_create_not_full_data
