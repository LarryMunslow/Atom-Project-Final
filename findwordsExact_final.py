# This program will search input text content and count the words that match
# positive and negative word lists

#
# open the postive and negative list files and store the data into a structure.
# The list will need to store the word and a count field. The count field is
# always a positive number.
# imports
import sys
import matplotlib as mpl
import re
#
# data structures and classes
# wordElement class.
class WordElement():
    "Stores word and count"
    def __init__(self, word, n):
        self.word = word
        self.count = n

    def __iter__(self):
        return iter(self.word)

    def increment_count(self):
        self.count +=1

# store for brutality words with count
brutality_word_count = []

# store for grief words with count
grief_word_count = []

# store for hopelessness words with count
hopelessness_word_count = []

# store for military words with count
military_word_count = []

# store for optimism words with count
optimism_word_count = []

# store for religious words with count
religious_word_count = []
#
# end of data structure definitions
#
def exact_match(phrase, word):
    b = r'(\s|^|$)'
    return re.match(b + word + b, phrase)

# variable to hold positive words and count field

# debug lines below to show word in lists
#for i in range(0,3):
#    print "%d: %s" % (i, negative_word_count[i].word)

# read brutality.rtf
pf = open('brutality.rtf')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    brutality_word_count.append(WordElement(data, 0))

# read grief.rtf
pf = open('grief.rtf')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    grief_word_count.append(WordElement(data, 0))

# read hopelessness.rtf
pf = open('hopelessness.rtf')
# loop reading each line
for i,line in enumerate(pf):
    data = line.strip()
    hopelessness_word_count.append(WordElement(data, 0))

# read military.rtf
pf = open('military.rtf')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    military_word_count.append(WordElement(data, 0))

# read optimism.rtf
pf = open('optimism.rtf')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    optimism_word_count.append(WordElement(data, 0))

# read religious.rtf
pf = open('religious.rtf')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    religious_word_count.append(WordElement(data, 0))


# search for a string
#searchfile('content.rtf', 'This')
pcontent = open('content.txt', 'rt')

# look for positive words first
#[findwrd(obj, line) for x, obj in enumerate(positive_word_count) for line
# in pcontent]
for line in pcontent:
    sentence_words = line.split()
    for wrd in sentence_words:
        wrd = wrd.strip('.,!?:;()_-')
        wrd = wrd.lower()
        for newobj in brutality_word_count:
            if exact_match(wrd, newobj.word) != None:
                newobj.increment_count()
        for newobj1 in grief_word_count:
            if exact_match(wrd, newobj1.word) != None:
                newobj1.increment_count()
        for newobj3 in hopelessness_word_count:
            if exact_match(wrd, newobj3.word) != None:
                newobj3.increment_count()
        for newobj5 in military_word_count:
            if exact_match(wrd, newobj5.word) != None:
                newobj5.increment_count()
        for newobj8 in optimism_word_count:
            if exact_match(wrd, newobj8.word) != None:
                newobj8.increment_count()
        for newobj9 in religious_word_count:
            if exact_match(wrd, newobj9.word) != None:
                newobj9.increment_count()

for obj in brutality_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

for obj in grief_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

for obj in hopelessness_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

for obj in military_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

for obj in optimism_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)

for obj in religious_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)


brutality_total_count = 0
grief_total_count = 0
hopelessness_total_count = 0
military_total_count = 0
optimism_total_count = 0
religious_total_count = 0

for obj in brutality_word_count:
    brutality_total_count += obj.count

print " Total Brutality word count is {0}".format(brutality_total_count)

for obj in grief_word_count:
    grief_total_count += obj.count

print " Total Grief word count is {0}".format(grief_total_count)

for obj in hopelessness_word_count:
    hopelessness_total_count += obj.count

print " Total Hopelessness word count is {0}".format(hopelessness_total_count)

for obj in military_word_count:
    military_total_count += obj.count

print " Total Military count is {0}".format(military_total_count)

for obj in optimism_word_count:
    optimism_total_count += obj.count

print " Total Optimistic word count is {0}".format(optimism_total_count)

for obj in religious_word_count:
    religious_total_count += obj.count

print " Total Religious count is {0}".format(religious_total_count)

#plot stuff
