f1 = open("/home/dsammmy/Desktop/Online_practice/OverTheWire/krypton/krypton4/found1", "r")
f2 = open("/home/dsammmy/Desktop/Online_practice/OverTheWire/krypton/krypton4/found2", "r")
f = open("/home/dsammmy/Desktop/Online_practice/OverTheWire/krypton/krypton4/krypton5", "r")

letter = "ETA"
cipher = ""
tokens = f.read().split(" ")
for tok in tokens :
	cipher += tok

key_len = 6
key_poss = []


for k in range(key_len):

	offset = k
	frequence = []

	for i in range(26):
		frequence.append([chr(i+65),0])
	
	while offset<len(cipher):
		p = ord(cipher[offset])-65
		frequence[p][1] += 1
		offset += key_len

	frequence.sort(key = lambda x: x[1])
	frequence.reverse()
	p1 = chr((ord(letter[0])-ord(frequence[0][0]))%26+65)
	p2 = chr((ord(letter[1])-ord(frequence[1][0]))%26+65)
	p3 = chr((ord(letter[2])-ord(frequence[2][0]))%26+65)
	key_poss.append([p1,p2,p3,frequence[0][1],frequence[1][1],frequence[2][1]])

#print(key_poss)

#[['V', 'B', 'C', 37, 24, 22], ['J', 'J', 'C', 35, 32, 19], ['W', 'W', 'I', 34, 30, 27], ['Q', 'S', 'X', 37, 26, 22], ['W', 'B', 'E', 32, 26, 24], ['C', 'C', 'O', 33, 20, 19]]
#[['V', 'A', 'C', 58, 37, 33], ['J', 'C', 'G', 38, 38, 33], ['H', 'L', 'I', 46, 45, 39], ['Q', 'Q', 'Q', 44, 41, 38], ['W', 'W', 'I', 52, 50, 30], ['C', 'C', 'O', 59, 40, 35]]

#key = "VJIQWC""VJWQWC"

# possible keys : 
key =["VJIQWC", "VJWQWC", "VJHQWC", "VJLQWC"]
plaintext = []

for k in range(len(key)):
	text = ""
	offset = 0
	for i in range(len(cipher)):
		offset %= 6
		p = chr((ord(key[k][offset])+ord(cipher[i])-130)%26 + 65)
		text += p
		offset += 1
	plaintext.append(text)

#print(plaintext)

#['CLQARTEXF', 'CLEARTEXT', 'CLPARTEXE', 'CLTARTEXI']

print(plaintext[1])  # the correct one