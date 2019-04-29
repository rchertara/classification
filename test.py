import numpy as np


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

c = np.arange(4200).reshape((70,60))
print(c )

print (blockshaped(c, 2, 4))
# print()




# print ("\n")
# print (val)
