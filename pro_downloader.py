import requests

def baixar_arquivo(url,endereco):
	resposta = requests.get(url)
	if resposta.status_code == requests.codes.OK:
		with open(endereco, 'wb') as novo_arquivo:
			novo_arquivo.write(resposta.content)
		print("Download finalizado. Nome do arquivo: {}".format(endereco))
	else:
		resposta.raise_for_status()	


if __name__ == "__main__":
	baixar_arquivo('https://esic.br/manuais2021/Pol%C3%ADticadeloginEsenha.pdf', 'Gerenciamento de Senhas.pdf')
