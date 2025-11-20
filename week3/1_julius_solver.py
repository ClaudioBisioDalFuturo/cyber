# Julius,Q2Flc2FyCg==
# dato che finisce con ==
# allora sappiamo che è a base64 encoding

import base64
enc_b64 = 'Q2Flc2FyCg=='

#we define a function. It might be helpful in future
def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")          #decodifica la Base64 in bytes.
                #funzione del import b64decode
print(f"Decoding=\t{base64tostring(enc_b64)}")                              #trasforma i bytes in stringa UTF-8, ignorando eventuali byte non validi.

# l'indizio recita "caesar", allora sappiamo che dovremo usare la crittografia di cesare
# con questo nome possiamo applicarlo e invertirlo fino al testo decifrato

puzzle = 'fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=='
print("The length of the puzzle is:\t", len(puzzle))                        #decodifica Base64 del puzzle. Il risultato è una stringa 
                                                                            #(molto probabilmente piena di caratteri non leggibili).

# la lunghezza è un multiplo di 4, l'alfabeto sembra troppo regolare (niente punteggiatura)
# possiamo pensare che è una stringa a base64 encoded string
puzzle_dec = base64tostring(puzzle)
print("Decoded puzzle:", puzzle_dec)

#applichiamo la crittografia di cesare da -30 a +30
def ceasar_cracker(text, from_ = -30, to_=+30):                             #Per ogni possibile i somma i a ord(c) di ogni carattere e ricrea il carattere con chr(...)
    for i in range(from_, to_):                                 #possibili chiavi [-30, 30]
        
        curr_step = ''.join([chr(ord(c) + i) for c in text])    #decodifico

        
        print(f"Step={i}\t{curr_step}")                         #stampo il risultato

ceasar_cracker(puzzle_dec)
# cerchiamo una stringa leggibile come quella al passo -24
# FLAG: ecCTF3T_7U_BRU73?!




#--------------------------FUNZIONAMENTO:------------------------------------------------------------------------------------------------
#1. Decodifica una stringa Base64 (Q2Flc2FyCg==) per ottenere un suggerimento.

#2. Prende un'altra stringa che sembra Base64 (puzzle) e la decodifica.

#3. Applica una sorta di brute-force sul testo decodificato: prova a sommare/sottrarre tutti i possibili valori di offset (da -30 a +29) 
#   ai codici Unicode di ogni carattere, stampando il risultato per ogni tentativo.

#4. Osservando le uscite, l’autore trova una riga leggibile (la flag) al passo -24