# analyser


def analyze(word):
	values = {}
	score = 0
	values['-'] = 0
	values["'"] = 0
	alphabet = ' ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
	alphabet = alphabet.split(',')
	for a in range(len(alphabet)):
		values[alphabet[a]] = a
	for b in word.strip().lower():
		for c in values:
			if b == c:
				score += values[c]
	return score

def main():
	word = raw_input('Word/sentence: ')
	score = analyze(word)
	if len(word.split()) != 1:
		print 'The sentence: "%s" gives a score of %.0f points!' % (word, score)
	else:
		print 'The word: "%s" gives a score of %.0f points!' % (word, score)

if __name__ == '__main__':
	main()