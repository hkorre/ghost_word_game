#!/usr/bin/env python2.7

import random
from word_list import Word_List


DEBUG = True


class Bot:

    def __init__(self, _num):
        self.num = _num
        self.wordList = Word_List()
        if DEBUG is True: print("Bot #" + str(self.num) + " created.")

    def _is_evenPlayer(self, _fragment):
        frag_len = len(_fragment)
        if (frag_len % 2) == 0:
            if DEBUG is True: print("  Bot is the odd player.")
            return False
        else:
            if DEBUG is True: print("  Bot is the even player.")
            return True

    def _get_sublistOdd(self, _sublist):
        if DEBUG is True: print("  Getting odd-legnth word list.")
        odd_list = []
        for word in _sublist:
            if (len(word) % 2) != 0:
                odd_list.append(word) 
        return odd_list
        

    def _get_sublistEven(self, _sublist):
        if DEBUG is True: print("  Getting even-legnth word list.")
        even_list = []
        for word in _sublist:
            if (len(word) % 2) == 0:
                even_list.append(word) 
        return even_list

    def _get_wordRandom(self, _sublist):
       idx = random.randint(0, len(_sublist)-1)
       return _sublist[idx]

    def _get_wordLongest(self, _sublist):
        max_length = 0
        choices = []
        for word in _sublist:
            if len(word) > max_length:
                max_length = len(word)
                choices = []
                choices.append(word)
            elif len(word) == max_length:
                choices.append(word)
        idx = random.randint(0, len(choices)-1)
        return choices[idx]


    def pick_letter(self, _fragment):
        print("Bot #" + str(self.num) + ": Picking letter...")

        if DEBUG is True: print("  fragment = " + _fragment)
        sublist = self.wordList.get_sublist(_fragment)
        if DEBUG is True: print("  There are " + str(len(sublist)) + " words to chose from.")

        is_evenPlayer = self._is_evenPlayer(_fragment)
        if is_evenPlayer:
            win_list = self._get_sublistOdd(sublist)
            lose_list = self._get_sublistEven(sublist)
        else:
            win_list = self._get_sublistEven(sublist)
            lose_list = self._get_sublistOdd(sublist)

        goal_word = None
 
        while goal_word is None:
            if len(win_list) > 0:
                goal_word = self._get_wordRandom(win_list)
                if goal_word == _fragment:
                    win_list.remove(goal_word)
                    goal_word = None
                else:
                    new_fragment = _fragment + goal_word[len(_fragment)]
                    if self.wordList.is_wordOfFour(new_fragment):
                        win_list.remove(goal_word)
                        goal_word = None
            elif len(lose_list) > 0:
                goal_word = self._get_wordLongest(lose_list)
                if goal_word == _fragment:
                    win_list.remove(goal_word)
                    goal_word = None
                else:
                    new_fragment = _fragment + goal_word[len(_fragment)]
                    if self.wordList.is_wordOfFour(new_fragment):
                        lose_list.remove(goal_word)
                        goal_word = None
            else:
                break

        if goal_word is not None:
            if DEBUG is True: print("  goal_word = " + goal_word)
            return goal_word[len(_fragment)]

        if DEBUG is True: print("  No goal_word found!")
        return None




## TESTS ##

def Test_1(num_bots):
    print('\n')
    print ("class Bot: running Test_1.")
    bot_list = []
    for i in range(num_bots):
        bot_list.append(Bot(i))

def Test_2(fragment):
    print('\n')
    print ("class Bot: running Test_2.")
    bot = Bot(0)
    letter = bot.pick_letter(fragment)
    print('Bot picked the letter ' + letter)


if __name__ == "__main__":
    Test_1(2)
    Test_2('zym')


