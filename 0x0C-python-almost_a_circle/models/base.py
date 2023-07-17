#!/usr/bin/python3
"""Defines the Base class for the project"""
import turtle
import json
import csv
import os


class Base:
    """Base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance

        Args:
            id (int): The id of the new Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            json_string = f.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                writer = csv.writer(f)
                if cls.__name__ == "Rectangle":
                    writer.writerow(["id", "width", "height", "x", "y"])
                    for obj in list_objs:
                        writer.writerow(
                                [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow(["id", "size", "x", "y"])
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            if cls.__name__ == "Rectangle":
                attrs = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                attrs = ["id", "size", "x", "y"]
            objs = []
            for row in reader:
                d = {}
                for i, attr in enumerate(attrs):
                    d[attr] = int(row[i])
                objs.append(cls.create(**d))
            return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Create a screen"""
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        """Create a turtle object"""
        pen = turtle.Turtle()
        pen.speed(10)

        """Draw rectangles"""
        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("red")
            for i in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        """Draw squares"""
        for sq in list_squares:
            pen.penup()
            pen.goto(sq.x, sq.y)
            pen.pendown()
            pen.color("blue")
            for i in range(4):
                pen.forward(sq.size)
                pen.left(90)

        """Keep the window open"""
        turtle.mainloop()
