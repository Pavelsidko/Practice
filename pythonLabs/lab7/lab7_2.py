n = int(input())
dictionary = {}
for i in range(n):
    line = input().split(" - ")
    english_word = line[0]
    latin_words = line[1].split(", ")
    for latin_word in latin_words:
        if latin_word not in dictionary:
            dictionary[latin_word] = []
        dictionary[latin_word].append(english_word)

sorted_latin_words = sorted(dictionary.keys())
print(len(sorted_latin_words))
for latin_word in sorted_latin_words:
    english_words = sorted(dictionary[latin_word])
    print(latin_word + " - " + ", ".join(english_words))