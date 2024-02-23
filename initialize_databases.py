import initialize_hero_database
import initialize_monster_database
import initialize_trivia_database
import initialize_monstername_database

import build_hero_database
import build_monster_database
import build_trivia_database
import build_monstername_database

def main():
    initialize_monster_database.main()
    initialize_trivia_database.main()
    initialize_hero_database.main()
    initialize_monstername_database.main()

    build_monster_database.main()
    build_trivia_database.main()
    build_hero_database.main()
    build_monstername_database.main()


if __name__ == '__main__':
    main()
