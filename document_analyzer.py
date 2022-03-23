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
            
    index = 0
    unique = sorted(words.items(), key = lambda x:x[1], reverse = True)
    unique = dict(unique)

    print("\r")
    for word, count in unique.items():
        print("%s: %s" % (word, count))
        index += 1
        if(index == 5):
            break
