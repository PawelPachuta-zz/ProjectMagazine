import sys

class Magazine:

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def show_av_products(self):
        print('Avaiable products:')
        for products in self.list_of_products:
            print(products)

    def add_product(self):
        self.product_name = input('Type a product name: >>> ')
        if self.product_name not in self.list_of_products:
            self.list_of_products.append(self.product_name)
        print(f'Product {self.product_name}has been added into the magazine')

    def delete_product(self):
        self.product_name = input('Type a product name, which you want to delete: >>> ')
        if self.product_name in self.list_of_products:
            self.list_of_products.remove(self.product_name)
            print('Product has been deleted')
        else:
            print('Product is not exists')


magazine = Magazine(['ipod', 'telephone', 'laptop'])

while True:
    print('Put 1 to show a magazine store.')
    print('Put 2 to add a product.')
    print('Put 3 to delete a product.')
    print('Put 4 to finish.')
    user_choice = int(input('>>> '))
    if user_choice == 1:
        magazine.show_av_products()
    elif user_choice == 2:
        magazine.add_product()
    elif user_choice == 3:
        magazine.delete_product()
    elif user_choice == 4:
        sys.exit()
