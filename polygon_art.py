import turtle
import random

class Polygon:
    def __init__(self, num_sides=0, size=0, orientation=0, location=None, color=None, border_size=0) -> None:
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        current_size = self.size
        current_location = self.location
        for _ in range(self.num_levels):
            super().draw()
            current_size *= self.reduction_ratio
            turtle.penup()
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
            turtle.right(90)
            current_location = [turtle.xcor(), turtle.ycor()]
            self.size = current_size
            self.location = current_location

class PolygonArt:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def run(self, choice):
        for _ in range(random.randint(20,30)):
            if choice == 1:
                num_sides = 3
            elif choice == 2:
                num_sides = 4
            elif choice == 3:
                num_sides = 5
            elif choice == 4:
                num_sides = random.choice([3, 4, 5])
            elif choice == 5:
                num_sides = 3 
            elif choice == 6:
                num_sides = 4  
            elif choice == 7:
                num_sides = 5 
            else:
                num_sides = random.randint(3, 5)

            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            if choice in [5, 6, 7, 8]:
                num_levels = 3 
            elif choice == 9:
                num_levels = random.randint(1, 3)
            else:
                num_levels = 1

            reduction_ratio = 0.618

            if choice in [5, 6, 7, 8, 9]:
                polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
            else:
                polygon = Polygon(num_sides, size, orientation, location, color, border_size)

            polygon.draw()

        turtle.update()
        turtle.done()


art = PolygonArt()
choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

if 1 <= choice <= 9:
    art.run(choice)
else:
    print("Invalid choice. Please enter a number between 1 and 9.")
