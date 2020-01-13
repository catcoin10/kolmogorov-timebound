# Kolmo v1.1
# New feature: loop code using search() function which in turn calls run()
# Syntax: multi.py start
import base64, binascii, timeout_decorator, sys

@timeout_decorator.timeout(5)
def n_to_b85_mod(n):
	if (len(hex(n)) % 2) == 1:	n *= 16 # have no choice
	w = str(binascii.unhexlify(hex(n)[2:].encode()))[2:-1]
	x = base64.b85encode(w.encode())
	y = str(x)[2:-1]
	z = ""
	items = [';', '?', '~', 'q', '#'] # I assume these will be the least important
	Items = ['print', '\n', ' ', '(', ')'] # could use a dictionary being lazy, words/characters
	for i in y:
		if i not in items:	z += i
		else:
			for j in range(1):
				if items[j] == i:	z += Items[j]
	return z

def run(i):
	while True:
		try:
			i += 1
			exec(n_to_b85_mod(i))
			return i
		except:	continue

xe = int(sys.argv[1])

def search(xe):
	while True:
		xe = run(xe)
		if "(" in n_to_b85_mod(xe):
			print([xe,n_to_b85_mod(xe)])

print(search(xe))
