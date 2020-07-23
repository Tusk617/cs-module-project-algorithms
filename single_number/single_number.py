'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    '''
    This implementation works only under the condition that all the elements in the array appear as pairs with eachother. 
    Obviously in a large database this logic might not be effective if it isn't sorted that way.
    '''
    # for i in arr:
    #     temp = i
    #     arr.remove(i)
    #     if temp not in arr:
    #         return temp
    '''
    This implementation works better than the previous, as it's actually iterating through the array and taking account of each time
    an element shows up. We want the element that appears just once, so this makes it much more effective and dynamic as opposed
    to the previous methods requirement that each double is next to its double.
    '''
    for i in arr:
        if arr.count(i) == 1:
            return i

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 4, 1, 5, 5, 3, 3, 9, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")