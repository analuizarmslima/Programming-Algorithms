# exercicio 1: soma
n1 = int(input("digite n1: "))
n2 = int(input("digite n2: "))
soma = n1+n2
print(soma)

# exercicio 2: média
nota1 = float(input("digite a nota1: "))
nota2 = float(input("digite nota2: "))
media = (nota1 + nota2) /2
print(media)

# #exercicio 3: antecessor e sucessor 
n = int(input("digite um numero: "))
antecessor= n - 1 
sucessor = n + 1
print(f"o sucessor do numero {n} é o {sucessor} e o antecessor é o {antecessor}")

#exercicio 4: dobro, triplo e metade
valor = float(input("digite um valor: "))
dobro = valor *2
triplo = valor *3
metade = valor /2
print(f"o dobro de {valor} é {dobro}, o triplo é {triplo} e a metade é {metade}")

#exercicio 5: conversão de m,cm,mm
m = float(input("digite o metro: "))
cm = m *100
mm = m *1000
print(f"{m} metros são {cm}cm que, por sua vez, são {mm}mm")

#exercicio 6: area e perimetro do retangulo
largura = float(input("digite a largura: "))
altura = float(input("digite a altura: "))
area = largura * altura
perimetro = 2 * (largura + altura)
print(f"A área do retângulo é {area} e o perímetro é {perimetro}")

#exercicio 7: Celsius para Fahrenheit
celsius = float(input("digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivalem a {fahrenheit}°F")

#exercicio 8: Desconto no produto
preco = float(input("digite o preço do produto: "))
desconto = preco * 0.10
preco_final = preco - desconto
print(f"O desconto foi de {desconto} e o preço final é {preco_final}")
 
#exercicio 9: Reajuste salarial
salario = float(input("digite o salário atual: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O aumento foi de {aumento} e o novo salário é {novo_salario}")

#exercicio 10: Salário com comissão
salario_fixo = float(input("digite o salário fixo: "))
total_vendas = float(input("digite o total vendido: "))
comissao = total_vendas * 0.04
salario_total = salario_fixo + comissao
print(f"A comissão foi de {comissao} e o salário total é {salario_total}")

#exercicio 14: Troca de valores~~´[~[;;]]
a = int(input("digite o valor de A: "))
b = int(input("digite o valor de B: "))
aux = a
a = b
b = aux
print(f"Depois da troca, A = {a} e B = {b}")

#exercicio 15: Custo final da compra
preco_unitario = float(input("digite o preço unitário: "))
quantidade = int(input("digite a quantidade: "))
frete = float(input("digite o valor do frete: "))
subtotal = preco_unitario * quantidade
total = subtotal + frete
print(f"O subtotal dos produtos é {subtotal} e o total da compra é {total}")
