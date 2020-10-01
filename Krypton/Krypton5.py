f1 = open("/home/dsammmy/Desktop/Online_practice/OverTheWire/krypton/krypton5/found1", "r")
f2 = open("/home/dsammmy/Desktop/Online_practice/OverTheWire/krypton/krypton5/found2", "r")
f3 = open("/home/dsammmy/Desktop/Online_practice/OverTheWire/krypton/krypton5/found3", "r")
f = open("/home/dsammmy/Desktop/Online_practice/OverTheWire/krypton/krypton5/krypton6", "r")

max_length = 15

#  creating ciphers.
cipher1 = ""
tokens1 = f1.read().split(" ")
for tok in tokens1 :
	cipher1 += tok

cipher2 = ""
tokens2 = f2.read().split(" ")
for tok in tokens2 :
	cipher2 += tok

cipher3 = ""
tokens3 = f3.read().split(" ")
for tok in tokens3 :
	cipher3 += tok

cipher = ""
tokens = f.read().split(" ")
for tok in tokens :
	cipher += tok

total_cipher = len(cipher1) + len(cipher2) + len(cipher3)
# using letter frequency
letter = "ETA"
found = False

for l in range(4, max_length) :
	key_len = l
	if found :
		break
	key_poss = []
	print("[+] Checking for key_length : "+str(l)+" ",end="")

	for k in range(key_len) :

		counter = []
		for i in range(26):
			counter.append([chr(i+65),0])

		# for cipher1
		offset = k
		frequence = []
		for i in range(26):
			frequence.append([chr(i+65),0])
	
		while offset<len(cipher1):
			p = ord(cipher1[offset])-65
			frequence[p][1] += 1
			offset += key_len

		frequence.sort(key = lambda x: x[1])
		frequence.reverse()
		counter[((ord(letter[0])-ord(frequence[0][0]))%26)][1] += frequence[0][1]
		counter[((ord(letter[1])-ord(frequence[1][0]))%26)][1] += frequence[1][1]
		counter[((ord(letter[2])-ord(frequence[2][0]))%26)][1] += frequence[2][1]

		#for cipher2
		offset = k
		frequence = []
		for i in range(26):
			frequence.append([chr(i+65),0])
	
		while offset<len(cipher2):
			p = ord(cipher2[offset])-65
			frequence[p][1] += 1
			offset += key_len

		frequence.sort(key = lambda x: x[1])
		frequence.reverse()
		counter[((ord(letter[0])-ord(frequence[0][0]))%26)][1] += frequence[0][1]
		counter[((ord(letter[1])-ord(frequence[1][0]))%26)][1] += frequence[1][1]
		counter[((ord(letter[2])-ord(frequence[2][0]))%26)][1] += frequence[2][1]

		# for cipher 3
		offset = k
		frequence = []

		for i in range(26):
			frequence.append([chr(i+65),0])
	
		while offset<len(cipher3):
			p = ord(cipher3[offset])-65
			frequence[p][1] += 1
			offset += key_len

		frequence.sort(key = lambda x: x[1])
		frequence.reverse()
		counter[((ord(letter[0])-ord(frequence[0][0]))%26)][1] += frequence[0][1]
		counter[((ord(letter[1])-ord(frequence[1][0]))%26)][1] += frequence[1][1]
		counter[((ord(letter[2])-ord(frequence[2][0]))%26)][1] += frequence[2][1]

		# checking key
		counter.sort(key = lambda x: x[1])
		counter.reverse()
		if ((counter[0][1]*key_len)/total_cipher) < 0.10 :
			break
		key_poss.append([counter[0][0], (counter[0][1]*key_len)/total_cipher])

	if len(key_poss)==l :
		print('True')
		found = True
	else:
		print("False")
	

key = ''
for i in range(len(key_poss)) :
	key += key_poss[i][0]
# [['Q', 0.1191], ['W', 0.1228], ['C', 0.1302], ['P', 0.1656], ['W', 0.1638], ['N', 0.1433], ['U', 0.1172], ['H', 0.1321], ['T', 0.1209]]
print("\n[+] KEy : "+key)
print("\n[+] Decrypting the cipher with key : " + key)
key = 'QWCPWNUHT'

plain_text = ''

for c in range(len(cipher)) :
	plain_text += chr((ord(key[c]) + ord(cipher[c])-130)%26 + 65)

print("[+] Plain text recieved : "+plain_text)