import requests

def baixar_arquivo(url,endereco):
	resposta = requests.get(url)
	with open (endereco, 'wb') as novo_arquivo:
		novo_arquivo.write(resposta.content)



if __name__=="__main__":
	baixar_arquivo('https://wp.ufpel.edu.br/seginfo/files/2016/06/OUCH-201510_pt.pdf', 'Gerenciamento de senhas.pdf')
