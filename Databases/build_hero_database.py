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


def create_hero(conn, hero):
    """
    Create a new task
    :param conn: Connection object
    :param hero: CREATE HERO statement
    :return:
    """

    sql = ''' INSERT OR REPLACE INTO heroes('hero', 'hit_points', 'attack_speed', 'chance_to_hit', 'minimum_damage', 'maximum_damage', 'chance_to_block')
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, hero)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"Databases/database_heroes.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        priestess = ('Priestess', '75', '5', '70', '25', '45', '30')

        knight = ('Knight', '125', '4', '80', '35', '60', '20')

        rogue = ('Rogue', '75', '6', '80', '20', '40', '40')

        create_hero(conn, priestess)
        create_hero(conn, knight)
        create_hero(conn, rogue)


if __name__ == '__main__':
    main()
