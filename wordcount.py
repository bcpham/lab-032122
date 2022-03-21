"""Count words in file."""


# put your code here.
def word_count(file):
    file = open("test.txt")
    for line in file:
        words = line.split(" ")

        print(words)

word_count("test.txt")