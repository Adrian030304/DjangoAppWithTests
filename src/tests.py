import unittest

from app import Superhero

class TestSuperhero(unittest.TestCase):

    # setting a setup method for fixture so we dont repeat the instantiation of an object for example
    # this runs before every single test method
    def setUp(self):
        self.superhero = Superhero('Spiderman', 50)

    def test_stringify(self):
        self.assertEqual(str(self.superhero), 'Spiderman')

    def test_is_stronger(self):
        other_hero = Superhero('Batman', 55)
        self.assertFalse(self.superhero.is_stronger_than(other_hero))
        self.assertTrue(other_hero.is_stronger_than(self.superhero))
