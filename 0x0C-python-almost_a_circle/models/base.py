#!/usr/bin/python3
import json
import csv
import turtle


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
        id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
        list_dictionaries (list): A list of dictionaries.

        Returns:
        str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
        list_objs (list): A list of instances.

        Returns:
        None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by json_string.

        Args:
        json_string (str): A JSON string representing a list of dictionaries.

        Returns:
        list: List of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
        **dictionary: Double pointer to a dictionary.

        Returns:
        Base: Instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a file.

        Returns:
        list: List of instances loaded from file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                list_dicts = Base.from_json_string(json_data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list of instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                instances.append(obj)
            return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the rectangles and squares using Turtle graphics."""
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Drawing Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(0)

        # Function to draw a rectangle
        def draw_rectangle(x, y, width, height):
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.setheading(0)
            for _ in range(2):
                pen.forward(width)
                pen.left(90)
                pen.forward(height)
                pen.left(90)

        # Function to draw a square
        def draw_square(x, y, size):
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.setheading(0)
            for _ in range(4):
                pen.forward(size)
                pen.left(90)

        # Draw rectangles
        for rectangle in list_rectangles:
            draw_rectangle(rectangle.x, rectangle.y, rectangle.width, rectangle.height)

        # Draw squares
        for square in list_squares:
            draw_square(square.x, square.y, square.size)

        turtle.done()
