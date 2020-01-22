#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    # end if there is less than 2 weights
    if len(weights) <= 1:
        return None

    # declare a result and a hash table
    result = []
    table = {}

    # loop thru the weights, determine the sum minus the weight
    for i in range(0, len(weights)):
        limit_minus_weight = limit - weights[i]

        table[weights[i]] = limit_minus_weight

    for i in range(0, len(weights)):
        if limit - weights[i] in table:
            result.insert(0, i)

    return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


get_indices_of_item_weights([ 4, 7, 9, 12, 15 ], 7, 98)
