import os
import json

from models import (Subject,
                    Topic,
                    Lesson,
                    InstructionActivity,
                    NumericalAnswerActivity,
                    TextAnswerActivity,
                    MultipleChoiceActivity)


class App:

    def __init__(self):
        self.subjects = []
        self.subjects = self.load_subjects()


    def create_activity(self, activity_json):
        activity_type = activity_json["type"]

        if activity_type not in ["instruction activity"]:
            print(f"Activity Type Not Found: {activity_type}")

        if activity_type == "instruction activity":
            return InstructionActivity(activity_json["text"])

    def load_subjects(self):
        with open("subjects.json") as json_file:
            course_data = json.load(json_file)

        subjects = []
        for subject_json in course_data["subjects"]:
            subject = Subject(subject_json["name"])
            for topic_json in subject_json["topics"]:
                topic = Topic(topic_json["name"])
                for lesson_json in topic_json["lessons"]:
                    lesson = Lesson(lesson_json["name"], topic_json["name"], subject_json["name"])
                    for activity_json in lesson_json["activities"]:
                        activity = self.create_activity(activity_json)
                        lesson.activities.append(activity)
                    topic.lessons.append(lesson)
                subject.topics.append(topic)
            subjects.append(subject)

        return subjects

    def run(self):
        os.system('clear')
        print()
        print("Adding and Subtracting Fractions (Same Denominator)")
        print("=========")
        print()

        current_lesson = self.subjects[0].topics[0].lessons[0]

        for activity in current_lesson.activities:
            print(activity.text)
            print()
            input("Press Enter To Continue...")




if __name__ == "__main__":
    app = App()
    app.run()
