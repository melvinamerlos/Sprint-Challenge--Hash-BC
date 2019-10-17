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

    """
    YOUR CODE HERE
    """

    # insert tickets into hash table
    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    # setting the first destination to starting point's destination
    route[0] = hash_table_retrieve(ht, 'NONE')

    # after starting point set, loop thru route list and set next destination in list
    for i in range(1, length):
        route[i] = hash_table_retrieve(ht, route[i - 1])

    # return the list of routes
    return route
