class Subscriber:
	def __init__(self, list):
		self.list = list

	def add_client(self, client):
		if type(client) is not str:
			raise ValueError('Wrong client')
		self.list.append(client)
		return self.list

	def delete_client(self, client):
		if type(client) is not str or client not in self.list:
			raise ValueError('Wrong client')
		self.list.remove(client)
		return self.list

	def send_message(client, message):
		pass