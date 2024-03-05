import random
import sqlite3
from trivia_question import TriviaQuestion


class TriviaFactory:
    def __init__(self):
        self.__conn = sqlite3.connect('dungeon_trivia.db')
        self.pillar = 'Encapsulation'  # Pillar value triggered by pick-up
        self.elapids_count = random.randint(1, 10)
        self.astronomy_count = random.randint(1, 10)
        self.pokemon_count = random.randint(1, 10)
        self.international_count = random.randint(1, 10)

    def read_elapids_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM elapids_trivia WHERE rowid = "{num}"')
        elapids_trivia = cursor.fetchone()
        return elapids_trivia

    def read_astronomy_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM astronomy_trivia WHERE rowid = "{num}"')
        astronomy_trivia = cursor.fetchone()
        return astronomy_trivia

    def read_pokemon_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM pokemon_trivia WHERE rowid = "{num}"')
        pokemon_trivia = cursor.fetchone()
        return pokemon_trivia

    def read_international_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM international_trivia WHERE rowid = "{num}"')
        international_trivia = cursor.fetchone()
        return international_trivia

    def create_elapid_question(self, num):
        elapids_question = self.read_elapids_table(num)
        return elapids_question

    def create_astronomy_question(self, num):
        astronomy_question = self.read_astronomy_table(num)
        return astronomy_question

    def create_pokemon_question(self, num):
        pokemon_question = self.read_pokemon_table(num)
        return pokemon_question

    def create_international_question(self, num):
        international_question = self.read_international_table(num)
        return international_question

    def choose_question(self):
        # if elapids_count or astronomy_count or pokemon_count or international_count == 5:
        #     DungeonAdventure().current_menu = DungeonAdventure().game_over

        if self.pillar == 'Encapsulation':
            choice = self.create_elapid_question(self.elapids_count)
            return choice

        if self.pillar == 'Abstraction':
            choice = self.create_astronomy_question(self.astronomy_count)
            return choice

        if self.pillar == 'Polymorphism':
            choice = self.create_pokemon_question(self.pokemon_count)
            return choice

        if self.pillar == 'Inheritance':
            choice = self.create_international_question(self.international_count)
            return choice

    def create_question(self):
        chosen_question = self.choose_question()
        print(chosen_question)
        return TriviaQuestion(*chosen_question)

    def main(self):
        pass


if __name__ == '__main__':
    u = TriviaFactory()
    trivia_question = u.create_question()

