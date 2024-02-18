

class TriviaQuestion:

    def __init__(self, question, answer):
        self.__question = question
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_answer(self):
        return self.__answer


if __name__ == "__main__":
    q = TriviaQuestion
    q.get_question(1)


