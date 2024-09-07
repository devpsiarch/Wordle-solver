import random
from english_words import get_english_words_set
import sys

all_words = get_english_words_set(['web2'], lower=True)
possible_words = [word for word in all_words if len(word) == 5]

#best words to start of with according to math and gpt
starters = ["crane","slate","raise","least","trite"]

#crane => c.r^a=n.e. this is an example of the kind of notation we will be using to denote the start if the chars

guess = random.choice(starters)
print(f"starter guess ==> {guess}")

def parse_output(string,words):
    i = 0
    while i < len(string):
        char = string[i]
        sign = string[i+1]
        match sign:
            case "^":
                words = [word for word in words if word[int(i/2)] == char]
            case ".":
                words = [word for word in words if char not in word]
            case "=":
                words = [word for word in words if char in word and word[int(i/2)] != char]
            case "*":
                words = [word for word in all_words if len(word) == 5]
        print(f"{string[i]} is {string[i+1]}")
        i += 2
    return words
#6 only tries in wordle
while True:
    result = str(input("result ==>"))
    possible_words = parse_output(result,possible_words)
    print(possible_words)
