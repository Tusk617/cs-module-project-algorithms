'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    '''
    This solution was inefficient becuase rather than moving the other values to the front, it was simply 
    appending an instance of 0 to the end of the the list. With real data this would be inefficient, as we might not always
    a new instance of the same element, rather we might just want to organize the current list as is.
    '''
    # appended = True
    # while appended:
    #     appended = False
    #     for elem in arr:
    #         if elem == 0:
    #             arr.remove(elem)
    #             arr.append(0)
    #             appended = True
    #     return arr
    '''
    This solution is more efficient. We're not losing any data in the transfer from current position to the 
    front of the list. This would be more effiecient than the previous as we aren't losing any data, simply storing it in
    a temporary location and reintroducing it later.
    '''
    inserted = True
    while inserted:
        inserted = False
        for i in range(len(arr)):
            if arr[i] != 0:
                temp = arr[i]
                arr.pop(i)
                arr.insert(0, temp)
        return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")