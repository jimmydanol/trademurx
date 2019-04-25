def process_term(term):

    list_of_permutated_terms = []

    # Creates a for loop that calls upon a generator function
    if term:
        for c in permutate(term):
            list_of_permutated_terms.append(c)

        return(list_of_permutated_terms)

def permutate(term_to_permutate):

    yield (term_to_permutate,)
    # A recursive for loop that generates permutations
    for i in range(1, len(term_to_permutate)):
        for c in permutate(term_to_permutate[i:]):
            yield (term_to_permutate[:i],) + c
