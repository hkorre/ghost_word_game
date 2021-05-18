#!/usr/bin/env python3.5

DEBUG = True

FILEPATH = 'WORD.LST'


from treelib import Node, Tree


class Letter(object):
    def __init__(self, _result, _depth, _percent_win):
        self.result = _result
        self.depth = _depth
        self.percent_win = _percent_win

class Word_Tree:

    def __init__(self):
        self._tree = Tree()
        self._tree.create_node(0, 0)  # root node
        if DEBUG is True: print("class Word_Tree created.")


    def get_tree(self):
        return self._tree

    def show_tree(self):
        self._tree.show()

    def show_treeData(self):
        self._tree.show(data_property='result')

    def show_treePercent(self):
        self._tree.show(data_property='percent_win')

    def add_word(self, _word):
        for i in range(1, len(_word)+1):
            if self._tree.contains(_word[:i]) is False:
                if i == 1:
                    self._tree.create_node(_word[:i], _word[:i], parent=0)
                else:
                    self._tree.create_node(_word[:i], _word[:i], parent=_word[:i-1])

    def remove_word(self, _word):
        for i in range(len(_word)+1, 1, -1):
            if self._tree.contains(_word[:i]) is True:
                wNode = self._tree.get_node(_word[:i])
                if wNode.is_leaf() is True:
                    self._tree.remove_node(_word[:i])

    def remove_node(self, _fragment):
        self._tree.remove_node(_fragment)

    def add_sublist(self, _sublist):
        for word in _sublist:
            self.add_word(word)

    def _calc_winPercent(self, _node_id):
        wNode = self._tree.get_node(_node_id)
        percent_sum = 0.0

        children_ids = wNode.successors(self._tree.identifier)
        for child_id in children_ids:
            child = self._tree.get_node(child_id)
            percent_sum += child.data.percent_win

        return percent_sum/len(children_ids)

    def _label_recursion(self, _node_id, _count, _num_players, _user_id):
        wNode = self._tree.get_node(_node_id)

        # base case
        if wNode.is_leaf() is True:
            if (_count-1) % _num_players != (_user_id-1):
                wNode.data = Letter('win', _count, 1.0)
            else:
                wNode.data = Letter('loss', _count, 0.0)
            return

        # recursive call
        num_wins = 0
        num_losses = 0
        num_unknown = 0

        children_ids = wNode.successors(self._tree.identifier)
        for child_id in children_ids:
            self._label_recursion(child_id, _count+1, _num_players, _user_id)
            child = self._tree.get_node(child_id)
            if child.data.result == 'win':
                num_wins += 1
            elif child.data.result == 'loss':
                num_losses += 1
            else:
                num_unknown += 1

        # label based on children
        if num_unknown != 0:
            wNode.data = Letter('unknown', _count, self._calc_winPercent(_node_id))
        elif num_losses == 0:
            wNode.data = Letter('win', _count, 1.0)
        elif num_wins == 0:
            wNode.data = Letter('loss', _count, 0.0)
        else:
            wNode.data = Letter('unknown', _count, self._calc_winPercent(_node_id))


    def label_tree(self, _node_id, _num_players, _user_id):
        print('labelling tree')
        self._label_recursion(_node_id, 0, _num_players, _user_id)


    def get_winOptions(self, _node_id):
        win_options = []
        wNode = self._tree.get_node(_node_id)
        children_ids = wNode.successors(self._tree.identifier)
        for child_id in children_ids:
            child = self._tree.get_node(child_id)
            if child.data.result == 'win':
                win_options.append(child_id[-1])
        return win_options


    def get_highestUnknown(self, _node_id):
        highestUnknown_id = 0
        highestUnknown_percent = 0.0
        solution = []

        wNode = self._tree.get_node(_node_id)
        children_ids = wNode.successors(self._tree.identifier)
        for child_id in children_ids:
            child = self._tree.get_node(child_id)
            if child.data.result == 'unknown':
                if child.data.percent_win > highestUnknown_percent:
                    highestUnknown_id = child_id
                    highestUnknown_percent = child.data.percent_win
        if highestUnknown_id != 0:
            solution.append(highestUnknown_id[-1])
        return solution


## TESTS ##

def Test_1():
    print ("class Word_Tree: running Test_1.")
    wtree = Word_Tree()

def Test_2(word):
    print ("class Word_Tree: running Test_2.")
    wtree = Word_Tree()
    wtree.add_word(word)
    wtree.show_tree()

def Test_3():
    print ("class Word_Tree: running Test_3.")
    wtree = Word_Tree()
    sublist = ['hasan', 'korre', 'hamburger']
    wtree.add_sublist(sublist)
    wtree.show_tree()

def Test_4():
    print ("class Word_Tree: running Test_4.")
    wtree = Word_Tree()
    wtree.add_word('hasan')
    wtree.add_word('hamburger')
    wtree.remove_word('hasan')
    wtree.show_tree()

def Test_5():
    print ("class Word_Tree: running Test_5.")
    wtree = Word_Tree()
    sublist = ['hasan', 'korre', 'hamburger', 'jump']
    wtree.add_sublist(sublist)
    #wtree.label_tree(0, 3, 1)
    #wtree.label_tree(0, 3, 2)
    wtree.label_tree(0, 3, 3)
    wtree.show_tree()
    wtree.show_treeData()
    wtree.show_treePercent()
    print('win options = ' + str(wtree.get_winOptions('ha')))

if __name__ == "__main__":
    Test_1()
    Test_2('zym')
    Test_3()
    Test_4()
    Test_5()


