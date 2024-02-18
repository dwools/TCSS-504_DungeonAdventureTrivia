

class TriviaQuestion:

    def __init__(self, question, answer):
        self.__question = question
        self.__answer = answer

    def get_question(self):
        return f'{self.__question}'

    def get_answer(self):
        return self.__answer
