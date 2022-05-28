class Node:
    ''' Class representing a Node in a Trie '''

    def __init__(self):
        ''' Constructor for the Node class '''
        
        self.is_word = False
        self.children = {} # letters -> nodes