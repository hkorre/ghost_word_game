#!/usr/bin/env python2.7

DEBUG = True

FILEPATH = 'WORD.LST'



class Word_List:

    def __init__(self):
        self._list = open(FILEPATH).read().splitlines()
        if DEBUG is True: print("class Word_List created.")

    def get_sublist(self, fragment):
        if DEBUG is True: print("Word_List: getting sublist of fragment = " + fragment)
        sublist = []
        for word in self._list:
            if word.startswith(fragment) and word != fragment:
                sublist.append(word) 
        return sublist

    def is_word(self, fragment):
        if fragment in self._list:
            if DEBUG is True: print(fragment + ' is in the word list!')
            return True
        else:
            if DEBUG is True: print(fragment + ' is not in the word list.')
            return False

    def is_wordOfFour(self, fragment):
        if self.is_word(fragment):
            if len(fragment) >= 4:
                if DEBUG is True: print(fragment + ' length >= 4!')
                return True
            else:
                if DEBUG is True: print('OK. ' + fragment + ' length less than 4')
                return False
        else:
            return False


## TESTS ##

def Test_1():
    print ("class Word_List: running Test_1.")
    words = Word_List()

def Test_2(fragment):
    print ("class Word_List: running Test_2.")
    words = Word_List()
    sublist = words.get_sublist(fragment)
    print("sublist...")
    print sublist

def Test_3():
    print ("class Word_List: running Test_3.")
    words = Word_List()
    words.is_word('hysteric')

if __name__ == "__main__":
    Test_1()
    Test_2('zym')
    Test_3()


