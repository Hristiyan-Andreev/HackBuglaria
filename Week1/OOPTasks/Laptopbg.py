class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self, stock_price, final_price):
        return final_price - stock_price


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, Disk, RAM):
        super().__init__(name, stock_price, final_price)
        self.Disk = Disk
        self.Ram = RAM


class Smartphone(Product):

    all_smartphones = 0

    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store():

    def __init__(self, name):
        self.name = name
        self.products = {}

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        print(self.products)
        for product in self.products:
            if isinstance(product, product_class):
                print("Name: {} Count: {}".format(product.name, self.products[product]))

    def sell_product(self, product):
        if product in self.products:
            if self.products[product] > 0:
                return True
            else:
                return False
        else:
            return False

    def total_income(self):
        profit = 0

        for product in self.products:
            profit += product.profit()

        return profit


def main():
    store = Store('Laptop.bg')
    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
    store.load_new_products(smarthphone, 0)
    store.load_new_products(laptop, 10)
    store.list_products(Laptop)
    print(store.sell_product(laptop))
    print(store.sell_product(smarthphone))
    print(store.total_income)

if __name__ == '__main__':
    main()
