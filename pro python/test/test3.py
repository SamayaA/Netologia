import unittest

from yandex_authentication import YaAuth
class TestYaAuth(unittest.TestCase):
    def setUp(self) -> None:
        self.a = YaAuth()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_authentication(self):
        # assign login and password
        login = ...
        password = ...
        self.assertIsNone(self.a.authentication(login, password))

if __name__ == "__main__":
    unittest.main()


    