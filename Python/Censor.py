def censor(text, word):
    word2 = text.split()
    out = ""
    for a in range(len(word2)):
        if word2[a] == word:
            word2[a] = "*"*len(word2[a])
        out += word2[a]
        if a != len(word2)-1:
            out += " "
    return out