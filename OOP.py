class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}"


class Ebook(Book):
    def __init__(self, title, author, genre, file_size):
        super().__init__(title, author, genre)  # Call the constructor of the base class
        self.file_size = file_size  # In MB

    def display_info(self):
        info = super().display_info()  # Get info from the Book class
        return f"{info}\nFile Size: {self.file_size} MB"


#  instances of Book and Ebook
print("### Book Information ###")
book1 = Book("1984", "George Orwell", "Dystopian")
print(book1.display_info())

print("\n### Ebook Information ###")
ebook1 = Ebook("Digital Fortress", "Dan Brown", "Thriller", 1.5)
print(ebook1.display_info())

# activity 2
class Car:
    def move(self):
        return "Driving 🚗"


class Plane:
    def move(self):
        return "Flying ✈️"


class Bicycle:
    def move(self):
        return "Pedaling 🚲"


# Function to demonstrate polymorphism
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(vehicle.move())


# Create instances of the vehicles
car = Car()
plane = Plane()
bicycle = Bicycle()

# Create a list of vehicles to demonstrate polymorphism
vehicles = [car, plane, bicycle]
print("### Vehicles Movement ###")
demonstrate_movement(vehicles)