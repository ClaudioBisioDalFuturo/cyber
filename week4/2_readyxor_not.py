#original data: "El Psy Congroo"         testo in chiaro
#encrypted data: "IFhiPhZNYi0KWiUcCls="  ciphertext (base64)
#encrypted flag: "I3gDKVh1Lh4EVyMDBFo="  ciphertext (base64)

#The flag is a composition of two names (two animals (?)). 

#La cifratura è XOR con una chiave ripetuta (repeating-key XOR) e poi codifica Base64
#puoi ricavare la chiave:
#possiamo ricavare la chiave con "key = ciphertext ⊕ plaintext"
   #Poi applichiamo la stessa chiave ripetuta al ciphertext della flag per ottenere il plaintext della flag.

#PASSAGGI:
#1. Decodifica base64 i due ciphertext
#2. XOR byte per byte il ciphertext decodificato, il risultato è la chiave ripetuta
#3. se la chiave si ripete
#4. Applichiamo la chiave ripetuta al ciphertext della flag con XOR per ottenere il plaintext

import base64

known_plain = b"El Psy Congroo" #texto in chiaro

ct_b64 = "IFhiPhZNYi0KWiUcCls=" #encrypted data
ct = base64.b64decode(ct_b64) #decodifica base64

flag_b64 = "I3gDKVh1Lh4EVyMDBFo=" #encrypted flag
flag_ct = base64.b64decode(flag_b64) #decodifica base64

# 3) ricava la chiave (byte-wise XOR)
key_bytes = bytes([c ^ p for c, p in zip(ct, known_plain)])
# probabilmente otterrai "e4Bne4Bne4Bne4" (cioè "e4Bn" ripetuto)
# prendi la parte ciclata (la lunghezza del pattern)
# qui osserviamo che la chiave corta è "e4Bn"
key = b"e4Bn"

# 4) funzione repeating XOR per decriptare
def repeating_xor(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

flag_plain = repeating_xor(flag_ct, key)
print(flag_plain.decode()) #stampo il risultato