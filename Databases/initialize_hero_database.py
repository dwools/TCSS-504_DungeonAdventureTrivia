import sqlite3
from sqlite3 import Error


# run me first
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
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"Databases/dungeon_heroes.db"

    sql_create_heroes_table = """ CREATE TABLE IF NOT EXISTS heroes (
                                    hero text PRIMARY KEY,
                                    hit_points integer,
                                    attack_speed integer,
                                    chance_to_hit float,
                                    minimum_damage integer,
                                    maximum_damage integer,
                                    chance_to_block float
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create dungeon monsters table
        create_table(conn, sql_create_heroes_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()