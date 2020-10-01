#!/usr/bin/python

key = 'EICTDGYIYZKTHNSIRFXYCPFUEOCKRN'
ct = 'PNUKLYLWRQKGKBE'
pt = ''

for i in range(len(ct)) :
	p = (ord(ct[i])-ord(key[i]))%26
	pt += chr(p+65)
	
print pt