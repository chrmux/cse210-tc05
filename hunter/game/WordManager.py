import random
class WordManager:
    def __init__(self, list):
        self.list = list
        self.current_value = self.random_word()
    def random_word(self):
        value = random.choice(self.list)
        return value
    def get_word(self):
        return self.current_value

