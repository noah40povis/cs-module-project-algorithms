'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    lst = []
    for i in arr: 
        if i != 0:
            lst.insert(0, i)
        else:
            lst.insert(len(arr), i)
    return lst 


if __name__ == '__main__': 
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")