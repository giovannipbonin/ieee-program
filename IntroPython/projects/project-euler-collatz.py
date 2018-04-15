"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""



def get_collatz_chain_length(starting_number: int) -> int:
    """
    Implement the collatz function and return the chain length
    """
    pass


def find_longest_chain(max_number):
    longest_chain = 0
    for i in range(max_number):
        curr_chain = get_collatz_chain_length(i)
        if curr_chain > longest_chain:
            longest_chain = curr_chain

    return longest_chain

if __name__ == "__main__":
    print(find_longest_chain(max_num=1000000))
