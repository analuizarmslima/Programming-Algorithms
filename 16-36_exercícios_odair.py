# exercicio 16: positivo, negativo ou zero
n = float(input("digite um número: "))
if n > 0:
    print("POSITIVO")
elif n < 0:
    print("NEGATIVO")
else:
    print("ZERO")

# exercicio 17: par ou ímpar
n = int(input("digite um número: "))
if n % 2 == 0:
    print("PAR")
else:
    print("ÍMPAR")

# exercicio 18: maior de dois números
n1 = float(input("digite o primeiro valor: "))
n2 = float(input("digite o segundo valor: "))
if n1 > n2:
    print(f"Maior valor: {n1}")
elif n2 > n1:
    print(f"Maior valor: {n2}")
else:
    print("VALORES IGUAIS")

# exercicio 19: maior e menor de três números
n1 = float(input("digite o primeiro valor: "))
n2 = float(input("digite o segundo valor: "))
n3 = float(input("digite o terceiro valor: "))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f"Maior: {maior}")
print(f"Menor: {menor}")

# exercicio 20: três valores em ordem crescente
n1 = int(input("digite o primeiro valor: "))
n2 = int(input("digite o segundo valor: "))
n3 = int(input("digite o terceiro valor: "))
ordem = sorted([n1, n2, n3])
print(f"Ordem crescente: {ordem[0]}, {ordem[1]}, {ordem[2]}")

# exercicio 21: aprovado ou reprovado
nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f"Média: {media} - APROVADO")
else:
    print(f"Média: {media} - REPROVADO")

# exercicio 22: situação do aluno por faixa
nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
media = (nota1 + nota2) / 2
if media < 5.0:
    situacao = "REPROVADO"
elif media < 7.0:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"
print(f"Média: {media} - {situacao}")

# exercicio 23: categoria de votação
idade = int(input("digite a idade: "))
if idade < 16:
    print("NÃO PODE VOTAR")
elif idade == 16 or idade == 17 or idade >= 70:
    print("VOTO OPCIONAL")
else:
    print("VOTO OBRIGATÓRIO")

# exercicio 24: ano bissexto
ano = int(input("digite o ano: "))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("ANO BISSEXTO")
else:
    print("NÃO BISSEXTO")

# exercicio 25: preço conforme a forma de pagamento
preco = float(input("digite o preço: "))
opcao = int(input("digite a opção de pagamento (1 a 4): "))
if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.08
print(f"Valor final: R$ {valor_final:.2f}")

# exercicio 26: reajuste por faixa salarial
salario = float(input("digite o salário atual: "))
if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento
print(f"Percentual: {percentual}%")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

# exercicio 27: classificação de IMC
peso = float(input("digite o peso em kg: "))
altura = float(input("digite a altura em metros: "))
imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")

# exercicio 28: é possível formar um triângulo?
a = float(input("digite o lado A: "))
b = float(input("digite o lado B: "))
c = float(input("digite o lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("FORMAM UM TRIÂNGULO")
else:
    print("NÃO FORMAM UM TRIÂNGULO")

# exercicio 29: tipo de triângulo
a = float(input("digite o lado A: "))
b = float(input("digite o lado B: "))
c = float(input("digite o lado C: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("NÃO FORMA TRIÂNGULO")

# exercicio 30: aprovação de empréstimo
imovel = float(input("digite o valor do imóvel: "))
salario = float(input("digite o salário: "))
anos = int(input("digite o prazo em anos: "))

prestacao = imovel / (anos * 12)
limite = salario * 0.30

print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite: R$ {limite:.2f}")
if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")

# exercicio 31: divisível por 3 e por 5
n = int(input("digite um número: "))
if n % 3 == 0 and n % 5 == 0:
    print("DIVISÍVEL POR 3 E 5")
elif n % 3 == 0:
    print("DIVISÍVEL APENAS POR 3")
elif n % 5 == 0:
    print("DIVISÍVEL APENAS POR 5")
else:
    print("NÃO DIVISÍVEL POR 3 NEM 5")

# exercicio 32: número dentro do intervalo
n = float(input("digite um número: "))
if 10 <= n <= 20:
    print("DENTRO")
else:
    print("FORA")

# exercicio 33: dia da semana
opcao = int(input("digite um número de 1 a 7: "))
if opcao == 1:
    print("SEGUNDA-FEIRA")
elif opcao == 2:
    print("TERÇA-FEIRA")
elif opcao == 3:
    print("QUARTA-FEIRA")
elif opcao == 4:
    print("QUINTA-FEIRA")
elif opcao == 5:
    print("SEXTA-FEIRA")
elif opcao == 6:
    print("SÁBADO")
elif opcao == 7:
    print("DOMINGO")
else:
    print("OPÇÃO INVÁLIDA")

# exercicio 34: quantidade de dias do mês
mes = int(input("digite o mês (1 a 12): "))
ano = int(input("digite o ano: "))

if mes < 1 or mes > 12:
    print("MÊS INVÁLIDO")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    print("31 dias")
elif mes in [4, 6, 9, 11]:
    print("30 dias")
elif mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print("29 dias")
    else:
        print("28 dias")

# exercicio 35: valor do ingresso
idade = int(input("digite a idade: "))
estudante = input("é estudante? (SIM/NÃO): ").strip().upper()

if idade < 12 or estudante == "SIM" or idade >= 60:
    valor = 15.00
else:
    valor = 30.00
print(f"Valor do ingresso: R$ {valor:.2f}")

# exercicio 36: contagem de 1 até 10
for i in range(1, 11):
    print(i)