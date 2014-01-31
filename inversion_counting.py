#!/usr/bin/env python

import random
import math


def generate_array(size):
    temp_array = []
    for i in range(size):
        temp_array.append(i)
    random.shuffle(temp_array)

    return temp_array

def brute_force(array):
    pairs = []
    for j in range(len(array)):
        for k in range(j + 1, len(array)):
            if array[j] < array[k]:
                pairs.append((array[j], array[k]))

    return pairs

def naive_dnc(array):
    """Naive divide and conquer method for finding inversions"""
    size = len(array)

    # only split if we have enough to split
    if size < 2:
        return []

    al = array[:int(size/2)]
    ar = array[int(size/2):]

    # recursive calls
    pairs = []
    pairs.extend(naive_dnc(al))
    pairs.extend(naive_dnc(ar))

    # additional work for left and right halves
    for a in al:
        for b in ar:
            if a > b:
                pairs.append((a, b))

    return pairs



def main():
    n = 10 
    
    array = generate_array(n)
    
    print(array)
    
    bf = brute_force(array)

    print("Results bf: " + repr(bf))

    ndc = naive_dnc(array)

    print("Results naive_dnc: " + repr(ndc))

if __name__ == "__main__":
    main()
