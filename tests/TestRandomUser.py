from func.RandomUser import RandomUser
import unittest
from unittest.mock import *

class TestRandomUser(unittest.TestCase):

	def setUp(self):
		self.temp = RandomUser()
	
	def test_random_user_get_random_user_ok(self):
		user = self.temp.getRandomUser()
		self.assertIsInstance(user, dict)

	def test_random_user_get_user_nationality_es (self):
		user = self.temp.getRandomUserNationality('ES')
		self.assertEqual(user['location']['country'], 'Spain')

	def test_random_user_get_user_nationality_de (self):
		user = self.temp.getRandomUserNationality('DE')
		self.assertEqual(user['location']['country'], 'Germany')

	def test_random_user_get_user_nationality_wrong (self):
		self.assertRaises(ValueError, self.temp.getRandomUserNationality,'dfgfdgfdg')

	def test_random_user_get_user_nationality_wrong2 (self):
		self.assertRaises(ValueError, self.temp.getRandomUserNationality,65466)

	def test_random_user_get_user_nationality_wrong3 (self):
		self.assertRaises(ValueError, self.temp.getRandomUserNationality,{'DE'})

	def test_random_user_get_user_gender_male_ok(self):
		user = self.temp.getRandomUserGender('male')
		self.assertEqual(user['gender'], 'male')

	def test_random_user_get_user_gender_female_ok(self):
		user = self.temp.getRandomUserGender('female')
		self.assertEqual(user['gender'], 'female')

	def test_random_user_get_user_gender_wrong(self):
		self.assertRaises(ValueError, self.temp.getRandomUserGender, 56756567)

	def test_random_user_get_user_gender_wrong2(self):
		self.assertRaises(ValueError, self.temp.getRandomUserGender, 'sdfdsfd')

	def test_random_user_get_user_gender_wrong3(self):
		self.assertRaises(ValueError, self.temp.getRandomUserGender, [])


	def tearDown(self):
		self.temp = None