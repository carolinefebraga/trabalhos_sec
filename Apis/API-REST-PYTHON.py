import requests
import os

while True:

	os.system('clear')


	id = input('Digite o seu ID:')


	os.system('clear')

	r = requests.get('http://jsonplaceholder.typicode.com/todos/{}'.format (id))
	data = r.json()

	print('O seu ID informado foi: {}'.format(data['id']))
	print()
	print('O seu UserID é: {}'.format(data['userId']))
	print()
	print('O seu título é: {}'.format(data['title']))
	print()


	loop = input('Deseja inserir outro ID? (S/N)')
	if loop not in ('S', 's'):
		print('Encerrando o programa...')
		break