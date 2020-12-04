
#Métrica de Relatedness de Lesk
def getTermList(Dataset, word):
    terms = []
    return terms

def rel_lesk(Dataset, word1, word2):

    #   The Lesk measure works by finding overlaps in the extended definitions 
    #   of the two concepts. The relatedness score is the sum of the squares of 
    #   the overlap lengths.  For example, a single word overlap results in a 
    #   score of 1.  Two single word overlaps results in a score of 2. A two 
    #   word overlap (i.e., two consecutive words) results in a score of 4. A 
    #   three word overlap results in a score of 9.    

    overlap = 0
    terms = getTermList(word1)
    terms = getTermList(word2)
    for i in terms:
        if (i in word2.terms):
            overlap+=1

    lesk_score = overlap*overlap
    return lesk_score

# McInnes(2015): Lesk [17] introduces a measure that determines the relatedness
# between two concepts by counting the number of overlaps
# between their two definitions. An overlap is the longest sequence
# of one or more consecutive terms that occur in both definitions.
# When implementing this measure in WordNet, Banerjee and
# Pedersen [18] found that the definitions were short, and did not
# contain enough overlaps to distinguish between multiple concepts,
# therefore, they extended this measure by including the definitions
# of the related concepts


# function SIMPLIFIED LESK(word,sentence) returns best sense of word
#     best-sense <- most frequent sense for word
#     max-overlap <- 0
#     context <- set of words in sentence
#     for each sense in senses of word do
#     signature <- set of words in the gloss and examples of sense
#     overlap <- COMPUTEOVERLAP (signature,context)
#     if overlap > max-overlap then
#     max-overlap <- overlap
#     best-sense <- sense
#     end return (best-sense)

def rel_vector():

    # <h2>Vector</h2>
    # <p>The vector measure works by forming second-order 
    #   co-occurrence vectors from the UMLS extended definitions of concepts. 
    #   The relatedness of two concepts is determined as the cosine of the 
    #   angle between their vectors. 

    return rel_vector