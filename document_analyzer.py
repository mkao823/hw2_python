def sorter(nameOfFile):
    file = open(nameOfFile) 
    words = {}
    a = file.read()
    words = a.split()
    words.sort()

    for word in words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1        
        
