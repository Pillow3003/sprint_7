import allure
from handle import Handle


class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self, cancel_order):
        response = Handle.create_order()
        assert response.status_code == 200
        assert "orders" in response.json()
