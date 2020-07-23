'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # initialize index of arr and temp
    left = 0
    right = len(arr) - 1
    # iterate through array
    while left <= right:
        # if left is 0 and left is not 0
        if arr[left] == 0 and arr[right] != 0:
            # swap left with right
            arr[left], arr[right] = arr[right], arr[left]
            # increment left
            left += 1
            # decrement right
            right -= 1
        # otherwise
        else:
            # if left is not 0
            if arr[left] != 0:
                # increment left
                left += 1
            # if right is 0
            if arr[right] == 0:
                # decrement right
                right -= 1
    # return arr
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")