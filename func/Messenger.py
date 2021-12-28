from func.MailServer import MailServer
from func.TemplateEngine import TemplateEngine

class Messenger:
	def __init__(self):
		self.templateEngine = TemplateEngine()
		self.mailServer = MailServer()
	
	def send(self, person, message):
		return self.mailServer.send(person, self.templateEngine.create(message))

	def receive(self):
		return self.mailServer.receive()


