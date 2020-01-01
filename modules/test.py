from modules.utility import multiply, divide
from modules.shopping.more_shopping import shopping_cart

# Only runs if the current file is ran.
if __name__ == '__main__':
    print(shopping_cart.buy('apple'))
    print(divide(5, 2))
    print(multiply(5, 2))
    print(max([1,2,3]))

    print('please run this')