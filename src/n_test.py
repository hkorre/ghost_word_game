from word_list import Word_List
from word_tree import Word_Tree



wTree = Word_Tree()

wList = Word_List()
sublist = wList.get_sublist('nir')
wTree.add_sublist(sublist)

wTree.label_tree(0, 2, 2)
wTree.show_tree()
wTree.show_treeData()

