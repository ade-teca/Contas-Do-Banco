from datetime import datetime
from random import randint
import pytz


class ContaCorrente:
    """

    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente
        cpf (str): CPF do cliente
        agencia (str): Agência responsável pela conta do cliente
        num_conta (str): Número da conta do cliente
        saldo (float): Saldo disponível na conta do cliente
        limite (float): Limite de cheque especial do cliente
        transacoes (list): Histórico de transações do cliente

    """

    @staticmethod
    def _data_hora():
        """Retorna a data e hora atual"""
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, conta):
        """Inicialização da classe"""
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.conta = conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        """Consulta o valor do saldo"""
        print("O saldo atual é de: R$ {:,.2f}".format(self._saldo))

    def depositar(self, valor):
        """Deposita um valor na conta"""
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _definir_limite_conta(self):
        """Define o limite da conta. Método privado"""
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        """Retira um valor da conta"""
        if self._saldo - valor < self._definir_limite_conta():
            print("O seu saldo é insuficiente para o saque informado")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consulta_limite_conta(self):
        """Retorna o limite em cheque especial"""
        print("O seu limite de cheque especial é de {}".format(self._definir_limite_conta()))

    def consultar_historico_transacoes(self):
        """Consulta o histórico de transações"""
        print("Histórico de transações")
        print("Valor, Saldo, Data e Hora")
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        """Realiza transferência entre contas"""
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        """Retorna a data e hora atual"""
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.codigo_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self._senha = 1234
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Senha inválida.")