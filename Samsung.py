from smartPhone import SmartPhone
class Samsung(SmartPhone):
    def __init__(self, model, price, screen_size, battery_capacity):
        super().__init__("Samsung", model, price)
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Battery Capacity: {self.battery_capacity} mAh")