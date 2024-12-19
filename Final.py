# Emmalyn Holmquist
# 12/14/2024
# CPSC 507
# Final

## Problem 1a

# Define a function called number of duplicates which will take as input a Numpy array A and will return the number of
# elements in A such that the element occurs more than once in the array. Note that if an element occurs more than once,
# each instance of the element should be counted. So, if the input array contained 1,2,3,4,1, the function would return 2.
# Assume that the array contains integer values and that it is one dimensional. You may only use Numpy functionality
# in the function. In particular, you may not use any loops. Your code will need to be able to deal with large arrays.

#import numpy library
import numpy as np

def number_of_duplicates(array):
    #this function returns a list of the unique values and the counts of each unique value. doc - https://numpy.org/doc/stable/reference/generated/numpy.unique.html
    uniques, counts = np.unique(array, return_counts = True)
    #this function will give us the max of the counts returned from above
    #doc - https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max
    max_duplicates = np.max(counts)
    #return the max duplicates
    return max_duplicates

# #test
# array = np.array([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7])
# total_duplicates = number_of_duplicates(array)
# print(total_duplicates)

## Problem 1b

# Define a function called most consecutive which will take as input a list of integers L and which returns the length
# of the longest run of consecutive digits that can be constructed from the elements of L. For L = [6,2,5,3,0,10,1,9,8],
# the function would return 4 since it contains the consecutive numbers 0,1,2,3 and no longer sequence can be created.
# Assume that L does not contain any duplicates.

def most_consecutives(list):
    list = sorted(list) #sort list - doc - https://docs.python.org/3/howto/sorting.html

    #initialize first element of list
    num1 = list[0]
    #intialize highest consecutives count
    highest_consec = 0
    #initialize current consecutives count
    consec = 1

    #go through each element in list to check for consecutives, starting from second element
    for num2 in list[1:]:

        #if current element == previous + 1, they are consecutive
        if num2 == num1 + 1:
            consec += 1

        else:
            # if we have reached end of consecutive sequence, then see if the amount of consecs is greater than our highest consecs
            if consec > highest_consec:
                highest_consec = consec
                consec = 1  # reset consec count
            else:
                #if it is not higher, then just reset the consec seq num
                consec = 1

        #make previous num current num
        num1 = num2
    #account for if the highest consecutive sequence was the ending sequence (the above only accounts for when a sequence is "terminated"
    #by a number that is not in sequence
    if consec > highest_consec:
        return consec
    else:
        return highest_consec

# #test
# L = [6,2,5,3,0,10,1,9,8,11,12,13]
# total_consec = most_consecutives(L)
# print(total_consec)

## Problem 2

# Referencing the file docword.nytimes.txt answer the following questions. Store your answers in the variables provided.
# (a) How many documents contain more than 500 words?
# (b) How many documents contain more than 100 unique words?
# (c) How many words occur in more than 1000 documents?
# (d) What is the id of the word that appears the most times across all documents?
# (e) What is the average number of total words per document?


#a - How many documents contain more than 500 words?

#load data set and store in variable
nytimes = open("docword.nytimes.txt", "r")

#define a function to count every doc that has word count over 500
def count_words(file):
    #initialize the previous doc ID
    prev_doc = 1
    #intialize the word count
    word_count = 0
    #initialize a dictionary for storing word counts (for use in a later part, will use to compute average)
    dict_word_counts = {}
    #initialize docs with over 500 count
    docs_over_500 = 0
    #initialize count of all docs - for computing average later
    total_docs = 0

    #go through each line of the file
    for line in file:
        #split the line into a list
        curr_line = line.split()

        # this condition is necessary because our first 3 lines of each file will only contain one num
        # and contain info about the data overall, not about a certain doc
        if len(curr_line) == 3:

            #if the doc id is the same as the previous doc id
            if int(curr_line[0]) == prev_doc:
                #incrememnt the word count
                word_count += int(curr_line[2])

            #if the doc id does not equal the previous doc id
            elif int(curr_line[0]) != prev_doc:
                #we have reached the end of the word count for that doc.

                # If the word count is greater than 500, increment 500 count
                if word_count > 500:
                    docs_over_500 += 1

                #add to dictionary
                dict_word_counts[prev_doc] = word_count
                #reset word count to 1 (because we are starting at first word of next doc)
                word_count = int(curr_line[2])
                #increment doc count
                total_docs += 1
                #increment the prev doc (we move on to the next doc)
                prev_doc = int(curr_line[0])

    #we need to account for last doc in data set now. see if its a higher word count
    if word_count > 500:
        docs_over_500 += 1

    #add to dictionary
    dict_word_counts[prev_doc] = word_count
    total_docs += 1
    #return the highest doc name and the highest num words once we have gone through whole file
    return docs_over_500, dict_word_counts, total_docs

