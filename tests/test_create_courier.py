import allure
from tests.handle import Handle
from data import Courier


class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier(self, get_courier_data_and_remove_courier):
        request_body = get_courier_data_and_remove_courier
        response = Handle.create_courier(request_body=request_body)
        assert response.status_code == 201
        assert response.json() == Courier.response_create_ok

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_was_created(self, get_courier_data_and_remove_courier):
        request_body = get_courier_data_and_remove_courier
        response = Handle.create_courier(request_body=request_body)
        assert response.status_code == 201, 'Не удалось создать первого курьера'
        response = Handle.create_courier(request_body=request_body)
        assert response.status_code == 409
        assert response.json().get("message", "") == Courier.response_create_duplicate

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self, get_courier_data_and_remove_courier):
        request_body = get_courier_data_and_remove_courier
        request_body.pop("login")
        response = Handle.create_courier(request_body=request_body)
        assert response.status_code == 400
        assert response.json().get("message", "") == Courier.response_create_not_full_data

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self, get_courier_data_and_remove_courier):
        request_body = get_courier_data_and_remove_courier
        request_body.pop("password")
        response = Handle.create_courier(request_body=request_body)
        assert response.status_code == 400
        assert response.json().get("message", "") == Courier.response_create_not_full_data
