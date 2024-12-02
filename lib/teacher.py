#!/usr/bin/env python

from user import User

import random



class Teacher(User):

    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = Teacher.knowledge  # copy the list to avoid modifying it in the teacher instance.  # This is to simulate sharing knowledge between different teacher instances.  # In a real-world application, you would want to use a database or a shared resource to store and share knowledge.  # In this example, knowledge is stored in a class variable for simplicity.  # In a real-world application, you would use a database or a shared resource to store and

    def teach(self):
        return random.choice(self.knowledge)