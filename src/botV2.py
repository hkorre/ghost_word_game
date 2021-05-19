#!/usr/bin/env python2.7

import random
from word_list import Word_List
from word_tree import Word_Tree


DEBUG = True


class BotV2:

    def __init__(self, _user_id, _num_players):
        self.user_id = _user_id  #starts at 1, not 0
        self.num_players = _num_players
        self.wordList = Word_List()
        self.wordTree = None
        if DEBUG is True: print("Bot #" + str(self.user_id) + " created.")

    def _display_tree(self):
        self.wordTree.show_tree()
        self.wordTree.show_treeData()
        self.wordTree.show_treePercent()

    def _get_random(self, _sublist):
        idx = random.randint(0, len(_sublist)-1)
        return _sublist[idx]

    def pick_letter(self, _fragment):
        print("Bot #" + str(self.user_id) + ": Picking letter...")
        solution = None

        if DEBUG is True: print("  fragment = " + _fragment)
        sublist = self.wordList.get_sublist(_fragment)
        if DEBUG is True: print("  There are " + str(len(sublist)) + " words to chose from.")

        # create tree (if needed)
        if self.wordTree == None:
            self.wordTree = Word_Tree()
            self.wordTree.add_sublist(sublist)
            self.wordTree.label_tree(0, self.num_players, self.user_id)

        while solution == None:
            # check if any path is an automatic win...
            if len(self.wordTree.get_winOptions(_fragment)) != 0:
                winOptions = self.wordTree.get_winOptions(_fragment)
                print ('winOptions = ' + str(winOptions))
                solution = self._get_random(winOptions)

            # check if we can find an unknown path with highest win percentage...
            elif len(self.wordTree.get_highestUnknown(_fragment)) != 0:
                highestUnknown = self.wordTree.get_highestUnknown(_fragment)
                solution = highestUnknown[0]

            # find longest losing path...
            else:
                solnList = self.wordTree.get_longestLoss(_fragment)
                solnWord = self._get_random(solnList)
                if len(solnWord) > len(_fragment):
                    solution = solnWord[len(_fragment)]
                else:
                    solution = ''

            newFragment = _fragment + solution

            # check if the answer is a word...
            if self.wordList.is_wordOfFour(newFragment):
                print('solution - ' + solution + ' is invalid!')
                self.wordTree.remove_node(newFragment)
                solution = None
                continue

            # check if path leads to a word of length < 4...
            sublist = self.wordList.get_sublist(newFragment)
            if len(sublist) == 1 and len(sublist[0]) < 4:
                print('solution - ' + solution + ' is invalid!')
                self.wordTree.remove_node(newFragment)
                solution = None
                continue


        return solution



## TESTS ##

def Test_1(num_bots):
    print('\n')
    print ("class Bot: running Test_1.")
    bot_list = []
    for i in range(num_bots):
        bot_list.append(BotV2(i, num_bots))

def Test_2(fragment):
    print('\n')
    print ("class Bot: running Test_2.")
    bot = BotV2(1, 3)
    letter = bot.pick_letter(fragment)
    bot._display_tree()
    print('Bot picked the letter ' + letter)


if __name__ == "__main__":
    Test_1(2)
    #Test_2('zym')
    Test_2('has')


