def sort_list(list):
    '''this is summary line

    now we can use this to describe program
    method should take in a list input and return a list
    in sort list, n is length of input list
    
    ''' 
    n = len(list)
    i = 0
    j = 0
    while i < n - 1:
        while j < n - i - 1:
            if list[j+1] < list[j]:
                temp = list(j)
                list[j] = list[j+1]
                list[j+1] = temp
            j+=1
        i+=1
    return list
            
    

