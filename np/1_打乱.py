import numpy as np

a1 = np.array(range(10))
assert a1[0] == 0
assert a1[-1] == 9

"""
随机打乱
"""

np.random.seed(10)
shuffled_indexes = np.random.permutation(len(a1))
a2 = a1[shuffled_indexes]
assert a2[0] == 8
assert a2[-1] == 9

shuffled_indexes_1 = list(range(len(a1)))
np.random.shuffle(shuffled_indexes_1)
a3 = a1[shuffled_indexes_1]
assert a3[0] == 5
assert a3[-1] == 0
