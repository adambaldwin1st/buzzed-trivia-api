from enum import Enum


class QuestionType(Enum):
    # Open-ended question, write answer in text box
    FREE_RESPONSE = 'free response'
    # Multiple given options, can only pick one
    MULTIPLE_CHOICE = 'multiple choice'
    # Multiple given options, can pick multiple
    PICK_EM = 'pick_em'
    # Answer with two choices, usually True/False
    BINARY = 'binary'
