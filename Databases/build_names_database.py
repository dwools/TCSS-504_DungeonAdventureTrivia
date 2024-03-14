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

def create_monster_name(conn, names):
    """
       Create a new task
       :param conn:
       :param names:
       :return:
       """

    sql = ''' INSERT OR REPLACE INTO names(id, common_name, latin_name)
              VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, names)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"Databases/database_names.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        death_adder = ('1', 'Death adder', 'Acanthophis antarcticus')
        pigmy_copperhead = ('2', 'Pigmy copperhead', 'Austrelaps labialis')
        highlands_copperhead = ('3', 'Highlands copperhead', 'Austrelaps ramsayi')
        lowlands_copperhead = ('4', 'Lowlands copperhead', 'Austrelaps superbus')
        eastern_green_mamba = ('5', 'Eastern green mamba', 'Dendroaspis angusticeps')
        jamesons_mamba = ('6', "Jameson's mamba", 'Dendroaspis jamesoni')
        black_mamba = ('7', 'Black mamba', 'Dendroaspis polylepis')
        western_green_mamba = ('8', 'Western green mamba', 'Dendroaspis viridis')
        yellow_lipped_sea_krait = ('9', 'Yellow-lipped sea krait', 'Laticauda colubrina')
        eastern_coral_snake = ('10', 'Eastern coral snake', 'Micrurus fulvius')
        egyptian_cobra = ('11', 'Egyptian cobra', 'Naja haje')
        indian_cobra = ('12', 'Indian cobra', 'Naja naja')
        black_necked_spitting_cobra = ('13', 'Black-necked spitting cobra', 'Naja nigricollis')
        caspian_cobra = ('14', 'Caspian cobra', 'Naja oxiana')
        red_spitting_cobra = ('15', 'Red spitting cobra', 'Naja pallida')
        tiger_snake = ('16', 'Tiger snake', 'Notechis scutatus')
        king_cobra = ('17', 'King cobra', 'Ophiophagus hannah')
        inland_taipan = ('18', 'Inland taipan', 'Oxyuranus microlepidotus')
        coastal_taipan = ('19', 'Coastal taipan', 'Oxyuranus scutellatus')
        king_brown = ('20', 'King brown', 'Pseudechis australis')
        colletts_black_snake = ('21', "Collett's black snake", 'Pseudechis colleti')
        red_bellied_black_snake = ('22', 'Red-bellied black snake', 'Pseudechis porphryiacus')
        western_brown_snake = ('23', 'Western brown snake', 'Pseudonaja nuchalis')
        eastern_brown_snake = ('24', 'Eastern brown snake', 'Pseudonaja textilis')
        create_monster_name(conn, death_adder)
        create_monster_name(conn, pigmy_copperhead)
        create_monster_name(conn, highlands_copperhead)
        create_monster_name(conn, lowlands_copperhead)
        create_monster_name(conn, eastern_green_mamba)
        create_monster_name(conn, jamesons_mamba)
        create_monster_name(conn, black_mamba)
        create_monster_name(conn, western_green_mamba)
        create_monster_name(conn, yellow_lipped_sea_krait)
        create_monster_name(conn, eastern_coral_snake)
        create_monster_name(conn, egyptian_cobra)
        create_monster_name(conn, indian_cobra)
        create_monster_name(conn, black_necked_spitting_cobra)
        create_monster_name(conn, caspian_cobra)
        create_monster_name(conn, red_spitting_cobra)
        create_monster_name(conn, tiger_snake)
        create_monster_name(conn, king_cobra)
        create_monster_name(conn, inland_taipan)
        create_monster_name(conn, coastal_taipan)
        create_monster_name(conn, king_brown)
        create_monster_name(conn, colletts_black_snake)
        create_monster_name(conn, red_bellied_black_snake)
        create_monster_name(conn, western_brown_snake)
        create_monster_name(conn, eastern_brown_snake)

    if __name__ == '__main__':
        main()







