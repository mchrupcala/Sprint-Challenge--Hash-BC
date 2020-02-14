#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    sorted_route = []

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
        if i.source == "NONE":
            sorted_route.append(i.destination)
    
    while len(sorted_route) != length-1:
        new_destination = hash_table_retrieve(hashtable, sorted_route[len(sorted_route)-1])
        sorted_route.append(new_destination)
    

    return sorted_route