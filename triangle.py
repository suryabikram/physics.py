try:
    f = open(input("Enter input filename:   "))
    d = {}
    for line in f:
        for word in line.split():
            if word not in d:
                d[word] = 0
            d[word] += 1
    f.close()
    num_words = 0
    for word, count in reversed(sorted(d.items(), key=lambda x: x[1])):
        print(word, count)
        num_words += 1
        if num_words == 30:
            break
except:
    print("File not found!")