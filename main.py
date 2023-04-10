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

products=get_data("info.txt")




