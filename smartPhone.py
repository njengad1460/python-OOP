class SmartPhone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def take_photo(self):
        print("Taking a photo...")

    def browse_internet(self):
        print("Browsing the internet...")