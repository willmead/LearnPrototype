class Activity:
    pass


class InstructionActivity(Activity):

    def __init__(self, text):
        self.text = text

class MultipleChoiceActivity(Activity):
    pass


class NumericalAnswerActivity(Activity):
    pass


class TextAnswerActivity(Activity):
    pass


class Lesson:

    def __init__(self, name, topic, subject):
        self.name = name
        self.topic = topic
        self.subject = subject
        self.activities = []


class Topic:

    def __init__(self, name):
        self.name = name
        self.lessons = []


class Subject:

    def __init__(self, name):
        self.name = name
        self.topics = []
