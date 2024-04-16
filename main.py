from ContasBanco import ContaCorrente, CartaoCredito
from Agencia import Agencia

#Criar uma conta
conta_Keisar = ContaCorrente("Adelito Teca", "222.345.654.23", 1234, 32245)

#Criar um cartão de crédito
cartao_Keisar = CartaoCredito("Adelito Teca", conta_Keisar)

print(conta_Keisar.__dict__)
print(cartao_Keisar.__dict__)
print('\n'+'*'*20 +'\n')
agencia1 = Agencia(22237777, 256789092, 29752)

agencia1.caixa = 1000000

print(agencia1.__dict__)

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(1000, 1236722, 0.1)