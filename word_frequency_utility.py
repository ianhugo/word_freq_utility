import re

f = open("/Users/ianyuen/Documents/GitHub/mpcs50101-2020-autumn-assignment-3-pirateontheseas/speech.txt", 'r')

glossary = {}

#function to remove punctuation
def remove_punc(word):
    punctuations = '''!()-[]{};:“'”"\"\,<>./?@#$%^&*_~'''
    no_punct_str = ""
    for char in word:
        if char not in punctuations:
            no_punct_str = no_punct_str + char
    return no_punct_str        


#preparing the string
for line in f:
    t = line.strip()
    x = str(t)
    y = x.lower()
    e = remove_punc(y)
    z = e.split(" ")

    #looping through string that is now list of words, adding to glossary

    for j in z:
        try:
            glossary[j] += 1
        except KeyError:
            glossary[j] = 1
        
#write to file

t = open("/Users/ianyuen/Documents/GitHub/mpcs50101-2020-autumn-assignment-3-pirateontheseas/word_count.txt", "x")

#formating the output
for key, value in glossary.items():
    t.write(str(key) + " - " + str(value) +" \n")




f.close
t.close
