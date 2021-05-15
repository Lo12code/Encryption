#!/usr/bin/env python3

import string

flag = ""

flag_text = flag[8:-1]


letras = string.ascii_lowercase
lista_letras = []

for letra in letras:
	lista_letras.append(letra)



for t in range(26):

	nova_flag = []

	for i in flag_text:
		
		posicao = lista_letras.index(i)
		posicao -= t

		nova_flag.append(lista_letras[posicao])	

	print (''.join(nova_flag))