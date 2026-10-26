print("3. TUPLAS SÃO IMUTÁVEIS:\n")

tupla = ("Ana Luiza", 12345678910, "analuiza@gmail.com")
print(f"Tupla original: {tupla}\n")

print("Tentando modificar:")
try:
    tupla[0] = "Ricardo"
except TypeError as e:
    print(f" Erro: {e}\n")

print("Tentando trocar valores:")
try:
    tupla.append(4)
except AttributeError as e:
    print(f" Erro: Tuplas não têm append\n")

print(" Tuplas são imutáveis (proteção de dados)")
print(" Listas podem ser modificadas\n")

print("="*60 + "\n")