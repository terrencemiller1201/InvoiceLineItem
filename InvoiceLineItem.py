# WK6Lab1 – Invoice Line Item Calculator
# Course no: CIS 261
# Name: Terrence Miller
# Date: 10/10/2019
# Description: This program will calculate the total cost of an invoice line item.
# Input: Price and quantity of an item.
# Output: The total cost of the item.

def get_price():
    try:
        price = float(input("Enter price: "))
        return price
    except ValueError:
        print("Invalid price")
        return get_price()

def get_quantity():
    try:
        quantity = int(input("Enter quantity: "))
        return quantity
    except ValueError:
        print("Invalid quantity")
        return get_quantity()

def compute_total(price, quantity):
    return price * quantity

def display_item(item):
    print("PRICE: ", item[0])
    print("QUANTITY: ", item[1])
    print("TOTAL: ", item[2])

def main():
    print("The Invoice Line Item Calculator\n")
    while True:
        price = get_price()
        quantity = get_quantity()
        total = compute_total(price, quantity)
        display_item([price, quantity, total])
        choice = input("Enter another line item? (y/n): ")
        if choice == 'n' or choice == 'N':
            print("\n")
            print("Bye!")
            break
        print("\n")

main()





