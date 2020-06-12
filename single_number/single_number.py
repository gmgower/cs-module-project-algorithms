'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Create an arry, call it no_dups to hold numbers 
    # iterate through nums
        ## check to see if the number is already present
        ## remove duplicates numbers
    # return odd numbers out
    
    no_duplicates = []
    for x in arr:
        if x not in no_duplicates:
            no_duplicates.append(x)
        else:
            no_duplicates.remove(x)
    return no_duplicates[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
