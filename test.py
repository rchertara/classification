import numpy as np
import util
import classificationMethod
import math

def sumAll(input):
    return sum(map(sum, input))

def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    index = (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))
    # for lt in range(len(index))
    #     index[lt]
    #     if (== 0):
    # print
    # return sumAll(index[7])
    return index

# a = []
# for i in xrange(10):
#     a.append([])
#     for j in xrange(10):
#             a[i].append(i+j)
#
# # print(a)
# data = [1,3,4,5,6,7,8,9]
# y = np.array(data)
# c = np.reshape(data, (4,2))
# print(len(c))\

# 6 col, 4 rows
c = np.arange(24).reshape((4,6))
print(c)
arrayCount = []
# arrayCount.append(5)
print arrayCount

row_pixel_count = 0
for x in range(6):
    row_pixel_count = 0
    for y in range(4):
        if c[y, x] > 0:
            row_pixel_count += 1
        if (y == 4 -1):
            arrayCount.append(row_pixel_count)
            row_pixel_count = 0

print arrayCount
# print (blockshaped(c, 4, 2))
# print()




# print ("\n")
# print (val)
