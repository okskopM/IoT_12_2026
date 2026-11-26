class Smartphone:
    def __init__(self, model, price, storage, battery, phone_numbers=None):
        self.model = model
        self.price = price
        self.storage = storage
        self.battery = battery
        self.phone_numbers = phone_numbers if phone_numbers is not None else []


    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_storage(self):
        return self.storage

    def set_storage(self, storage):
        self.storage = storage

    def get_battery(self):
        return self.battery

    def set_battery(self, battery):
        self.battery = battery

    def get_phone_numbers(self):
        return self.phone_numbers

    def set_phone_numbers(self, phone_numbers):
        self.phone_numbers = phone_numbers

    def display_info(self):
        print(self.price, self.model, self.storage, self.battery, self.phone_numbers)

    def __del__(self):
        print(f"Об'єкт {self.model} видалено")

    class PhoneStore:
        def __init__(self, phones=None):
            self.phones = phones if phones is not None else []

    def add_phone(self, phone):
        self.phones.append(phone)

    def show_sorted_by_price(self):
        sorted_phones = sorted(self.phones, key=lambda phone: phone.price)

        for phone in sorted_phones:
            phone.display_info()
            print("-" * 20)

    def get_best_by_budget(self, max_budget):
        best_phone = None
        for phone in self.phones:
            if phone.price <= max_budget:
                if best_phone is None or phone.price > best_phone.price:
                    best_phone = phone

        return best_phone

if __name__ == "__main__":
    phone1 = Smartphone("Nokia", 2500, 32, 80, ["+380501234567"])
    phone2 = Smartphone("Pixel", 25000, 512, 100, ["+380679876543", "+380931112233"])
    phone3 = Smartphone("Samsung Galaxy",  12000, 128, 90, ["+380995554433"])

    store = PhoneStore()

    store.add_phone(phone1)
    store.add_phone(phone2)
    store.add_phone(phone3)

    print("Список всіх телефонів за ціною")
    store.show_sorted_by_price()

    print("Пошук найкращого телефону за бюджетом")
    budget = 15000
    best_phone = store.get_best_by_budget(budget)

    if best_phone:
        print(f"Найкращий телефон за budget <= {budget} грн:")
        best_phone.display_info()
    else:
        print("На жаль, за таким бюджетом телефонів немає")






