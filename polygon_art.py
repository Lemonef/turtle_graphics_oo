import turtle
import random

class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
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
    def __init__(self, num_sides, size, orientation, location, color, border_size, reduction_ratio, num_levels):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.reduction_ratio = reduction_ratio
        self.num_levels = num_levels

    def draw(self):
        current_size = self.size
        current_location = self.location
        
        for _ in range(self.num_levels):
            super().draw()
            current_size *= self.reduction_ratio
            self.move_to_next_position(current_size)

    def move_to_next_position(self, size):
        turtle.penup()
        turtle.forward(size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location = turtle.pos()


class PolygonArt:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        turtle.speed(0)
        turtle.tracer(0)
        turtle.colormode(255)

    def run(self):
        # Get user's choice
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9: "))
        turtle.clear()

        # Generate art based on the choice
        if choice == 1:
            self.draw_random_polygons(3, 20, 40)
        elif choice == 2:
            self.draw_random_polygons(4, 30, 50)
        elif choice == 3:
            self.draw_random_polygons(5, 20, 60)
        elif choice == 4:
            self.draw_random_polygons(6, 30, 80)
        elif choice == 5:
            self.draw_random_polygons(3, 10, 30)
        elif choice == 6:
            self.draw_embedded_polygons(4, 50, 5, 0.8)
        elif choice == 7:
            self.draw_embedded_polygons(5, 60, 6, 0.7)
        elif choice == 8:
            self.draw_embedded_polygons(6, 70, 7, 0.6)
        elif choice == 9:
            self.draw_embedded_polygons(3, 80, 8, 0.5)

        turtle.update()
        turtle.done()

    def draw_random_polygons(self, num_sides, min_size, max_size):
        for _ in range(15):
            size = random.randint(min_size, max_size)
            orientation = random.randint(0, 360)
            location = (random.randint(-200, 200), random.randint(-200, 200))
            color = self.get_new_color()
            border_size = random.randint(1, 5)
            
            polygon = Polygon(num_sides, size, orientation, location, color, border_size)
            polygon.draw()

    def draw_embedded_polygons(self, num_sides, size, num_levels, reduction_ratio):
        for _ in range(10):
            orientation = random.randint(0, 360)
            location = (random.randint(-200, 200), random.randint(-200, 200))
            color = self.get_new_color()
            border_size = random.randint(1, 5)
            
            embedded_polygon = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, reduction_ratio, num_levels)
            embedded_polygon.draw()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Run the program
if __name__ == "__main__":
    art = PolygonArt()
    art.run()
