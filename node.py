from functools import partial
import leaf

class Node:
    ''' Class representing a Node in a Trie '''

    def __init__(self, is_word: bool):
        ''' Constructor for the Node class '''

        self.is_word = is_word
        self.children = [leaf.Leaf() for i in range(26)]


    def add(self, word: str) -> "Node":
        ''' 
        Adds an element into the trie and increases trie size by 1

        Parameters:
        word (str) -- word to add into the trie
        '''
        
        if len(word) == 0:
            self.is_word = True
        else:
            letter = word[0]
            index = ord(letter) - 65 # converts capital letter into ASCII
            self.children[index] = self.children[index].add(word[1:])

        return self


    def remove(self, word: str) -> bool:
        ''' 
        Removes an element from the trie and decreases trie size by 1 if successful

        Parameters:
        word (str) -- word to remove from the trie

        Returns:
        (bool) -- returns True if element is successfully removed, False otherwise
        '''

        if len(word) == 0:
            if self.is_word:
                self.is_word = False
                return True
            else:
                return False
        else:
            letter = word[0]
            index = ord(letter) - 65 # converts capital letter into ASCII

            return self.children[index].remove(word[1:])


    def contains(self, word: str, partial_word: bool) -> bool:
        ''' 
        Determines whether an element exists in the trie 
        
        Parameters:
        word (str) -- word to check for in the trie
        partial_word (bool) -- whether or not user is searching for partial word or not
        
        Returns: 
        (bool) -- returns True if element is found, False otherwise
        '''
        
        if len(word) == 0:
            return self.is_word or partial_word
        else:
            letter = word[0]
            index = ord(letter) - 65 # converts capital letter into ASCII

            return self.children[index].contains(word[1:], partial_word)
