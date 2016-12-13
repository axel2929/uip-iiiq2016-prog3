from unittest import TestCase
from quiz10 import cuenta

class TestCuenta(TestCase):
    def test_deposito(self):
        a = cuenta ()
        self.assertEqual(a.deposito(300), 500)


    def test_retiro(self):
        a = cuenta ()
        self.assertEqual(a.retiro(300), 500)
