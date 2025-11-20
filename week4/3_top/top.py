#Perfectly secure. That's for sure! Or can break it and reveal my secret?
#We are given a encryption script and the a file which is encrypted with it

#HINT1:ciao
#We are given a script that generated the encrypted file. 
#The challenge here is to spot potential vulnerabilities.  
#The first thing to do is to debug it; we can find the following steps: 
#Set a seed with a time.  
#Get an input string 
#Define a key for the string 
#Encryption: the final output is the concatenation of both encrypted message and encrypted time!  

#HINT2:
#The time characters are encrypted with some fixed values (0x88). Since we are talking about a xor operation, 
    #we can retrieve the original time. To know the length, get a time variable and see how many characters we do have.  
#Then, once we have the “plain” time, we ca regenerate the original sequence of characters that compose the key … and 
    #apply it to the encrypted text. We finally have the flag.  


#!/usr/bin/env python3
import random
import sys
import time

cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

msg = input('Your message: ').encode('ASCII')
key = [random.randrange(256) for _ in msg]
c = [m ^ k for (m,k ) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

with open(sys.argv[1], "wb") as f:
    f.write(bytes(c))
