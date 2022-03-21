"""Count words in file."""
# put your code here.


def word_count(file):
    file = open(file)
    word_dict = {}
    for line in file:
        line = line.rstrip()
        words = line.split(" ")
        
        #print(words)
        
        for word in words:
            #if word_dict.get(word, 0) == 0:
                #word_dict[word] = 1

            word_dict[word] = word_dict.get(word, 0) +1
    
    #print(word_dict)

    for key, value in word_dict.items():
        print(f'{key} {value}')

word_count("test.txt")
