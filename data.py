class Users:
    data_current = {
        "login": "ninjafdfdf666",
        "password": "1234666"
    }
    data_negative = {
        "login": "test181920",
        "password": "19874634"
    }
    data_without_login = {
        "login": "",
        "password": "19874634"
    }
    data_without_password = {
        "login": "test181920",
        "password": ""
    }


class Orders:
    data_order = {
        "firstName": "Test",
        "lastName": "Testov",
        "address": "MSK, street 5555.",
        "metroStation": 5,
        "phone": "+7 111 222 33 33",
        "rentTime": 6,
        "deliveryDate": "2024-04-25",
        "comment": "Test",
        "color": [
            "BLACK"
        ]
    }


class Courier:
    response_create_ok = {"ok": True}
    response_create_duplicate = {"message": "Этот логин уже используется"}
    response_create_not_full_data = {"message": "Недостаточно данных для создания учетной записи"}

    response_login_negative = {"message": "Учетная запись не найдена"}
    response_login_not_full_data = {"message": "Недостаточно данных для входа"}

