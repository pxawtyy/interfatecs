# InterFatecs 2023 - Problema C
entrada = input()
qtd = int(entrada.split()[0]) # 1 <= qtd <= 26, converte para int o primeiro elemento da entrada
maiuscula = True if entrada.split()[1] == 'maiusculas' else False # usa bool pra determinar se é maiúscula ou minúscula
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista = lista if (maiuscula) else [letra.lower() for letra in lista] # se verdadeiro, transforma cada letra em minúscula

i = 0 # variável de controle
letras = '' # string vazia

while i < qtd:
    print('.' * (25 - i), end='') # imprime os pontos com base em i
    letras += lista[i] # adiciona a letra correspondente do index na string
    print(letras)
    i += 1 