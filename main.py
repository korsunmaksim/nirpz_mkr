import datetime

class Product:
    def __init__(self,name,date,price):
        self.name=name
        self.date=date
        self.price=price


def get_data(file_path):
    info=[]
    file=open(file_path,'r')
    for line in file:
        line = line.strip().split(',')
        product=Product(line[0], datetime.datetime.strptime(line[1], '%d-%m-%Y'),float(line[2]))
        info.append(product)
    return info


def check_price_change(product_name,file_path):
    date=datetime.datetime
    current_month = date.now().month
    last_month = current_month - 1 if current_month > 1 else 12
    last_month_year = date.now().year if last_month != 12 else datetime.datetime.now().year - 1
    last_month_start = date(last_month_year, last_month, 1)
    last_month_end = date(last_month_year, last_month, 1) + datetime.timedelta(days=31)
    products=get_data(file_path)
    month_prices = []
    for product in products:
        if product.name == product_name and product.date >= last_month_start and product.date < last_month_end:
            month_prices.append(product.price)
    if len(month_prices) == 0:
        return "There is no price changes in this month"
    price_change = (month_prices[-1] - month_prices[0]) 
    return f"The price of {product_name} in the last month : {price_change}"


product_name = "Banana"
print(check_price_change(product_name,"info.txt"))









