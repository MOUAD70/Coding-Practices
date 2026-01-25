def mango(quantity, price):
    return (int(quantity) - int(quantity / 3)) * price 

print(mango(20, 9.99))