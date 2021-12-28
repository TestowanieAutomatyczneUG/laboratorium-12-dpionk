import unittest
from unittest.mock import *
from func.Messenger import Messenger

class TestMessenger(unittest.TestCase):

	def setUp(self):
		self.temp = Messenger()

	def test_send(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.return_value = True
		self.assertTrue(self.temp.send('Daria', 'message'))

	def test_send_didnt_send(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.return_value = False
		self.assertFalse(self.temp.send('Daria', 'message'))

	def test_send_wrong(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.side_effect = ValueError('Wrong client')
		self.assertRaises(ValueError, self.temp.send,5654654466, 'message')
			

	def test_send_wrong2(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.side_effect = ValueError('Wrong client')
		self.assertRaises(ValueError, self.temp.send,756.5677657, 'message')

	def test_send_wrong3(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.side_effect = ValueError('Wrong client')
		self.assertRaises(ValueError, self.temp.send,[], 'message')

	def test_send_message_wrong(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.side_effect = ValueError('Wrong message')
		self.assertRaises(ValueError, self.temp.send,'Daria', 464565464)

	def test_send_message_wrong2(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.side_effect = ValueError('Wrong message')
		self.assertRaises(ValueError, self.temp.send,'Daria', None)

	def test_send_message_wrong3(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.side_effect = ValueError('Wrong message')
		self.assertRaises(ValueError, self.temp.send,'Daria',{True})

	def test_send_message_not_send_message_not_str_but_dict(self):
		self.temp.templateEngine = MagicMock()
		self.temp.mailServer = MagicMock()
		self.temp.templateEngine.create.side_effect = 'message'
		self.temp.mailServer.send.side_effect = ValueError('Wrong message')
		self.assertRaises(ValueError, self.temp.send,'Daria',[45,3454,55,3])

	def test_receive(self):
		self.temp.mailServer = MagicMock()
		self.temp.mailServer.receive.return_value = 'message'
		self.assertEqual('message', self.temp.receive())

	def test_receive_message_not_received(self):
		self.temp.mailServer = MagicMock()
		self.temp.mailServer.receive.return_value = False
		self.assertFalse(self.temp.receive())