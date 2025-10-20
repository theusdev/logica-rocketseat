perguntas = [ ['Seu animal gosta de bananas', 'macaco']
]

while True:
  print('pense em um animal...')

  acertou = False

  for pergunta in perguntas:
  resposta = input(f'{pergunta[0]} (s/n):')
  if (resposta.lower() == 's'):
    print(f'O animal é um {pergunta[1]}')
    acertou = True
    break

  if not acertou:
    animal = input('Desisto! qual é o animal que você pensou? ')
    novaPergunta = input(f'Qual pergunta eu poderia fazer para distinguir um {animal}? ')
    perguntas.append( [novaPergunta, animal] ) 

  resposta = input('Quer jogar novamente? (s/n): ')
  if (resposta.lower() != 's'):
    print('Obrigado por jogar!')
    break

