import unittest
from Model.user import User
from Model.place import Places

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User(email="test@example.com")
        self.assertEqual(user.email, "test@example.com")

    def test_email_uniqueness(self):
        User.create(email="test1@example.com")
        with self.assertRaises(ValueError):
            User.create(email="test1@example.com")

class TestPlaces(unittest.TestCase):
    def test_create_place(self):
        user = User.create(email="test@example.com")
        place = Places.create(user)
        self.assertEqual(place.host, user)

    def test_host_is_user(self):
        with self.assertRaises(ValueError):
            Places.create("not a user instance")

if __name__ == '__main__':
    unittest.main()