soma = 0
quantidade = 0
anterior = None
crescente = True

print("Digite números inteiros positivos (digite 0 para parar)")

while True:
    try:
        numero = int(input("Número: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    
    if numero == 0:
        break

    if numero < 0:
        print("O número deve ser maior que zero.")
        continue

    
    if anterior is not None and numero <= anterior:
        crescente = False
        quantidade += 1
        print("O número informado é menor ou igual ao anterior.")
        break
    
    quantidade += 1
    anterior = numero


if quantidade == 0:
    print("Nenhum número foi informado.")
else:
    if crescente:
        print("A sequência é crescente.")
    else:
        print("A sequência NÃO é crescente.")

    print(f"Quantidade de números informados: {quantidade}")