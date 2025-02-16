import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1"

UNIQUE_SELLER_ID = 1234345231

# Позитивный тест 1
# Создание объявления с корректными данными
def test_create_item_positive():
    payload = {
        "name": "Велосипед Format",
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    assert response.status_code == 200
    print("Тело ответа:", response.text)
    assert 'Сохранили объявление' in response.json()['status']

# Позитивный тест 2
# Создание объявления только с обязательными полями
def test_create_unique_item_positive():
    payload = {
        "name": "Велосипед Format",
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    assert response.status_code == 200
    print("Тело ответа:", response.text)
    assert 'Сохранили объявление' in response.json()['status']


# Позитивный тест 3
# Получение объявлений по item_id
def test_get_item_positive():
    item_id = 'a6d27f40-bbb7-406a-800c-47103c406b62'
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    print("Тело ответа:", response.text)
    assert response.status_code == 200
    item_data = response.json()
    assert isinstance(item_data, list)
    assert len(item_data) > 0


# Позитивный тест 4
# Получение объявлений по statistic_id
def test_get_statistic_positive():
    item_id = 'a6d27f40-bbb7-406a-800c-47103c406b62'
    response = requests.get(f"{BASE_URL}/statistic/{item_id}")
    print("Тело ответа:", response.text)
    assert response.status_code == 200
    item_data = response.json()
    assert isinstance(item_data, list)
    assert len(item_data) > 0


# Позитивный тест 5
# Получение объявлений по seller_id
def test_get_items_by_seller_id_positive():
    response = requests.get(f"{BASE_URL}/{UNIQUE_SELLER_ID}/item")
    print("Тело ответа:", response.text)
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)


# Негативный тест 1
# Создание объявления с пустыми полями
def test_create_item_negative_fields():
    response = requests.post(f"{BASE_URL}/item", json={})
    assert response.status_code == 500
    print("Тело ответа:", response.text)
    assert "internal error" in response.json()['message']


# Негативный тест 2
# Создание объявления с ценой в текстовом формате
def test_create_item_negative_price_string():
    payload = {
        "name": "Велосипед Format",
        "price": "Цена",
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']


# Негативный тест 3
# Создание объявления с отрицательной ценой
def test_create_item_negative_price_minus():
    payload = {
        "name": "Велосипед Format",
        "price": -1,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']


# Негативный тест 4
# Создание объявления с названием None
def test_create_item_negative_name():
    payload = {
        "name": None,
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Негативный тест 5
# Создание объявления с ценой None
def test_create_item_negative_price_none():
    payload = {
        "name": "Велосипед Format",
        "price": None,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']


# Негативный тест 6
# Создание объявления с названием и ценной None
def test_create_item_negative_pname_none():
    payload = {
        "name": None,
        "price": None,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']


# Негативный тест 7
# Создание объявления с максимальной ценой
def test_create_item_negative_price_max():
    payload = {
        "name": "Велосипед Format",
        "price": 10000000000000000000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    assert response.status_code == 500
    print("Тело ответа:", response.text)
    assert "internal error" in response.json()['message']


# Негативный тест 8
# Создание объявления с именем в числовом формате
def test_create_item_fake_name():
    payload = {
        "name": 666,
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Негативный тест 9
# Создание объявления со всеми отрицательными значениями в статистике
def test_create_item_stats_negative():
    payload = {
        "name": "Велосипед Format",
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": -10,
            "likes": -10,
            "viewCount": -10
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Негативный тест 10
# Создание объявления с отрицательным значением contacts в статистике
def test_create_item_stats_contact_negative():
    payload = {
        "name": "Велосипед Format",
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": -10,
            "likes": 10,
            "viewCount": 10
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Негативный тест 11
# Создание объявления с отрицательным значением likes в статистике
def test_create_item_stats_likes_negative():
    payload = {
        "name": "Велосипед Format",
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": -10,
            "viewCount": 10
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500

# Негативный тест 12
# Создание объявления с отрицательным значением viewCount в статистике
def test_create_item_stats_view_negative():
    payload = {
        "name": "Велосипед Format",
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": -10
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Негативный тест 13
# Создание объявления с None значениями в статистике
def test_create_item_stats_none():
    payload = {
        "name": "Велосипед Format",
        "price": 120000,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": None,
            "likes": None,
            "viewCount": None
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Негативный тест 14
# Получение несуществующего item_id
def test_get_item_negative1():
    item_id = '66666666666666666666'
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    print("Тело ответа:", response.text)
    assert response.status_code == 404
    item_data = response.json()


# Негативный тест 15
# Получение данных с текстом в item_id
def test_get_item_negative():
    item_id = "Tatata"
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    print("Тело ответа:", response.text)
    assert response.status_code == 404


# Негативный тест 16
# Получение данных по несуществующему seller_id
def test_get_items_by_seller_id_negative():
    nonexistent_seller_id = "149684144194154"
    response = requests.get(f"{BASE_URL}/{nonexistent_seller_id}/item")
    print("Тело ответа:", response.text)
    assert response.status_code == 404


# Негативный тест 17
# Создание объявления только с необязательными полями
def test_create_unique_item_negative():
    payload = {
        "statistics": {
            "contacts": 5,
            "likes": 100,
            "viewCount": 1000
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    assert response.status_code == 500
    print("Тело ответа:", response.text)
    assert 'Сохранили объявление' in response.json()['status']


# Негативный тест 18
# Создание объявления со всеми параметрами значения None
def test_create_all_none():
    payload = {
        "name": None,
        "price": None,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": None,
            "likes": None,
            "viewCount": None
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']



