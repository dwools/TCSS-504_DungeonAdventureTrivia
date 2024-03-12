import unittest
from Characters.hero_factory import HeroFactory
from Characters.hero_rogue import Rogue


class CharacterUnitTests(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_hero_creation(self):
        assert isinstance(HeroFactory().create_rogue(), Rogue)

if __name__ == '__main__':

    unittest.main()
