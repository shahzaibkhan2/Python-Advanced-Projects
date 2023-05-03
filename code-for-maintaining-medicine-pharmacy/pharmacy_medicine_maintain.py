# Medicine class
class Medicine:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # A function to format strings
    def __str__(self):
        return f"{self.name} - {self.quantity} - ${self.price:.2f}"


# Pharmacy class
class Pharmacy:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, name, price, quantity):
        # check if the medicine already exists
        for medicine in self.medicines:
            if medicine.name == name:
                medicine.quantity += quantity
                return

        # add a new medicine
        self.medicines.append(Medicine(name, price, quantity))

    def sell_medicine(self, name, quantity):
        # check if the medicine exists
        for medicine in self.medicines:
            if medicine.name == name:
                if medicine.quantity < quantity:
                    print(f"Not enough {name} in stock.")
                    return
                else:
                    medicine.quantity -= quantity
                    print(f"Sold {quantity} {name}.")
                    return

        # medicine not found
        print(f"{name} not found.")

    def print_stock(self):
        for medicine in self.medicines:
            print(medicine)


# example usage
pharmacy = Pharmacy()

pharmacy.add_medicine("Paracetamol", 4.2, 100)
pharmacy.add_medicine("Ibuprofen", 4.22, 50)

pharmacy.print_stock()

pharmacy.sell_medicine("Paracetamol", 8)
pharmacy.sell_medicine("Ibuprofen", 40)
pharmacy.sell_medicine("Aspirin", 2)

pharmacy.print_stock()
