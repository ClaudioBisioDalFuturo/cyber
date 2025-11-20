#Sherlock has a mystery in front of him. Help him to find the flag.

#The first intui is to notice that there are some characters uppercase, so we can open and filter them (we
# suggest to use Python).
 #open the text file
# with open('challenge.txt', 'r') as file:
#    challenge = file.read()
 #extract uppercase letters
# insight=''.join([c for c in challenge if c.isupper()])
# print(insight)
# The output is a string with a series of “ZERO” and “ONE”. We can first convert them into their
# numerical representation. 
#insight = insight.replace('ZERO', '0')
# insight = insight.replace('ONE', '1')
# We can then look of the length of this new string: it is a multiple of 8. The new intuition is that this
# string represents a series of unicode characters written I binary. We just need to reverse this process.
# result=''.join(chr(int(insight[i*8:i*8+8],2)) for i in range(len(insight)//8))
# print(result)


#open the text file
with open('challenge.txt', 'r') as file:
    challenge = file.read()

#extract uppercase letters
insight=''.join([c for c in challenge if c.isupper()])
print(insight)

#replace the zeros and ones in the numerical representation
insight = insight.replace('ZERO', '0')
insight = insight.replace('ONE', '1')
print(insight)

#let see the length
print(len(insight))

#since it is a multiple of 8, we can think that this is a series of
#ascii characters
result=''.join(chr(int(insight[i*8:i*8+8],2)) for i in range(len(insight)//8))
print(result)
# And the flag is reached: BITSCTF{h1d3_1n_pl41n_5173}