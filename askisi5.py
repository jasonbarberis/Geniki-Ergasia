def split_str(x):
    return [ch for ch in x]

import re
f = open("random text.txt","r")
contents = f.read()
words = re.split("[. ]",contents)
words_length = len(words)
for x in range(words_length):
    if len(words[x]) > 3:
        char = split_str(words[x])
        a = char[0]
        char.remove(char[0])
        char.append(a)
        char.append("ay")
        print (char)

f.close()
