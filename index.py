input_testo = input(str("Inserisci la parola che vuoi trasformare in BTW: " ))

input_testo = input_testo + '$'

print("Testo senza BTW: " + input_testo)

lista_rotazioni =[]


for i in range(len(input_testo)):
    rotazione = input_testo[i:] + input_testo[:i]
    lista_rotazioni.append(rotazione)

lista_rotazioni.sort()

btw_risultato = ""

for riga in lista_rotazioni:
    btw_risultato+= riga[-1]


print("Testo con BTW: ", btw_risultato)

    
