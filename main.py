from gronsfeld import gronsfeld, GronsfeldKey, textutils

if __name__ == '__main__':
    best_score = 0
    ciphertext = 'DGMOINHGNUJDRYNUNHOIUENIFNIXXLAYPTMVHSNSFYLKROIYJTDJTCCULEYEVYRTGUA'.lower()
    expected_words = [
        'un',
        'deux',
        'trois',
        'quatre',
        'cinq',
        'six',
        'sept',
        'huit',
        'neuf',
        'dix',
        'cent'
        ]
    for key in range(0, 100000000):
        gkey = GronsfeldKey(str(key))
        cleartext = gronsfeld.decipher(ciphertext, gkey)
        score = textutils.score(cleartext, expected_words)
        if (key % 10000) == 0:
            print(str(key))
        if score > best_score:
            best_score = score
            print(str(score) + ': ' + cleartext + '(' + str(key) + ')')
    print('end')