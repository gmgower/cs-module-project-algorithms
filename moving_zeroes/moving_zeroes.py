'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):  
    # create two counters 
    i = 0
    end = len(arr) - 1
    # Iterate list 
    while i < end:
        # If value is 0 append and del position
        if arr[i] == 0:
            arr.append(arr[i])
            del arr[i]
            # and decrement i
            end -= 1
        # otherwise increment i
        else:
            i += 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
