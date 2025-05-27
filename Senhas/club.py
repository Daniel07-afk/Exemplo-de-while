time = input("Digite o nome do melhor time do Brasil:")

while time != 'Tricolor':
    time = input('Qual é o melhor time do Brasil:')
    if time == 'Tricolor':
        print('Você acertou! Salve o tricolor Paulista!')
    else:
        print('tente novamente!')