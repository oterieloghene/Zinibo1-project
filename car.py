#car.py

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.backseat = []
        
    def display_info(self):
        print (f"{self.year} {self.brand} {self.model}")
        
    def add_items_from_backpack(self, backpack):
        self.backseat.extend(backpack)
        print("items added to car:", self.backseat)
        
    def remove_item_from_car(self, item):
        if item in self.backseat:
            self.backseat.remove(item)
            print(f"Removed '{item}' from car.")
        else:
            print(f"'{item}' not found in car.")
            
    def show_backseat(self):
        print("Car backseat contains:", self.backseat)