""" import time


def PensarPor10Segundos():
    print("pensando")
    time.sleep(10)
    print("Lembrei!")


if 10 > 5:

    print("10 é maior que 5")


class BemVindo():
    def __init__(self):
        print("Bem vindo")


oi = BemVindo()
# CARACTERES DE ESCAPE : \ A BARRA INVERTIDA
print("Olá meu nome é \n Gustavo")
print("COdar todos \'os dias\'")
print("Arquivo localizado em \\c:drive\\arquivo.txt")
# printar o nome usando variaveis
nome = "Gustavo"
print(nome)
# descobrit a quantidades de caracters
print(len(nome))
print("Vamos codar!")
print("Vamos 'Codar!'")
print('Vamos \n"codar!!"')

# String dinamico
nome = "Gustavo"
email = "gustavome05@gmail.com"

# exiba a seguinte menssagem :Olá gustavo voce cadastrou o email gustavome05@gmail.com, essa informação está correta ??

print(f"Olá {nome} voce cadastrou o email {email}, essa informação está correta ??")

# crie os seguintes strings dinamicos
nome = "carol"
hobby = "ouvir musica"

print(f"Olá sou a {nome} e meu hobby é ouvir {hobby}")

# monte as seguintes palvaras usando as silabas como base
b = "ba"
parte2 = "nica"
a = "a"
r = "ri"
parte1 = "eletrô"
t = "te"

print(f"{b}{t}{r}{a} {parte1}{parte2}") """
# metodos comun das strings
""" nome_curso = "  Edição de Video"
# 012345
# upper deixa tudo maiusculo
print(nome_curso.upper())
# lower deixa tudo minusculo
print(nome_curso.lower())
# strip remove todos os espáços em branco
print(nome_curso.strip())
# lstrip remove espaços em branco do ladp left(esqeuerdo)
print(nome_curso.lstrip())
# rstrip remove todos espaços em branco do lado right(direito )
print(nome_curso.rstrip())
# find encontra informações dentro das estring -- aqui mostra que a letra 'Ç' esta no indice 5 pois temos espacços na palavra e a contagem inicia a partir de '0'
print(nome_curso.find("ção"))
# replace substitui palavras chaves
print(nome_curso.replace("Video", "Musica"))
print("http://sc.olx.com.br/?o=90&q=relogio".replace("relogio", "carros"))
# pratricas desafio
"""
a = "é"
b = "MELHOR"
c = "QUE"
d = "feito"
e = "perfeito"
# resultado deve ser = È melhor FEITO que PERFEITO

print(f"{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}")

# referenciando uma string usando-se = ' [] '
teclado = "Teclado"

print(teclado[2])
