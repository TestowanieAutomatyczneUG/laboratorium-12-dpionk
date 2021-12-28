import requests

class RandomUser:
	def __init__(self):
		self.source='https://randomuser.me/api'
		self.nationalities=['AU', 'BR', 'CA', 'CH', 'DE', 'DK', 'ES', 'FI', 'FR', 'GB', 'IE', 'IR', 'NO', 'NL', 'NZ', 'TR', 'US']
		self.genders=['female', 'male']
	
	def getRandomUser(self):
		r = requests.get(self.source)
		return r.json()['results'][0]

	def getRandomUserGender(self, gender):
		if gender in self.genders :
			r = requests.get(f'{self.source}?gender={gender}')
			return r.json()['results'][0]
		raise ValueError('Wrong gender')

	def getRandomUserNationality(self, nationality):
		if nationality in self.nationalities:
			r = requests.get(f'{self.source}?nat={nationality.lower()}')
			return r.json()['results'][0]
		raise ValueError('Wrong nationality')

