def words_check(text):
    res = {}
    text = text.split()
    for item in text:
        item = item.split(' ')
        for word in item:
            length = len(word) / 2
            cnt = 0
            for ch in word:
                if ch.isalpha() is False:
                    cnt += 1
                    word = word.replace(ch, '')
            if 0 <= cnt < length:
                word = word.title()
                if word in res:
                    res[word] += 1
                else:
                    res[word] = 1
    return res


# Local Test
print(words_check("""HeLLLO_O My________________FRIEND
HOW ARE YOUUUUU?___?
I Don'T KNow Y_O_U_R_N_A_M_E yet !!!!!!!!"""))
# {'Hellloo': 1, 'How': 1, 'Are': 1, 'Youuuuu': 1, 'I': 1, 'Dont': 1, 'Know': 1, 'Yourname': 1, 'Yet': 1}
