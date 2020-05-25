# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():

    def __init__(self,nome,cidade,telefone,email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("Objeto criado")

    def __str__(self):
        return "O usuário " + self.nome + " mora na cidade " + self.cidade

P1 = Pessoa("Rafaella", "Uberlândia", 991195202, "rafaella.d.d.carvalho@gmail.com")
print(str(P1))