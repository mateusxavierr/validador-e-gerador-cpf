import random

validade = None

def digit(qtdNumerosMultiplicados, multiplicador):
    soma = 0
    for num in cpf_[:(qtdNumerosMultiplicados)]:
        multiplicacao = (int(num) * multiplicador)
        multiplicador -= 1
        soma += multiplicacao

    restoDivisao = (soma * 10 % 11)
    if restoDivisao > 9:
        digit = 0
    else: 
        digit = restoDivisao

    return digit

cpf_ = input('Digite um CPF ou pressione enter para gerar um aleatório: ').replace('.', '').replace('-', '').replace(' ', '')

if cpf_ == '':
    for i in range(9):
        cpf_ += str(random.randint(0, 9))
    
    primeiroDigito = digit(9, 10)
    cpf_ += str(primeiroDigito)
    segundoDigito = digit(10, 11)
    cpf_ += str(segundoDigito)

if len(cpf_) == 11:
    try:
        primeiroDigito = digit(9, 10)
        segundoDigito = digit(10, 11)

    except (ValueError, IndexError):
        print('Entrada inválida')

    else:
        if primeiroDigito == int(cpf_[9]) and segundoDigito == int(cpf_[10]):
            validade = 'válido'
        else:
            validade = 'inválido'

        print(f'{primeiroDigito} e {segundoDigito} - CPF {validade}: {cpf_}')
else:
    print('Entrada inválida')
