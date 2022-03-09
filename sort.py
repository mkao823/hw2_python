def sort_list(myList):
    '''this is summary line

    now we can use this to describe program
    method should take in a list input and return a list
    in sort list, n is length of input list
    
    ''' 
    n = len(myList)
    i = 0
    j = 0
    while i < n - 1:
        while j < n - i - 1:
            if myList[i] > myList[j]:
                myList[j] = myList[i]

    return myList
            
    

