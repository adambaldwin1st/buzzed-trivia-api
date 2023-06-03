from enum import Enum


class QuestionType(Enum):
    FREE_RESPONSE = 1
    MULTIPLE_CHOICE = 2
    LIST = 3
    TRUE_FALSE = 4


class Question:
    def __init__(self, text, type):
        self.text = text
        self.type = type
