import node 

class Trie:
    ''' Class representing the Trie data structure for words '''

    def __init__(self):
        ''' Constructor for the Trie class '''

        self.root = node.Node()
        self.size = 0
    

    def add(self, word: str):
        ''' 
        Adds an element into the trie and increases trie size by 1

        Parameters:
        word (str) -- word to add into the trie
        '''

        word = word.upper()
        curr_node = self.root

        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                new_node = node.Node()
                curr_node.children[letter] = new_node
                curr_node = new_node

        if curr_node.is_word == False:
            curr_node.is_word = True
            self.size += 1


    def remove(self, word: str) -> bool:
        ''' 
        Removes an element from the trie and decreases trie size by 1 if successful

        Parameters:
        word (str) -- word to remove from the trie

        Returns:
        (bool) -- returns True if element is successfully removed, False otherwise
        '''

        word = word.upper()
        curr_node = self.root

        for letter in word:
            if letter not in curr_node.children:
                return False
            
            curr_node = curr_node.children[letter]
        
        if curr_node.is_word == True:
            curr_node.is_word = False
            self.size -= 1
            
            return True
        else:
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

        word = word.upper()
        curr_node = self.root

        for letter in word:
            if letter not in curr_node.children:
                return False
            
            curr_node = curr_node.children[letter]
        
        return curr_node.is_word or partial_word