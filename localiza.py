
print('------ Descontos -----')

def desconto(valor):
    desconto = int(input('Qual o desconto em %: '))
    valorComDesconto = valor - ((desconto/100)*valor)
    print('Sua compra no valor de {} teve um desconto de {}% Totalizando:{} Reais'.format(valor,desconto,valorComDesconto))



valor = float(input('Valor da compra: '))

op = int(input('Desconto?: [1/0] '))

while(op != 1 and op!= 0):
    print('Valor invalido, digite novamente:')
    op = int(input('Desconto?: [1/0] '))


if 1 == op:
    print('SIM')
    desconto(valor)

elif 0 == op:
    #print('NÃO')
    print('Total a pagar: {}'.format(valor))

else:
    print('Erro')




