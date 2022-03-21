"""Count words in file."""


# put your code here.
def word_count(file):
    file = open("test.txt")
    word_dict = {}
    for line in file:
        line = line.rstrip()
        words = line.split(" ")
        
        #print(words)
        for word in words:
            if word_dict.get(word, 0) == 0:
                word_dict[word] = 1

    print(word_dict)
word_count("test.txt")
#word_dict[word] = word_dict.get(word, 0) +1