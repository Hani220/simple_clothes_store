from Clothes import Shirt, Pants, Shoes

num_items = 0
while True:
    try:
        num_items = int(input("Enter the number of items you bought: "))
        if num_items <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

total_amount = 0.0
items = []

print()

for _ in range(num_items):
    while True:
        try:
            clothes_type = input("Enter the type of clothes (shirt, pants, shoes): ")
            if clothes_type not in ['shirt', 'pants', 'shoes']:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter either 'shirt', 'pants', or 'shoes'.")

    model_year = 0
    while True:
        try:
            model_year = int(input("Enter the model year: "))
            if model_year <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the model year.")

    brand = input("Enter the brand: ")
    price = 0.0
    while True:
        try:
            price = float(input("Enter the price: "))
            if price <= 0.0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive number for the price.")

    if clothes_type == 'shirt':

        while True:
            try:
                size = input("Enter the size (XL, L, M, S): ")
                if size not in ['XL', 'L', 'M', 'S']:
                    raise ValueError
                break
            except ValueError:
                print("Invalid size. Please enter XL, L, M or S.")

        clothes = Shirt(model_year, brand, price, size)
    elif clothes_type == 'pants':
        width = 0.0
        height = 0.0
        while True:
            try:
                width = float(input("Enter the width: "))
                height = float(input("Enter the height: "))
                if width <= 0.0 or height <= 0.0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter valid positive numbers for width and height.")
        clothes = Pants(model_year, brand, price, width, height)
    elif clothes_type == 'shoes':
        size = 0.0
        while True:
            try:
                size = float(input("Enter the size: "))
                if size <= 0.0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a valid positive number for size.")
        clothes = Shoes(model_year, brand, price, size)

    items.append(clothes)
    final_price, _, _ = clothes.calculate_final_price()
    total_amount += final_price
    print()

print("----- Receipt -----")
for i, item in enumerate(items):
    final_price, discount_info, model_year_discount_info = item.calculate_final_price()
    print(f"Item {i+1}: {item.brand} {item.clothes_type.capitalize()} - Final Price: {final_price:.2f}")
    print(f"Discounts Applied: {discount_info}")
    print(f"Model Year Discount: {model_year_discount_info}")
    print()
print(f"Total Amount: {total_amount:.2f}")