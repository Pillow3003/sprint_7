import allure
import pytest
from tests.handle import Handle
from data import Users, Courier


class TestLoginCourier:

    @allure.title('Авторизация под курьером выдает id')
    def test_courier_log_in(self):
        response = Handle.login_courier(request_body=Users.data_current)
        assert response.status_code == 200
        assert response.json().get("id") is not None
        assert response.json().get("id") > 0

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_courier_log_negative(self):
        response = Handle.login_courier(request_body=Users.data_negative)
        assert response.status_code == 404
        assert response.json().get("message") == Courier.response_login_negative

    @pytest.mark.parametrize('data_without_login_or_password', [Users.data_without_login, Users.data_without_password])
    @allure.title('Ошибка при авторизации если не зполнить логин или пароль')
    def test_courier_log_not_all_data(self, data_without_login_or_password):
        response = Handle.login_courier(request_body=data_without_login_or_password)
        assert response.status_code == 400
        assert response.json().get("message") == Courier.response_login_not_full_data
