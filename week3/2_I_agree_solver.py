# The description says:
# "ceasar is everything"

# potrebe essere stat usata la crittogragia di cesare come nell'esercizioo precedente
puzzle = 'vhixoieemksktorywzvhxzijqni'

def ceasar_cracker(text, from_ = -30, to_=+30):
    for i in range(from_, to_):                                 #possible keys [-30, 30]
        
        curr_step = ''.join([chr(ord(c) + i) for c in text])    #decode

        
        print(f"Step={i}\t{curr_step}")                         #stampa risultato

ceasar_cracker(puzzle)                                          #richiamo la funzione

# I don't see any proper flag. We need to find another way
# la descrizione dice che si tratta di "next level" of ceasar.

# lìevoluzione di cesare la troviamo nel "vigenere cipher".
# ma il vigenere richiede una chiave
# utiliziamo servizi online di bruteforce come
#   https://www.guballa.de/vigenere-solver
#
# la flag è: theforceisstrongwiththisone
#
# the key is "ceasar" ... as the hint suggested
