import node

class Trie:
    ''' Class representing the Trie data structure for words '''

    def __init__(self):
        ''' Constructor for the Trie class '''
        
        self.root = node.Node(False)
        self.size = 0


    def add(self, word: str):
        ''' 
        Adds an element into the trie and increases trie size by 1

        Parameters:
        word (str) -- word to add into the trie

        Exceptions:
        (ValueError) -- raised if attemping to insert word of length 0
        '''
        
        if len(word) == 0:
            raise ValueError("cannot add empty word into trie!")
        
        if not self.contains(word, False):
            self.root = self.root.add(word)
            self.size += 1
        

    def remove(self, word: str) -> bool:
        ''' 
        Removes an element from the trie and decreases trie size by 1 if successful

        Parameters:
        word (str) -- word to remove from the trie

        Returns:
        (bool) -- returns True if element is successfully removed, False otherwise
        '''

        if self.root.remove(word):
            self.size -= 1
            return True
        
        return False


    def contains(self, word: str, partial_word: bool) -> bool:
        ''' 
        Determines whether an element exists in the trie 
        
        Parameters:
        word (str) -- word to check for in the trie
        partial_word (bool) -- whether or not user is searching for partial word or not

        Returns: 
        (bool) -- returns True if element is found, False otherwise
        '''

        return self.root.contains(word, partial_word)
