import node

class Leaf:
    ''' Class representing a Leaf in a trie '''

    def add(self, word: str):
        ''' 
        Adds an element into the trie and increases trie size by 1

        Parameters:
        word (str) -- word to add into the trie
        '''
        
        if len(word) == 0:
            return node.Node(True)
        else:
            new_node = node.Node(False)
            letter = word[0]
            index = ord(letter) - 65 # converts capital letter into ASCII
            new_node.children[index] = new_node.children[index].add(word[1:])

            return new_node


    def remove(self, word: str) -> bool:
        ''' 
        Removes an element from the trie and decreases trie size by 1 if successful

        Parameters:
        word (str) -- word to remove from the trie

        Returns:
        (bool) -- returns True if element is successfully removed, False otherwise
        '''
        
        return False


    def contains(self, word: str, partial_word: bool) -> bool:
        ''' 
        Determines whether an element exists in the trie 
        
        Parameters:
        word (str) -- word to check for in the trie
        partial_word (bool) -- whether or not user is searching for partial word or not

        Returns: 
        (bool) -- returns False since this is a Leaf
        '''
        
        return False