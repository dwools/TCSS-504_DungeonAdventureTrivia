import sqlite3
from sqlite3 import Error


# run me second
# from https://www.sqlitetutorial.net/sqlite-python/

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_pokemon_trivia(conn, trivia):
    """
    Create a new pokemon trivia question
    :param conn:
    :param trivia:
    :return:
    """

    sql = ''' INSERT OR REPLACE INTO pokemon_trivia(id, question, answer)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, trivia)
    conn.commit()
    return cur.lastrowid


def create_international_trivia(conn, trivia):
    """
    Create a new international trivia question
    :param conn:
    :param trivia:
    :return:
    """

    sql = ''' INSERT OR REPLACE INTO international_trivia(id, question, answer)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, trivia)
    conn.commit()
    return cur.lastrowid


def create_astronomy_trivia(conn, trivia):
    """
    Create a new astronomy trivia question
    :param conn:
    :param trivia:
    :return:
    """

    sql = ''' INSERT OR REPLACE INTO astronomy_trivia(id, question, answer)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, trivia)
    conn.commit()
    return cur.lastrowid


def create_elapids_trivia(conn, trivia):
    """
    Create a new task
    :param conn:
    :param trivia:
    :return:
    """

    sql = ''' INSERT OR REPLACE INTO elapids_trivia(id, question, answer)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, trivia)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"dungeon_trivia.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        pokemon_trivia_1 = ('1', 'Togepi is known for stealing children', 'FALSE')
        pokemon_trivia_2 = ('2', 'GameFreak has modeled a Pokemon game region after South America', 'FALSE')
        pokemon_trivia_3 = ('3', 'The three types of starter pokemon are: Ice Type, Poison Type, and Fire Type', 'FALSE')
        pokemon_trivia_4 = ('4', 'Mew can be found living under a yellow truck in the original Red and Blue games', 'FALSE')
        pokemon_trivia_5 = ('5', 'Pikachu is an Electric Type Pokemon', 'TRUE')
        pokemon_trivia_6 = ('6', 'Jerrifet is a Poison and Ice Type Pokemon', 'FALSE')
        pokemon_trivia_7 = ('7', 'The most recent Pokemon generation was based on the Iberian Peninsula', 'TRUE')
        pokemon_trivia_8 = ('8', 'All Pokemon Evolve', 'FALSE')
        pokemon_trivia_9 = ('9', 'Ash Ketchum started his Pokemon journey in Viridian City', 'FALSE')
        pokemon_trivia_10 = ('10', 'Mareep is Jackson\'s favorite Pokemon', "TRUE")
        create_pokemon_trivia(conn, pokemon_trivia_1)
        create_pokemon_trivia(conn, pokemon_trivia_2)
        create_pokemon_trivia(conn, pokemon_trivia_3)
        create_pokemon_trivia(conn, pokemon_trivia_4)
        create_pokemon_trivia(conn, pokemon_trivia_5)
        create_pokemon_trivia(conn, pokemon_trivia_6)
        create_pokemon_trivia(conn, pokemon_trivia_7)
        create_pokemon_trivia(conn, pokemon_trivia_8)
        create_pokemon_trivia(conn, pokemon_trivia_9)
        create_pokemon_trivia(conn, pokemon_trivia_10)

        international_trivia_1 = ('1', 'There are 8 continents', 'FALSE')
        international_trivia_2 = ('2', 'Mount Everest is the highest mountain in the world', 'TRUE')
        international_trivia_3 = ('3', 'Every country in the world has a rectangular flag', 'FALSE')
        international_trivia_4 = ('4', 'Florida is the southernmost state in the US', 'FALSE')
        international_trivia_5 = ('5', 'It snows in Hawaii', 'TRUE')
        international_trivia_6 = ('6', 'The highest mountain in the US is in Colorado', 'FALSE')
        international_trivia_7 = ('7', 'Switzerland is landlocked', 'TRUE')
        international_trivia_8 = ('8', 'Sydney is the capital of Australia', 'False')
        international_trivia_9 = ('9', 'New Zealand has more sheep than people', 'TRUE')
        international_trivia_10 = ('10', 'The flag of Canada has a maple leaf on it', 'TRUE')
        create_international_trivia(conn, international_trivia_1)
        create_international_trivia(conn, international_trivia_2)
        create_international_trivia(conn, international_trivia_3)
        create_international_trivia(conn, international_trivia_4)
        create_international_trivia(conn, international_trivia_5)
        create_international_trivia(conn, international_trivia_6)
        create_international_trivia(conn, international_trivia_7)
        create_international_trivia(conn, international_trivia_8)
        create_international_trivia(conn, international_trivia_9)
        create_international_trivia(conn, international_trivia_10)

        astronomy_trivia_1 = ('1', 'There are 8 continents', 'FALSE')
        astronomy_trivia_2 = ('2', 'Mount Everest is the highest mountain in the world', 'TRUE')
        astronomy_trivia_3 = ('3', 'Every country in the world has a rectangular flag', 'FALSE')
        astronomy_trivia_4 = ('4', 'Florida is the southernmost state in the US', 'FALSE')
        astronomy_trivia_5 = ('5', 'It snows in Hawaii', 'TRUE')
        astronomy_trivia_6 = ('6', 'The highest mountain in the US is in Colorado', 'FALSE')
        astronomy_trivia_7 = ('7', 'Switzerland is landlocked', 'TRUE')
        astronomy_trivia_8 = ('8', 'Sydney is the capital of Australia', 'False')
        astronomy_trivia_9 = ('9', 'New Zealand has more sheep than people', 'TRUE')
        astronomy_trivia_10 = ('10', 'The flag of Canada has a maple leaf on it', 'TRUE')
        create_astronomy_trivia(conn, astronomy_trivia_1)
        create_astronomy_trivia(conn, astronomy_trivia_2)
        create_astronomy_trivia(conn, astronomy_trivia_3)
        create_astronomy_trivia(conn, astronomy_trivia_4)
        create_astronomy_trivia(conn, astronomy_trivia_5)
        create_astronomy_trivia(conn, astronomy_trivia_6)
        create_astronomy_trivia(conn, astronomy_trivia_7)
        create_astronomy_trivia(conn, astronomy_trivia_8)
        create_astronomy_trivia(conn, astronomy_trivia_9)
        create_astronomy_trivia(conn, astronomy_trivia_10)

        elapids_trivia_1 = ('1', 'There are 8 continents', 'FALSE')
        elapids_trivia_2 = ('2', 'Mount Everest is the highest mountain in the world', 'TRUE')
        elapids_trivia_3 = ('3', 'Every country in the world has a rectangular flag', 'FALSE')
        elapids_trivia_4 = ('4', 'Florida is the southernmost state in the US', 'FALSE')
        elapids_trivia_5 = ('5', 'It snows in Hawaii', 'TRUE')
        elapids_trivia_6 = ('6', 'The highest mountain in the US is in Colorado', 'FALSE')
        elapids_trivia_7 = ('7', 'Switzerland is landlocked', 'TRUE')
        elapids_trivia_8 = ('8', 'Sydney is the capital of Australia', 'False')
        elapids_trivia_9 = ('9', 'New Zealand has more sheep than people', 'TRUE')
        elapids_trivia_10 = ('10', 'The flag of Canada has a maple leaf on it', 'TRUE')
        create_elapids_trivia(conn, elapids_trivia_1)
        create_elapids_trivia(conn, elapids_trivia_2)
        create_elapids_trivia(conn, elapids_trivia_3)
        create_elapids_trivia(conn, elapids_trivia_4)
        create_elapids_trivia(conn, elapids_trivia_5)
        create_elapids_trivia(conn, elapids_trivia_6)
        create_elapids_trivia(conn, elapids_trivia_7)
        create_elapids_trivia(conn, elapids_trivia_8)
        create_elapids_trivia(conn, elapids_trivia_9)
        create_elapids_trivia(conn, elapids_trivia_10)



if __name__ == '__main__':
    main()
