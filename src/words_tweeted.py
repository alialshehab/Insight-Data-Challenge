def main():
    f = open('tweet_input/tweets.txt')

    word_dict = {} # Dictionary that will hold all the uniques words as keys
                   #    and the number of their occurances as values
    len_longest_word = 0 #Used for output formating

    for line in f:
        # Find the list of words in each line
        list_of_words = line.split()

        # If the word is not in the dictionary add it and if it is increment
        #    the value
        for word in list_of_words:
            if len(word) > len_longest_word:
                len_longest_word = len(word)
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    #Sort the words in the dictionary 
    sorted_words = sorted(word_dict)
    nf = open('tweet_output/ft1.txt', 'w') 
    for w in sorted_words:
        #Write to file with specific format
        nf.write(w.ljust(len_longest_word+6) + str(word_dict[w]) + '\r\n')
    nf.close()
    f.close()

if __name__ == "__main__":
    main()
