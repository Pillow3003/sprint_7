import requests
from urls import Urls

class Handle:

    CREATE_COURIER = '/api/v1/courier'

    DELETE_COURIER = "/api/v1/courier/{0}"

    LOGIN_COURIER = '/api/v1/courier/login'

    CREATE_ORDER = '/api/v1/orders'

    CANCEL_ORDER = "/api/v1/orders/cancel"

    LIST_ORDER = '/api/v1/orders'

    @staticmethod
    def login_courier(*, request_body: dict) -> requests.Response:
        return requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', data=request_body)

    @staticmethod
    def create_courier(*, request_body: dict) -> requests.Response:
        return requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', request_body)
    
    @staticmethod
    def delete_courier(*, courier_id: int) -> requests.Response:
        return requests.delete(f'{Urls.URL}{Handle.DELETE_COURIER.format(courier_id)}')

    @staticmethod
    def create_order(*, request_body: dict = None, headers: dict = None) -> requests.Response:
        return requests.post(f'{Urls.URL}{Handle.CREATE_ORDER}', data=request_body, headers=headers)

    @staticmethod
    def list_order() -> requests.Response:
        return requests.get(f'{Urls.URL}{Handle.LIST_ORDER}')

    @staticmethod
    def cancel_order(*, order_id: int) -> requests.Response:
        return requests.put(f"{Urls.URL}{Handle.CANCEL_ORDER}", data={"track": order_id})
    