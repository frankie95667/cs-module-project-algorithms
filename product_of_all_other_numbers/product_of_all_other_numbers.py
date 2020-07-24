'''
Input: a List of integers
Returns: a List of integers
'''
import math
def product_of_all_other_numbers(arr):
    # loop through arr
    mult_arr = [1] * len(arr)
    for i in range(0, len(arr)):
        # loop through arr again
        if i == 0:
            # product of list from 1 to the end of the list
            mult_arr[i] = math.prod(arr[1:])
        elif i == len(arr) - 1:
            # product of list from 0 to i exclusive
            mult_arr[i] = math.prod(arr[0:i])
        else:
            # product of list from 0 to i exclusive and i+1 to the end
            mult_arr[i] = math.prod(arr[0:i] + arr[i+1:])
    return mult_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
