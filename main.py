from car import Car

backpack_items = ["laptop", 
                  "laptop charger",
                  "airpod",
                  "USB Type-C charger",
                  "journal",
                  "biro",
                  "keys",
                  "USB Type-B charger",
                  "mouse",
                  "umbrella",
                  ]

backpack = list(backpack_items)   
print("backpack contains:", backpack)

my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()

my_car.add_items_from_backpack(backpack)

my_car.remove_item_from_car("keys")
if "keys" in backpack:
    backpack.remove("keys")
print("Removed 'keys' from backpack.")
my_car.show_backseat()
print("Final backpack contents:", backpack)


