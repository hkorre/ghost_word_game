#!/usr/bin/env python3.5

DEBUG = True

FILEPATH = 'WORD.LST'


from treelib import Node, Tree
from word_list import Word_List

class Word_Tree:

    def __init__(self):
        self._tree = Tree()
        self._tree.create_node(0, 0)  # root node
        if DEBUG is True: print("class Word_Tree created.")


    def get_tree(self):
        return self._tree

    def add_word(self, word):
        for i in range(1, len(word)+1):
            if self._tree.contains(word[:i]) is False:
                if i == 1:
                    self._tree.create_node(word[:i], word[:i], parent=0)
                else:
                    self._tree.create_node(word[:i], word[:i], parent=word[:i-1])

    def remove_word(self, word):
        for i in range(len(word)+1, 1, -1):
            if self._tree.contains(word[:i]) is True:
                wNode = self._tree.get_node(word[:i])
                if wNode.is_leaf() is True:
                    self._tree.remove_node(word[:i])


## TESTS ##

def Test_1():
    print ("class Word_Tree: running Test_1.")
    wtree = Word_Tree()

def Test_2(word):
    print ("class Word_Tree: running Test_2.")
    wtree = Word_Tree()
    wtree.add_word(word)
    tree = wtree.get_tree()
    tree.show()

def Test_3():
    print ("class Word_Tree: running Test_3.")
    wtree = Word_Tree()
    wtree.add_word('hasan')
    wtree.add_word('korre')
    wtree.add_word('hamburger')
    tree = wtree.get_tree()
    tree.show()

def Test_4():
    print ("class Word_Tree: running Test_4.")
    wtree = Word_Tree()
    wtree.add_word('hasan')
    wtree.add_word('hamburger')
    wtree.remove_word('hasan')
    tree = wtree.get_tree()
    tree.show()

if __name__ == "__main__":
    Test_1()
    Test_2('zym')
    Test_3()
    Test_4()


