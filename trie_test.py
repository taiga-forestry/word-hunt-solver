import pytest
import trie

def test_add():
    ''' Tests the add() and contains() methods '''

    # empty trie
    t = trie.Trie()
    assert t.size == 0
    assert t.contains("A") == False

    # adding to trie on leaf, empty word case
    t.add("A")
    t.add("A")
    t.add("BOAT")
    assert t.size == 2
    assert t.contains("A") == True
    assert t.contains("BOAT") == True
    assert t.contains("B") == False
    assert t.contains("BOA") == False

    # adding to trie on node, non-empty word case
    t.add("BOLT")
    assert t.size == 3
    assert t.contains("BOLT") == True

    # adding to trie on node, empty word case
    t.add("BOA")
    assert t.size == 4
    assert t.contains("BOA") == True

    # adding to trie on leaf, non-empty word case
    t.add("BOATING")
    assert t.size == 5
    assert t.contains("BOATING") == True


def test_remove():
    ''' Tests the remove() and contains() methods '''

    # empty trie
    t = trie.Trie()
    assert t.size == 0
    assert t.remove("") == False

    t.add("BOAT")
    t.add("BOLT")
    t.add("BOA")
    t.add("BOATING")

    # removing non-existent element from trie
    assert t.size == 4
    assert t.remove("B") == False

    # removing element twice from trie
    assert t.remove("BOA") == True
    assert t.remove("BOA") == False
    assert t.contains("BOA") == False
    assert t.size == 3

    # removing element which is "subelement" from trie
    assert t.remove("BOAT") == True
    assert t.contains("BOATING") == True
    assert t.contains("BOLT") == True
    assert t.contains("BOAT") == False
    assert t.size == 2

    # removing element after adding same element
    t.add("BOA")
    assert t.contains("BOA") == True
    assert t.contains("BOAT") == False
    assert t.contains("BOATING") == True
    assert t.contains("BOLT") == True
    assert t.size == 3


# function calls!!
test_add()
test_remove()

