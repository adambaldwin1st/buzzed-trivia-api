class Question:

    # Constructor
    def __init__(self, title, answer, points_possible, question_type, options=None, media=None):
        # Instance Attributes
        self.title = title
        self.answer = answer
        self.points_possible = points_possible
        self.question_type = question_type
        self.options = options if options is not None else []
        self.media = media if media is not None else []

    def __str__(self):
        return f"Title: {self.title}\nQuestion Type: {self.question_type}\n" \
               f"Options: {self.options}\nAnswer: {self.answer}\nMedia: {self.media}"
