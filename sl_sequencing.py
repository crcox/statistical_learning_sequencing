#!/usr/bin/env python

# imports for this module
import numpy as np
import random
from collections import Counter
import pandas as pd
from itertools import permutations, chain

def get_random_except(excluded_numbers, numbers):
    """Return a random number from the second list, excluding numbers in the given first list."""
    choices = [x for x in numbers if x not in excluded_numbers]
    if not choices:
        raise ValueError("No numbers left to choose from after excluding the given numbers.")
    return random.choice(choices)

def count_numbers(lst):
    """function used for verifying answers and correct number counts at the end"""
    counts = Counter(lst)
    for number, count in sorted(counts.items()):
        print(f"{number}: {count}")

def count_sublist(main_list, sublist):
    """function used for verifying answers and correct transition counts at the end"""
    count = 0
    sublist_length = len(sublist)

    for i in range(len(main_list) - sublist_length + 1):
        if main_list[i:i + sublist_length] == sublist:
            count += 1
    return count

class Sequence:
    """Class for creating valid sequences for statistical learning paradigms.

    Parameters
    ----------
    total: int
        Entire length of sequence

    vector_size: int
        Your vector size. This will serve as your maximum vector value in a non-zero indexed vector
    
    """

    def __init__(self, total, vector_size):

        # check that total sequence length and vector length are compatible
        if total % vector_size != 0:
            raise ValueError(f'{vector_size} must be a factor of {total}\n+\
                             try vector_size = {vector_size + 1} or {vector_size - 1}\n +\
                                ')
        else:
            self.total = total
            self.vector_size = vector_size

        # initialize other attributes
        self.n_perms = len(list(permutations(np.linspace(0, vector_size-1, vector_size), 2))) # total transitions 
        self.indiv_perms = self.total/self.n_perms # maxmimum times total transition will occur in sequence of length defined by total

    # method to sequence the data
    def sequence(self):
        """Create valid sequence that satisfies: 
        1) no repeats
        2) equal observations of values in vector
        3) equal observations of possible transitions


        Parameters
        ----------
        self: self
        
        """
        np.random.seed(101)
        # functions for sequencing
        
        self.possible_nums = range(1,self.vector_size+1)

        try_count = 0
        while(True):
            valid_sequence = []
            start = np.random.randint(1, self.vector_size+1)

            # dictionary for measuring the amount of times each transition has occured
            self.tally_tracker = {i: {j: 0 for j in self.possible_nums if j != i} for i in self.possible_nums}

            try_count += 1
            print(f'number of times tried: {try_count}')

            for i in range(self.total):
                excluded_numbers = [start]
                #  loop to make sure we don't allow one transition (e.g. 6 -> 10) too many times
                for possible_transition in self.tally_tracker[start].keys():
                    if self.tally_tracker[start][possible_transition] >= self.indiv_perms:
                        excluded_numbers.append(possible_transition)

                try:
                    candidate_number = get_random_except(excluded_numbers, self.possible_nums)
                except:
                    break # do this break when we accidentally (randomly) exhaust all possible options for transitions

                # update the dicitonary so that we know not to use this transition again
                self.tally_tracker[start][candidate_number] += 1

                valid_sequence.append(candidate_number)
                start = candidate_number
            if len(valid_sequence) == self.total:
                break # this means we got to the end length successfully, while using the perfect number of transitions)

        print('Sequence achieved')
        self.valid_sequence = valid_sequence
        return self
    
    def validate(self):
        '''Display sequence validations
        '''
        print(f'total length of list: {len(self.valid_sequence)}\n')

        print('Checking transition counts: ')
        for i in self.possible_nums:
            print(f'Transition counts from {i}: {self.tally_tracker[i]}')

        print('\nDouble Checking transition counts (with different method): ')
        for i in self.possible_nums:
            print(f'Transition counts for {i}: ')
            remade_dict_of_transitions = {}
            for j in self.possible_nums:
                if j==i:
                    continue
                sublist = [i,j]
                remade_dict_of_transitions[j] = count_sublist(self.valid_sequence, sublist)
            for k in remade_dict_of_transitions.keys():
                print(f'     There were {remade_dict_of_transitions[k]} transitions to {k}: ')

        print('\nChecking number counts: ')
        count_numbers(self.valid_sequence)

    def save_csv(self, filename):
        '''Save sequence as .csv file

        Parameters
        ----------
        filename: str
            String filename (will save to current directory) or absoulte path
        
        '''
        # check 

        if not filename.endswith('.csv'):
            raise ValueError(f'You must include the .csv extension\n+\
                                Example: {filename + ".csv"}')

        # make into pandas DF
        d = pd.DataFrame(self.valid_sequence)
        d.to_csv(filename)

    def match(self, inpt, unlist=False):
        '''Match/replace indices with a specific value to a corresponding value
        
        Parameters
        ----------
        inpt: dict
            Input dictionary. Keys represent current observances in indices, values are what you
            wish to replace the indices with. 

        unlist: bool, default: False
            If you are inputing a nested dictionary and wish to unlist

        Example
        -------
        inpt = {
            1: 'm',
            2: 'p'
            3: 'j'
        }

        X = sls.Sequence(total=60, vector_size=3)
        X.sequence()
        X.match(inpt=inpt) # will create a new sequence where values 1 are replaced with 'm', 2 is replaced with 'p' and 3 is replaced with 'j'

        '''
        self.inpt = inpt
        # check for errors
        if len(self.inpt) != self.vector_size:
            raise ValueError('Dictionary size must be the same length as vector_size')
        
        match_sequence = []
        for j in self.valid_sequence:
            for i in self.inpt:
                if i == j:
                    match_sequence.append(self.inpt[i])

        # unlist if necessary
        if unlist == True:
            match_sequence = list(chain.from_iterable(match_sequence))

        self.match_sequence = match_sequence
        return self
    
    def save_match_csv(self, filename):
        '''Save match sequence as .csv file

        Parameters
        ----------
        filename: str
            String filename (will save to current directory) or absoulte path
        
        '''
        # check 

        if not filename.endswith('.csv'):
            raise ValueError(f'You must include the .csv extension\n+\
                                Example: {filename + ".csv"}')

        # make into pandas DF
        d = pd.DataFrame(self.match_sequence)
        d.to_csv(filename)