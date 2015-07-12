
# =============================================================================
# Vectors
# =============================================================================

def dotprod(a, b):
    """ Compute dot product
    Args:
        a (dictionary): first dictionary of record to value
        b (dictionary): second dictionary of record to value
    Returns:
        dotProd: result of the dot product with the two input dictionaries
    """
    return sum((a.get(k, 0.0) * v) for k,v in b.items())

# -----------------------------------------------------------------------------

def norm(a):
    """ Compute the norm of a vector = square root of the dot product.
    Args:
        a (dictionary): a dictionary of record to value
    Returns:
        norm: the norm of the vector.
    """
    return math.sqrt(sum(v**2 for v in a.values()))

# -----------------------------------------------------------------------------

def cossim(a, b):
    """Compute cosine similarity
    Args:
        a (dictionary): first dictionary of record to value
        b (dictionary): second dictionary of record to value

    Returns: cossim: dot product of two dictionaries divided by the norm of the
        first dictionary and then by the norm of the second dictionary

    """
    return dotprod(a,b) / (norm(a) * norm(b))

# -----------------------------------------------------------------------------

# test
# testVec1 = {'foo': 2, 'bar': 3, 'baz': 5 }
# testVec2 = {'foo': 1, 'bar': 0, 'baz': 20 }
# dp = dotprod(testVec1, testVec2)
# nm = norm(testVec1)
# cosine_similarity = cossim(testVect1, testVect1)
# print dp, nm
# TEST Implement the components of a cosineSimilarity function (3a)
# Test.assertEquals(dp, 102, 'incorrect dp')
# Test.assertTrue(abs(nm - 6.16441400297) < 0.0000001, 'incorrrect nm')
# Test.assertTrue( abs(cos_simil - 1.0) < 0.0000001 , 'bad cossim')
