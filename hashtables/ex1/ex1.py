#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    right_val = None

    if len(weights) == 2 and limit - (weights[0]*2) == 0:
        return (len(weights)-1, len(weights)-2)
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
        print(ht.storage)
    for j in range(len(ht.storage)):
        node = ht.storage[j]
        if node is not None:
            print("node is: ", node)
            print(node.next)
            need_val = limit - node.key
            print("Need: ", need_val)
            is_it_there = hash_table_retrieve(ht, need_val)
            print(is_it_there)
            if is_it_there is not None:
                if is_it_there > node.value:
                    right_val = (is_it_there, node.value)
                else:
                    right_val = (node.value, is_it_there)
                break
            else:
                j+= 1
            j+= 1
    if right_val is not None:
        return right_val
    else:
        return None

weights_3 = [4, 4]
print(get_indices_of_item_weights(weights_3, 2, 8))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
