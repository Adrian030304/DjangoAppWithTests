import unittest

from app import Superhero

class TestSuperhero(unittest.TestCase):
    def test_stringify(self):
        superhero = Superhero('Spiderman', 50)
