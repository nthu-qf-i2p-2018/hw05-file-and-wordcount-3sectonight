# -*- coding: utf-8 -*-
def main(filename):
    # read file into lines
    lines = open(" i_have_a_dream.txt").readlines()

    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        line = line.strip()
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word = word.strip(string.punctuation)
            all_words.append(word)
            # check if word is not empty
                

    # compute word count from all_words
    from collections import Counter
    word_counter = Counter(all_words)
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    import csv
    with open('word_count.csv', 'w') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(word_counter.most_common())
        
    import json    
    json.dump(word_counter.most_common(), open('word_counter.json', 'w')) 
    
    import pickle
    pickle.dump(word_counter.most_common(), open('word_counter.json', 'w'))
