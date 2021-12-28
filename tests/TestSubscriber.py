from func.Subscriber import Subscriber
import unittest
from unittest.mock import *

class TestSubscriber(unittest.TestCase):

	def setUp(self):
		self.temp = Subscriber([])

	def test_add_client(self):
		self.temp.add_client = MagicMock(return_value=['Daria'])
		self.assertEqual(['Daria'], self.temp.add_client('Daria'))

	def test_add_client_wrong(self):
		self.temp.add_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.add_client,456546)
			
	def test_add_client_wrong2(self):
		self.temp.add_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.add_client,{'Daria' : 5})

	def test_add_client_wrong3(self):
		self.temp.add_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.add_client,[1,3,45,4,5])

	def test_add_client_wrong4(self):
		self.temp.add_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.add_client,None)

	def test_delete_client(self):
		self.temp.delete_client = MagicMock(return_value=[])
		self.assertEqual([], self.temp.delete_client('Daria'))	

	def test_delete_client_wrong(self):
		self.temp.delete_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.delete_client,True)

	def test_delete_client_wrong2(self):
		self.temp.delete_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.delete_client,None)

	def test_delete_client_wrong3(self):
		self.temp.delete_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.delete_client,5646546.456564)

	def test_delete_client_wrong4(self):
		self.temp.delete_client = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.delete_client,{'sdfsdf': 'dfsdfs'})

	def test_send_message(self):
		self.temp.sendMessageToClient = MagicMock(return_value = True)
		self.assertTrue(self.temp.sendMessageToClient('Daria', 'wiadomość'))

	def test_send_message_wrong(self):
		self.temp.send_message = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.send_message,45645654, 'wiadomość')

	def test_send_message_wrong2(self):
		self.temp.send_message = MagicMock(side_effect=ValueError('Wrong message'))
		self.assertRaises(ValueError, self.temp.send_message,'Daria', 75675745 )

	def test_send_message_wrong3(self):
		self.temp.send_message = MagicMock(side_effect=ValueError('Wrong client'))
		self.assertRaises(ValueError, self.temp.send_message,{}, [])

	def test_send_message_client_not_in_list(self):
		self.temp.send_message = MagicMock(side_effect=ValueError('Client not found'))
		self.assertRaises(ValueError, self.temp.send_message,'some client', 'wiadomość')

	def tearDown(self):
		self.temp=None