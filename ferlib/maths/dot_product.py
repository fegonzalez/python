def dot_product(v, w):
    "v, w: two vectors of the same range. return: v.w"
    assert(len(v) == len(w))
    return sum([v[i]*w[i] for i in range(0, len(v))])

#\test
# v=[1, 0, 2]
# w=[3,1,1]
# assert(dot_product.dot_product(v, w)==5) 


# QUIZZ

# 1) 2111211

# 2) palabra dos = [1 7 0 0 2 0 1] 
#
# ex2_ref=[2,1,1,1,2,1,1]
# >>> uno = [7, 0, 2, 1, 0, 0, 1]
# >>> dos = [1, 7, 0, 0, 2, 0, 1]
# >>> tres = [1, 0, 0, 0, 7, 1, 2]
# >>> cuatro = [0, 2, 0, 0, 7, 1, 1]
# todos = [uno, dos, tres, cuatro]
# dot_ref_todos = [dot_product.dot_product(ex2_ref, i) for i in todos]
# dot_ref_todos
# [13, 27, 18, 22] # max similarity = 27 -> 'dos' se parece más a ex2_ref

