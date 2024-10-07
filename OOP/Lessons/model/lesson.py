class Lesson:
    def __init__(self, title, topic, instructor, duration):
        self._title = title
        self._topic = topic
        self._instructor = instructor
        self._duration = duration

    def get_description(self):
        return f"Lesson: {self._title} (Topic: {self._topic}, Duration: {self._duration} hours), Instructor: {self._instructor}"

    def get_topic(self):
        return self._topic

    def get_instructor(self):
        return self._instructor.get_name()
