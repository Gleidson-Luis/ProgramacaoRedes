import datetime

#Desafio: Calcular a idade do usuário
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
print("A idade do usuário é: ", idade)