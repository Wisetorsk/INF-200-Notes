
def translate_letter(input_letters): # string in, Returns list
	out = []
	a = 1
	b = 2
	c = 3
	d = 4
	e = 5
	f = 6
	g = 7
	h = 8
	i = 9
	j = 10
	k = 11
	l = 12
	m = 13
	n = 14
	o = 15
	p = 16
	q = 17
	r = 18
	s = 19
	t = 20
	u = 21
	v = 22
	w = 23
	x = 24
	y = 25
	z = 26
	for a in range(len(input_letters)):
		out.append(eval(input_letters[a]))
	return out

def translate_num(input_value): # list in, returns list
	letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	out = []
	for i in range(len(input_value)):
		for a in range(1,27):
			if input_value[i] == a:
				out.append(letter[a-1])
	return out

def print_func(list_letters):
	for a in range(len(list_letters)):
		if a == 0:
			out = list_letters[a]
		else:
			out += list_letters[a]
	print out

def return_states(state):
	if state > 26:
		state_r1 = state%26
		state_r2 = state/26
		if state_r2 > 26:
			state_r3 = state_r2/26
			state_r2 = state_r2%26
		else:
			state_r3 = 1
	elif state == 0:
		state_r1 = 1
		state_r2 = 1
		state_r3 = 1
	else: 
		state_r1 = state
		state_r2 = 1
		state_r3 = 1
	return [state_r1, state_r2, state_r3]
	
def encrypt(letter, state):
	key_start = state
	out = []
	for a in letter:
		state += 1
		state_rot = return_states(state)
		table_1 = r1[state_rot[0]]
		for k in range(26):
			if a == table_1[k][0]:
				out_1 = table_1[k][1]
		
		table_2 = r2[state_rot[1]]
		for k in range(26):
			if out_1 == table_2[k][0]:
				out_2 = table_2[k][1]
			
		table_3 = r3[state_rot[2]]
		for k in range(26):
			if out_2 == table_3[k][0]:
				out_3 = table_3[k][1]
		
		out.append(out_3)
	key_end = state
	return out, key_start, key_end

def encryption(string, state):
	values = translate_letter(string)
	enc_values, key_start, key_end = encrypt(values, state)
	print_str = translate_num(enc_values)
	print_func(print_str)
	print 'Start key: %s\nEnd key: %s\n' % (key_start, key_end)


r1 = {} # Rotor 1
for j in range(1,27):
	list = []
	for a in range(1,27):
		b = a-1+j
		if b > 26:
			b = b%26
		list.append([a, b])
	r1[j]=list

r2 = {} # Rotor 2
for j in range(1,27):
	list = []
	for a in range(1,27):
		b = a-1+j
		if b > 26:
			b = b%26
		list.append([a, b])
	r2[j]=list
	
r3 = {} # Rotor 3
for j in range(1,27):
	list = []
	for a in range(1,27):
		b = a-1+j
		if b > 26:
			b = b%26
		list.append([a, b])
	r3[j]=list
	


if __name__ == '__main__':
	encryption(raw_input('String: ').lower(), input('State: '))
	raw_input('')
