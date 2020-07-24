'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Initialize Qi with empty list
    Qi = []
    # initialize max_arr with empty list
    max_arr = []
      
    # Loop through nums array up to index k-1
    for i in range(k):
        
        # While nums[i] is greater than or equal to nums[Qi[-1]]
        while Qi and nums[i] >= nums[Qi[-1]]:
            # Remove last element on Qi list
            Qi.pop()

        # Add new element at rear of queue 
        Qi.append(i)
          
          
    # Loop through the rest of the nums array
    # from nums[k] to nums[len(nusm)-1] 
    for i in range(k, len(nums)):
          
        # The element at the front of the 
        # queue is the largest element of 
        # previous window, so append it to max_arr 
        max_arr.append(nums[Qi[0]])
          
        # Remove the elements which are  
        # out of this window 
        while Qi and Qi[0] <= i-k:
            # remove from front of Qi 
            Qi.pop(0)              
          
        # While nums[i] is greater than or equal to nums[Qi[-1]]
        while Qi and nums[i] >= nums[Qi[-1]]:
            Qi.pop()
          
        # Add current element at the rear of Qi 
        Qi.append(i)
      
    # append the maximum element of last window to max_arr
    max_arr.append(nums[Qi[0]])
    return max_arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
