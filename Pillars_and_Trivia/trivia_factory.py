import random
import sqlite3
from Pillars_and_Trivia.trivia_question import TriviaQuestion


class TriviaFactory:
    def __init__(self, pillar):
        self.__conn = sqlite3.connect('Databases/dungeon_trivia.db')
        self.__pillar = pillar  # Pillar value triggered by pick-up
        self.__elapids_count = random.randint(1, 10)
        self.__astronomy_count = random.randint(1, 10)
        self.__pokemon_count = random.randint(1, 10)
        self.__international_count = random.randint(1, 10)

    def read_elapids_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM elapids_trivia WHERE rowid = "{num}"')
        return cursor.fetchone()
        # elapids_trivia = cursor.fetchone()
        # return elapids_trivia

    def read_astronomy_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM astronomy_trivia WHERE rowid = "{num}"')
        return cursor.fetchone()
        # astronomy_trivia = cursor.fetchone()
        # return astronomy_trivia

    def read_pokemon_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM pokemon_trivia WHERE rowid = "{num}"')
        pokemon_trivia = cursor.fetchone()
        return pokemon_trivia

    def read_international_table(self, num):
        cursor = self.__conn.cursor()
        cursor.execute(f'SELECT * FROM international_trivia WHERE rowid = "{num}"')
        return cursor.fetchone()

    def create_elapid_question(self, num):
        return self.read_elapids_table(num)


    def create_astronomy_question(self, num):
        return self.read_astronomy_table(num)
        # astronomy_question = self.read_astronomy_table(num)
        # return astronomy_question

    def create_pokemon_question(self, num):
        return self.read_pokemon_table(num)
        # pokemon_question = self.read_pokemon_table(num)
        # return pokemon_question

    def create_international_question(self, num):
        return self.read_international_table(num)


    def choose_question(self):
        # if elapids_count or astronomy_count or pokemon_count or international_count == 5:
        #     DungeonAdventure().current_menu = DungeonAdventure().game_over

        if self.__pillar.get_pillar_name() == 'Encapsulation':
            choice = self.create_elapid_question(self.__elapids_count)
            return choice

        elif self.__pillar.get_pillar_name() == 'Abstraction':
            choice = self.create_astronomy_question(self.__astronomy_count)
            return choice

        elif self.__pillar.get_pillar_name() == 'Polymorphism':
            choice = self.create_pokemon_question(self.__pokemon_count)
            return choice

        elif self.__pillar.get_pillar_name() == 'Inheritance':
            choice = self.create_international_question(self.__international_count)
            return choice

    def create_question(self):
        # chosen_question = self.choose_question()
        # print(chosen_question)
        return TriviaQuestion(*self.choose_question())

    def main(self):
        pass

    def get_pillar(self):
        return self.__pillar

    def set_pillar(self, pillar):
        self.__pillar = pillar

if __name__ == '__main__':
    u = TriviaFactory()
    trivia_question = u.create_question()

