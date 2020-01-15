import re
f = open("random text.txt","r")
contents = f.read()
words = re.split("[. ]",contents)
words_length = len(words)
consonants="BDGHJLMNPQSTVXZ"
for x in range(words_length):
    letters = words[x].count("f") + words[x].count("c") + words[x].count("k") + words[x].count("r")
    number_of_consonants = sum(words[x].count(c) for c in consonants)
    if letters > number_of_consonants:
        print("Η λέξη είναι κακή")
    else:
        print("Η λέξη είναι καλή")
f.close()
