class Question:

    # Class attributes

    # Constructor
    def __init__(self, title, answer, question_type, media=None):
        # Instance Attributes
        self.title = title
        self.answer = answer
        self.question_type = question_type
        self.media = media if media is not None else []

