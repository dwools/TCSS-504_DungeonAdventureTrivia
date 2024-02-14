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

    sql = ''' INSERT OR REPLACE INTO heroes('hero', 'hit_points', 'attack_speed', 'chance_to_hit', 'minimum_damage', 'maximum_damage', 'chance_to_block', 'chance_to_heal', 'minimum_heal_points', 'maximum_heal_points', 'chance_for_bonus_damage', 'minimum_bonus_damage', 'maximum_bonus_damage', 'chance_for_second_attack')
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, hero)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"dungeon_heroes.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        priestess = ('Priestess', '75', '5', '0.7', '25', '45', '0.3', '0.7', '30', '60', '0', '0', '0', '0')

        knight = ('Knight', '125', '4', '0.8', '35', '60', '0.2', '0', '0', '0', '0.4', '40', '115', '0')

        rogue = ('Rogue', '75', '6', '0.8', '20', '40', '0.4', '0', '0', '0', '0', '0', '0', '0.4')

        create_hero(conn, priestess)
        create_hero(conn, knight)
        create_hero(conn, rogue)


if __name__ == '__main__':
    main()