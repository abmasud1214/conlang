import random
import json

letterFamilies = dict()
frequencyDict = {3: 672, 2: 396, 1: 26, 4: 1125, 5: 1386, 6: 1507, 11: 376, 7: 1464, 8: 1168, 9: 908, 10: 609, 13: 101, 12: 209, 14: 39, 15: 10, 18: 1, 16: 3}

letterFamilies["Vowel"] = ['a', 'e', 'i', 'o', 'u']
letterFamilies["C"] = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def generateWord(wordStructure):
    newWord = ''
    if(type(wordStructure) == str):
        wordStructure = wordStructure.split('/')

    for char in wordStructure:
        newWord += random.choice(letterFamilies[char])
    return newWord

print(generateWord('C/Vowel/C/Vowel/C'))
