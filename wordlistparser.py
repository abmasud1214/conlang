wordFile = open("google-10000-english-usa.txt")
words = wordFile.readlines()
wordFile.close()

print(len(words))

counter = dict()

for word in words:
    if(counter.get(len(word) - 1) == None):
        counter[len(word) - 1] = 0
    counter[len(word) - 1] += 1

print(counter)