import os
import time
import threading
from itertools import combinations
from itertools import permutations

def load_dictionary():
    # load word list
    path = os.getcwd() + "/python/words.txt"
    #path = "words.txt"
    word_file = open(path, "r")
    all_words = word_file.read()
    word_file.close()

    word_list = all_words.split('\n')    
    # make lower case
    for i in range(0, len(word_list)):
        word_list[i] = word_list[i].lower()

    return word_list

def check_word(tid, perm_all, word_list, found_word_list):
    #print("\nT = " + str(tid) + ", len = " + str(len(perm_all)))
    for perm in perm_all: 
        perm_word = "".join(perm)
        # check if word is in word list            
        if (perm_word in word_list):
            found_word_list.append(perm_word)
            #print (perm_word + " is in dictionary")
    #print(found_word_list)

def print_remove_redundant_word(found_word):       
    # remove redundant words
    found_word_cleaned = [*set(found_word)]
    found_word_cleaned.sort() # sorts normally by alphabetical order
    found_word_cleaned.sort(key=len, reverse=False) # sorts by descending length    
    for found_word in found_word_cleaned:
        print(found_word)

def word_connect_mt(string, start_num, end_num):
    word_list = load_dictionary()

    found_word1 = []
    found_word2 = []
    found_word3 = []
    found_word4 = []
    
    for num_letter in range(start_num, end_num + 1):
        # all combinations for a number of letters
        comb_letters_all = list(combinations(string, num_letter))

        for comb_letters in comb_letters_all:
            # all permutations
            perm_all = list(permutations(comb_letters))
            
            num_perm = len(perm_all)
            thr_size      = num_perm // 4
            thr_size_last = num_perm - (thr_size + thr_size + thr_size)            
            
            #print(num_letter, thr_size1, thr_size2, thr_size3, thr_size4, num_perm)
 
            t1 = threading.Thread(target=check_word, args=(1, perm_all[(0 * thr_size):(1 * thr_size)], word_list, found_word1,))
            t2 = threading.Thread(target=check_word, args=(2, perm_all[(1 * thr_size):(2 * thr_size)], word_list, found_word2,))
            t3 = threading.Thread(target=check_word, args=(3, perm_all[(2 * thr_size):(3 * thr_size)], word_list, found_word3,))
            t4 = threading.Thread(target=check_word, args=(4, perm_all[(3 * thr_size): num_perm     ], word_list, found_word4,))

            t1.start()
            t2.start()
            t3.start()
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
    
            found_word = found_word1 + found_word2 + found_word3 + found_word4
            
    print_remove_redundant_word(found_word)

        
def word_connect(string, start_num, end_num):
    word_list = load_dictionary()

    found_word = []

    for num_letter in range(start_num, end_num + 1):
        # all combinations for a number of letters
        comb_letters_all = list(combinations(string, num_letter))

        for comb_letters in comb_letters_all:
            #print("redundance check ", "".join(comb_letters))        

            # all permutations
            perm_all = list(permutations(comb_letters))
            check_word(0, perm_all, word_list, found_word)        

    print_remove_redundant_word(found_word)



if __name__ == "__main__":
    
    string = "glaehud"    
    
    start_time = time.perf_counter()
    word_connect(string, 3, len(string))
    end_time = time.perf_counter()
    print(start_time, end_time, end_time - start_time)    

    # MT is slower (https://blog.devgenius.io/why-is-multi-threaded-python-so-slow-f032757f72dc)
    # start_time = time.perf_counter()
    # word_connect_mt(string, 3, len(string))    
    # end_time = time.perf_counter()
    # print(start_time, end_time, end_time - start_time)    