import os
import datetime
from main import *


def test_get_data():
    file_path = "test_data.txt"
    file_data = [
        "Banana,1-3-2023,100\n",
        "Lemon,2-3-2023,200\n",
        "Banana,15-3-2023,110\n",
        "Banana,1-4-2023,120\n",
        "Lemon,2-4-2023,180\n",
        "Banana,15-4-2023,130\n"
    ]
    with open(file_path, "w") as f:
        f.writelines(file_data)
    
    expected_data = [
        Product("Banana", datetime.datetime(1,3,2023), 100.00),
        Product("Lemon", datetime.datetime(2,3,2023), 200.00),
        Product("Product A", datetime.datetime(15,3,2023), 110.00),
        Product("Product A", datetime.datetime(1,4,2023), 120.00),
        Product("Lemon", datetime.datetime(2,4,2023), 180.00),
        Product("Product A", datetime.datetime(15, 4, 2023), 130.00)
    ]
    
    assert get_data(file_path) == expected_data
    
    os.remove(file_path)


def test_check_price_change():
    file_path = "test_data.txt"
    file_data = [
        "Banana, 1-3-2023, 100\n",
        "Lemon, 2-3-2023, 200\n",
        "Banana, 15-3-2023, 110\n",
        "Banana, 1-4-2023, 120\n",
        "Lemon, 2-4-2023, 180\n",
        "Banana, 15-4-2023, 130\n"
    ]
    with open(file_path, "w") as f:
        f.writelines(file_data)
    
    assert check_price_change("Banana", file_path) == "The price of Banana in the last month : 10.0"
    assert check_price_change("Lemon", file_path) == "The price of Lemon in the last month : -20.0"
    assert check_price_change("Product C", file_path) == "There is no price changes in this month"
    
    os.remove(file_path)
