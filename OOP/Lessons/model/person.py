# Importing necessary libraries
import re
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, id_number):
        # Check if name contains only letters (no numbers or special characters allowed)
        if not re.match("^[A-Za-z ]+$", name):
            raise ValueError("Name must contain only letters and spaces.")
        self._name = name
        self._id_number = id_number

    @abstractmethod
    def get_description(self):
        pass

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

class Student(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._subscriptions = []

    def get_description(self):
        return f"Student: {self.get_name()} (ID: {self.get_id_number()})"

    def subscribe_to_lesson(self, lesson):
        self._subscriptions.append(lesson)

    def get_subscriptions(self):
        return self._subscriptions

class Instructor(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._lessons = []

    def get_description(self):
        return f"Instructor: {self.get_name()} (ID: {self.get_id_number()})"

    def add_lesson(self, lesson):
        self._lessons.append(lesson)

    def get_lessons(self):
        return self._lessons

    # Check if the instructor teaches a specific lesson topic.
    def teaches_lesson(self, topic):
        for lesson in self._lessons:
            if lesson.get_topic() == topic:
                return lesson
        return None
