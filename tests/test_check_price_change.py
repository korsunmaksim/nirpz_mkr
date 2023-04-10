import os
import datetime
import pytest
from main import *


@pytest.fixture
def test_data_file():
    file_path = "test_data.txt"
    file_data = [
        "Banana,1-3-2023,100",
        "Lemon,2-3-2023,200",
        "Banana,15-3-2023,110",
        "Banana, 1-4-2023,120",
        "Lemon, 2-4-2023,180",
        "Banana, 15-4-2023,130"
    ]
    with open(file_path, "w") as f:
        f.writelines(file_data)
    yield file_path
    os.remove(file_path)


@pytest.mark.parametrize("product_name, expected_output", [
    ("Banana", "The price of Banana in the last month : 10.0"),
    ("Lemon", "The price of Lemon in the last month : -20.0"),
    ("Product C", "There is no price changes in this month")
])
def test_check_price_change(product_name, expected_output, test_data_file):
    assert check_price_change(product_name, test_data_file) == expected_output
