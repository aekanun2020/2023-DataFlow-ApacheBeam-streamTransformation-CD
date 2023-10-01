import pytest
from ..your_project_name.cleanse_data_module import cleanse_data


def test_cleanse_data_string_fields():
    data = {
        "tr_time_str": " 2022-10-01 10:10:10 ",
        "first_name": " John ",
        "last_name": " Doe ",
        "city": " New York ",
        "state": " NY ",
        "product": " Laptop "
    }

    cleansed_data = cleanse_data(data)

    assert cleansed_data["tr_time_str"] == "2022-10-01 10:10:10"
    assert cleansed_data["first_name"] == "John"
    assert cleansed_data["last_name"] == "Doe"
    assert cleansed_data["city"] == "New York"
    assert cleansed_data["state"] == "NY"
    assert cleansed_data["product"] == "Laptop"

def test_cleanse_data_invalid_amount():
    data = {
        "amount": "invalid_amount"
    }

    cleansed_data = cleanse_data(data)

    assert cleansed_data["amount"] == None

def test_cleanse_data_valid_amount():
    data = {
        "amount": "100.5"
    }

    cleansed_data = cleanse_data(data)

    assert cleansed_data["amount"] == 100.5

def test_cleanse_data_valid_date():
    data = {
        "tr_time_str": "2022-10-01 10:10:10"
    }

    cleansed_data = cleanse_data(data)

    assert cleansed_data["dayofweek"] == 5  # Saturday

def test_cleanse_data_invalid_date():
    data = {
        "tr_time_str": "invalid_date"
    }

    cleansed_data = cleanse_data(data)

    assert cleansed_data["dayofweek"] == None


