from datetime import datetime

#C:\Users\hanyo\PycharmProjects\sic_store
class Clothes:
    def __init__(self, clothes_type, model_year, brand, price):
        self.clothes_type = clothes_type
        self.model_year = model_year
        self.brand = brand
        self.price = price

    def calculate_final_price(self):
        discount, discount_info = self.get_discount()
        model_year_discount, model_year_discount_info = self.get_model_year_discount()
        final_price = self.price - (self.price * (discount + model_year_discount))
        return final_price, discount_info, model_year_discount_info

    def get_discount(self):
        if self.clothes_type == 'shirt':
            discount = 0.3
            discount_info = "30% off for shirts"
        elif self.clothes_type == 'pants':
            discount = 0.4
            discount_info = "40% off for pants"
        elif self.clothes_type == 'shoes':
            discount = 0.5
            discount_info = "50% off for shoes"
        else:
            discount = 0
            discount_info = "No discount"
        return discount, discount_info

    def get_model_year_discount(self):
        current_year = datetime.now().year
        year_difference = current_year - self.model_year
        if year_difference > 0:
            model_year_discount = 0.02 * year_difference
            model_year_discount_info = f"Additional {year_difference * 2}% off for {year_difference}-year-old item"
        else:
            model_year_discount = 0
            model_year_discount_info = "No additional model year discount"
        return model_year_discount, model_year_discount_info


class Shirt(Clothes):
    def __init__(self, model_year, brand, price, size):
        super().__init__('shirt', model_year, brand, price)
        self.size = size

    def get_discount(self):
        discount, discount_info = super().get_discount()
        model_year_discount, model_year_discount_info = self.get_model_year_discount()
        return discount, f"{discount_info}, {model_year_discount_info}"


class Pants(Clothes):
    def __init__(self, model_year, brand, price, width, height):
        super().__init__('pants', model_year, brand, price)
        self.width = width
        self.height = height

    def get_discount(self):
        discount, discount_info = super().get_discount()
        model_year_discount, model_year_discount_info = self.get_model_year_discount()
        return discount, f"{discount_info}, {model_year_discount_info}"


class Shoes(Clothes):
    def __init__(self, model_year, brand, price, size):
        super().__init__('shoes', model_year, brand, price)
        self.size = size

    def get_discount(self):
        discount, discount_info = super().get_discount()
        model_year_discount, model_year_discount_info = self.get_model_year_discount()
        return discount, f"{discount_info}, {model_year_discount_info}"