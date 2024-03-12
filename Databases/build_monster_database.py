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


def create_monster(conn, monster):
    """
    Create a new task
    :param conn:
    :param monster:
    :return:
    """

    sql = ''' INSERT OR REPLACE INTO monsters(monster, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_heal, minimum_heal_points, maximum_heal_points)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, monster)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"Databases/dungeon_monsters.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        ogre = ('Ogre', '200', '2', '0.6', '30', '60', '0.1', '30', '60')
        gremlin = ('Gremlin', '70', '5', '0.8', '15', '30', '0.4', '20', '40')
        skeleton = ('Skeleton', '100', '3', '0.8', '30', '50', '0.3', '30', '50')
        create_monster(conn, ogre)
        create_monster(conn, gremlin)
        create_monster(conn, skeleton)


if __name__ == '__main__':
    main()
