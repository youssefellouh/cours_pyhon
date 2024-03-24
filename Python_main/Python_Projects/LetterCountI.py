def LetterCout(str):
    words = str.split(' ')
    max_word = ""
    max_count = 0
    for word in words:
        counts = {}
        for char in word:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        count = 0
        for k, v in counts.items():
            if v > 1:
                count += 1
        if count > max_count:
            max_count = count
            max_word = word
    if max_word == "":
        return -1
    else:
        return max_word

print(LetterCout("today, is the greatest day ever!"))
print(LetterCout("Aujourd'hui , c'est le plus grand jour de tous les temps"))
print(LetterCout("Bonjour tout le monde, je suis omar amrouss"))