from venv import create
from dictogram import Dictogram
from histogram import word_file, stochastic, histogram
import random

# word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose', 'doodle']



if __name__ == "__main__":
    test_markov = markov_chain(['one', 'fish', 'moose', 'one', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose'])
    # m = markov_chain(['i', 'like', 'cats', 'you', 'like', 'dogs', 'but', 'we', 'both', 'hate', 'trump'])
    test_sentence = create_sentence(test_markov)

    print(test_sentence)