docs_over_500, dict_word_counts, total_docs=count_words(nytimes)

print("\n")
print("The number of documents with more than 500 words is ",docs_over_500,".")

nytimes.close()

# b - How many documents contain more than 100 unique words?

#load data set and store in variable
nytimes = open("docword.nytimes.txt", "r")

def unique_counts(file):
    #initialize the previous doc ID
    prev_doc = 1
    #initialize the count of docs with more than 100 uniques
    unique_over_100 = 0
    #initialize count for current unique words
    curr_unique = 0
    #initialize dict for unique words of current doc
    dict_curr_uniques={}

    #go through each line of the file
    for line in file:
        #split the line into a list
        curr_line = line.split()

        # this condition is necessary because our first 3 lines of each file will only contain one num
        # and contain info about the data overall, not about a certain doc
        if len(curr_line) == 3:
            #if the doc id is the same as the previous doc id
            if int(curr_line[0]) == prev_doc:

                #check if the current word is in our current dictionary
                if int(curr_line[1]) not in dict_curr_uniques:
                    #if its not, add it. we don't need to do anything to it if its already in it
                    dict_curr_uniques[int(curr_line[1])] = 1
                    curr_unique += 1 #increment count of uniques in current dictionary

            #if the doc id does not equal the previous doc id- we are at a new one
            elif int(curr_line[0]) != prev_doc:
                #see if the amount of uniques is higher than 100
                if curr_unique > 100:
                    unique_over_100 += 1

                #reset dict and add current line
                dict_curr_uniques = {}
                dict_curr_uniques[int(curr_line[1])] = 1

                #reset curr unique count
                curr_unique = 1

                #adjust the prev_doc variable to be the doc of the current line (new doc)
                prev_doc = int(curr_line[0])

    #account for last doc in data set now
    # find the total amount of uniques in current dict
    if curr_unique > 100:
        unique_over_100 += 1

    #return the highest doc name and the highest num words once we have gone through whole file
    return unique_over_100

unique_over_100 = unique_counts(nytimes)
print("The number of documents with over 100 unique words is ",unique_over_100,".")

nytimes.close()

# c - How many words occur in more than 1000 documents? && d - what is the id of the word that appears the most times across all docs?

#load data set and store in variable
nytimes = open("docword.nytimes.txt", "r")

#for this one, we will make a function that addresses both b and c. we will make a nested dictionary with following format:
# nested_dict = {
#     word_id: {
#         "num_docs": ###,
#         "num_occurences": ####
#     }

def count_occurences(file):
    # initialize the previous doc ID
    prev_doc = 1
    # initialize nested dict
    nested_dict = {}

    # go through each line of the file
    for line in file:
        # split the line into a list
        curr_line = line.split()

        # this condition is necessary because our first 3 lines of each file will only contain one num
        # and contain info about the data overall, not about a certain doc
        if len(curr_line) == 3:
            #set word id
            word_id = curr_line[1]

            #if the current word is not in the nested dict, add it
            if word_id not in nested_dict:
                nested_dict[word_id] = {}
                nested_dict[word_id]["Num Docs"] = 1
                nested_dict[word_id]["Num Occur"] = int(curr_line[2])

            #if word is already in dict, increment the occurences
            elif word_id in nested_dict:
                #increment occurences
                nested_dict[word_id]["Num Occur"] += int(curr_line[2])
                # if the doc id is not the same as the previous doc id, increment num docs its in
                if int(curr_line[0]) != prev_doc:
                    nested_dict[word_id]["Num Docs"] += 1

                    # adjust the prev_doc variable to be the doc of the current line (new doc)
                    prev_doc = int(curr_line[0])


    #now that we have found the num occurrences and num docs that each word is in, go through each word and find out:
    #c) how many words are in more than 1000 docs?
    #d) what is the id of the word that appears the most times across all docs?

    #initialize count of highest occurences
    highest_occur = 0
    #initialize count of words in more than 1000 docs
    total_over_1000 = 0
    #initialize doc id
    greatest_word_id = 1

    for key, value in nested_dict.items():
        for inner_key, inner_value in value.items():
            if inner_key == "Num Occur" and inner_value > highest_occur:
                highest_occur = inner_value
                greatest_word_id = key
            if inner_key == "Num Docs" and inner_value > 1000:
                total_over_1000 += 1

    return total_over_1000, greatest_word_id

total_over_1000, greatest_word_id = count_occurences(nytimes)
print("The word with the most amount of occurrences across all docs had ID ",greatest_word_id,".")
print("The number of words that are in over 1000 documents is",total_over_1000,".")

nytimes.close()

# e -  What is the average number of total words per document?

#sums the values
total_words = sum(dict_word_counts.values())
average = int(total_words/total_docs)

print("The average number of total words per doc is ",average,".")






