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

    sql = ''' INSERT OR REPLACE INTO pokemon_trivia(question, answer)
              VALUES(?,?) '''
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

    sql = ''' INSERT OR REPLACE INTO international_trivia(question, answer)
              VALUES(?,?) '''
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

    sql = ''' INSERT OR REPLACE INTO astronomy_trivia(question, answer)
              VALUES(?,?) '''
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

    sql = ''' INSERT OR REPLACE INTO elapids_trivia(question, answer)
              VALUES(?,?) '''
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
        pokemon_trivia_1 = ('Togepi is known for stealing children.', 'FALSE')
        pokemon_trivia_2 = ('GameFreak has modeled a Pokemon game region after South America.', 'FALSE')
        pokemon_trivia_3 = ('The three types of starter pokemon are: Ice Type, Poison Type, and Fire Type.', 'FALSE')
        pokemon_trivia_4 = ('Mew can be found living under a yellow truck in the original Red and Blue games.', 'FALSE')
        pokemon_trivia_5 = ('Pikachu is an Electric Type Pokemon.', 'TRUE')
        pokemon_trivia_6 = ('Jerrifet is a Poison and Ice Type Pokemon.', 'FALSE')
        pokemon_trivia_7 = ('The most recent Pokemon generation was based on the Iberian Peninsula.', 'TRUE')
        pokemon_trivia_8 = ('All Pokemon Evolve.', 'FALSE')
        pokemon_trivia_9 = ('Ash Ketchum started his Pokemon journey in Viridian City.', 'FALSE')
        pokemon_trivia_10 = ('Mareep is Jackson\'s favorite Pokemon.', "TRUE")
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

        international_trivia_1 = ('There are 8 continents.', 'FALSE')
        international_trivia_2 = ('Mount Everest is the highest mountain in the world.', 'TRUE')
        international_trivia_3 = ('Every country in the world has a rectangular flag.', 'FALSE')
        international_trivia_4 = ('Florida is the southernmost state in the US.', 'FALSE')
        international_trivia_5 = ('It snows in Hawaii.', 'TRUE')
        international_trivia_6 = ('The highest mountain in the US is in Colorado.', 'FALSE')
        international_trivia_7 = ('Switzerland is landlocked.', 'TRUE')
        international_trivia_8 = ('Sydney is the capital of Australia.', 'FALSE')
        international_trivia_9 = ('New Zealand has more sheep than people.', 'TRUE')
        international_trivia_10 = ('The flag of Canada has a maple leaf on it.', 'TRUE')
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

        astronomy_trivia_1 = ('Neptune is sideways, with an axial tilt 82.23 degrees.', 'FALSE')
        astronomy_trivia_2 = ('There are more possible moves in a game of chess then there are atoms in the universe.', 'TRUE')
        astronomy_trivia_3 = ('Jupiter\'s largest moon, Ganymede, is larger than the planet Mercury.', 'TRUE')
        astronomy_trivia_4 = ('At the end of its life, the Sun will collapse into a black hole.', 'FALSE')
        astronomy_trivia_5 = ('There are more trees on earth than there are stars in the Milky Way.', 'TRUE')
        astronomy_trivia_6 = ('Venus is the brightest celestial object in the sky.', 'FALSE')
        astronomy_trivia_7 = ('The diameter of a neutron star is about the length of Manhattan Island.', 'TRUE')
        astronomy_trivia_8 = ('Like the Sun, Jupiter is mostly composed of hydrogen and helium.', 'TRUE')
        astronomy_trivia_9 = ('High-mass stars will continue fusing lighter elements into heavier elements (hydrogen into helium, helium into carbon) up until lead (Pb), when the star implodes and rebounds in a supernova.', 'FALSE')
        astronomy_trivia_10 = ('The lower the mass of a star, the longer it lives.', 'TRUE')
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

        elapids_trivia_1 = ('The king cobra, the longest venomous snake and largest elapid in the world, in addition to envenomation, will also constrict small prey.', 'FALSE')
        elapids_trivia_2 = ('The black mamba causes the most human fatalities per year out of any snake species.', 'FALSE')
        elapids_trivia_3 = ('The inland taipan, the most venomous snake in the world by venom toxicity, is native to Africa.', 'FALSE')
        elapids_trivia_4 = ('Most elapids predominantly produce a neurotoxic venom, as compared to vipers which produce a predominantly hemotoxic venom.', 'TRUE')
        elapids_trivia_5 = ('Of the four recognized extant mamba species - the black mamba, the western green mamba, the eastern green mamba, and the Jameson\'s mamba - three are arboreal (tree dwelling).', 'TRUE')
        elapids_trivia_6 = ('Elapids have proteroplyphous fangs, which are fixed, perpendicular to the jaw, and smaller than the solenoglyphous fangs (which are three times larger and hinged to fold parallel to the jaw when closed) found in vipers.', 'TRUE')
        elapids_trivia_7 = ('Turtle-headed sea snakes, due to a specialized diet of fish eggs, have only vestigial (small remnants of a once more significant characteristic) fangs and do not produce venom.', 'TRUE')
        elapids_trivia_8 = ('All species of the genus Naja (true cobras) can spray jets of venom through modified, forward-facing holes in their fangs.', 'FALSE')
        elapids_trivia_9 = ('Western green mambas are sexually dimorphic; females are usually a drab olive brown, and males are vibrant green with blue or black scale edges. ', 'FALSE')
        elapids_trivia_10 = ('The yellow-lipped sea krait (also known as the banded sea krait) is the second most venomous snake in the world by venom toxicity.', 'FALSE')
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
