from Databases import initialize_hero_database
from Databases import initialize_monster_database
from Databases import initialize_trivia_database
from Databases import initialize_monstername_database

from Databases import build_hero_database
from Databases import build_monster_database
from Databases import build_trivia_database
from Databases import build_monstername_database


def main():
    initialize_monster_database.main()
    build_monster_database.main()

    initialize_trivia_database.main()
    build_trivia_database.main()

    initialize_hero_database.main()
    build_hero_database.main()

    initialize_monstername_database.main()
    build_monstername_database.main()


if __name__ == '__main__':
    main()
