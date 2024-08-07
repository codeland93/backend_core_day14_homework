class Vehicle:
    def __init__(self, registration_number, vehicle_type, owner):
        self.registration_number = registration_number
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to: {self.owner}")

# Demonstration script
if __name__ == "__main__":
    # Creating Vehicle objects
    Honda = Vehicle("ABC123","Honda Civic", "Alice")
    Lexus = Vehicle("XYZ789", "Lexus RX", "Bob")
    BMW = Vehicle("LMN456", "BMW 5 Series", "Charlie")
    Audi = Vehicle("BMG789", "Audi A5", "Eric")

    # Displaying initial owners
    print(f"Honda Civic: Registration Number: {Honda.registration_number}, Type: {Honda.type}, Owner: {Honda.owner}")
    print(f"Lexus RX: Registration Number: {Lexus.registration_number}, Type: {Lexus.type}, Owner: {Lexus.owner}")
    print(f"BMW 5 Series: Registration Number: {BMW.registration_number}, Type: {BMW.type}, Owner: {BMW.owner}")
    print(f"Audi A5: Registration Number: {Audi.registration_number}, Type: {Audi.type}, Owner: {Audi.owner}")

    # Updating the owners
    Honda.update_owner("Dave")
    Lexus.update_owner("Eve")
    BMW.update_owner("Frank")
    Audi.update_owner("George")

    # Displaying updated owners
    print(f"Honda Civic: Registration Number: {Honda.registration_number}, Type: {Honda.type}, Owner: {Honda.owner}")
    print(f"Lexus RX: Registration Number: {Lexus.registration_number}, Type: {Lexus.type}, Owner: {Lexus.owner}")
    print(f"BMW 5 Series: Registration Number: {BMW.registration_number}, Type: {BMW.type}, Owner: {BMW.owner}")
    print(f"Audi A5: Registration Number: {Audi.registration_number}, Type: {Audi.type}, Owner: {Audi.owner}")
