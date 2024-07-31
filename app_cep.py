import requests as rq

lista_ceps = list()
print("Digite o CEP que deseja buscar: ")

lista_enderecos = list()

cep = input("Digite um CEP para consulta: ")

url = f'https://viacep.com.br/ws/{cep}/json/'
req = rq.get(url, timeout=3)
endereco = req.json()


print(endereco)