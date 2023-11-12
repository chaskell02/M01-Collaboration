class Vehicle:
  def __init__(self, vehicle_type):
      self.vehicle_type = vehicle_type

class Automobile(Vehicle):
  def __init__(self, vehicle_type, year, make, model, doors, roof):
      super().__init__(vehicle_type)
      self.year = year
      self.make = make
      self.model = model
      self.doors = doors
      self.roof = roof

  def display_info(self):
      print("Vehicle type:", self.vehicle_type)
      print("Year:", self.year)
      print("Make:", self.make)
      print("Model:", self.model)
      print("Number of doors:", self.doors)
      print("Type of roof:", self.roof)


def main():
  # Accept user input for car details
  vehicle_type = "car"  # Default type for this example
  year = input("Enter the year of the car: ")
  make = input("Enter the make of the car: ")
  model = input("Enter the model of the car: ")
  doors = input("Enter the number of doors (2 or 4): ")
  roof = input("Enter the type of roof (solid or sun roof): ")

  # Create an instance of the Automobile class
  car = Automobile(vehicle_type, year, make, model, doors, roof)

  # Display the car information
  print("\nCar Information:")
  car.display_info()


if __name__ == "__main__":
  main()
