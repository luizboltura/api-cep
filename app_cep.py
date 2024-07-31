import requests as rq

lista_ceps = list()

print("Digite os CEPs para adicionar à lista. Digite 'sair' para parar.\n")

while True:
    cep = input("Digite um CEP para adicionar à lista: ")
    if cep.lower() == 'sair':
        break
    lista_ceps.append(cep)

lista_enderecos = list()

for cep in lista_ceps:
    url = f'https://viacep.com.br/ws/{cep}/json/'
    req = rq.get(url, timeout=3)
    endereco = req.json()

    lista_enderecos.append(endereco)

print(lista_enderecos)