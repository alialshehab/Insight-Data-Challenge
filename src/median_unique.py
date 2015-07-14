'''
The script reads in a text file (tweets.txt)and calculates the median number 
of unique words per line and writes the updated median to an output file
(ft2.txt) as lines are read.

'''

from heapq import heappush, heappop
from math import trunc

def main():
    f = open('tweet_input/tweets.txt')
    nf = open('tweet_output/ft2.txt', 'w')

    lower_half = [] #max heap containing the lower half of tweet medians
    upper_half = [] #min heap containing the upper half of tweet medians

    for line in f:
        # Find the number of unique words in a line (tweet)
        no_unique_words = len(set(line.split()))
        
        # Distribute evenly between the two heaps such that the number of elements
        #   in lower_half is always >= upper_half by one element
        if len(lower_half) <= len(upper_half):
            heappush(lower_half, -no_unique_words)
        else:
            heappush(upper_half, no_unique_words)
            
        # If the largest element (median) in the lower_half is bigger than the
        #    the smallest element (median) in the upper_half fix it
        if upper_half != [] and -lower_half[0] > upper_half[0]:
            # Pop the smallest element in the upper_half and push it in lower_half
            heappush(lower_half, -heappop(upper_half))
            # Pop the largest element in the lower_half and push it in upper_half
            heappush(upper_half, -heappop(lower_half))
            
        # The median of a set with an even number of items is the mean of the two
        #     middle elements, which are: the largest element in lower_half and
        #     smallest element in upper_half
        if len(lower_half) > len(upper_half):
            nf.write(str(-lower_half[0]*1.0)+"\r\n")
        else:
            nf.write(str(trunc(((upper_half[0]-lower_half[0])/2.00)*100.0)/100.0)+'\r\n')

    nf.close()
    f.close()

if __name__ == "__main__":
    main()
