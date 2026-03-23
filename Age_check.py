nome = input('Insira o seu nome: ')
idade = float(input('Insira sua idade: '))

if idade >= 18:
    print(f'{nome}, você é maior de idade')
else:
    print(f'{nome}, você é menor de idade')
