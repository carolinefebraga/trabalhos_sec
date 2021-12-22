import requests
import os

while True:
	os.system('clear')

	id = input('Digite o seu Id:')

	os.system('clear')

	r = requests.get('http://jsonplaceholder.typicode.com/todos/{}'.format(id))
	data = r.json()

	print('O seu ID informado foi: {}'.format(data['id']))
	print()
	print('O seu userID informado foi:{}'.format(data['userId']))
	print()
	print('O seu título correspondente é: "{}"'.format(data['title']))
	print()

	loop = input('Deseja inserir outro ID? (S/N)')
	if loop not in ('S', 's'):
		os.system('clear')
		print('Encerrando o programa...')
		break