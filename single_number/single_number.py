'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # assign empty array to single_ladies
    single_ladies = {}
    # iterate through array
    for num in arr:
    # if value at index i is in new list
        if num in single_ladies:
            # remove i from new list
            single_ladies[num] += 1
        # else
        else:
            # append number to new list
            single_ladies[num] = 1
        # return first index of new list
    for key, value in single_ladies.items():
        if value == 1:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    

    print(f"The odd-number-out is {single_number(arr)}")