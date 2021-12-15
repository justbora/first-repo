def reverseandswapcases(sentence):
    # print(' '.join(reversed(sentence.split())).swapcase())


    rs=' '.join(reversed(sentence.split())).swapcase()
    s=''
    for word in rs:
        if word==word.upper():
            s+=word.lower()
        else: s+=word. upper()   
    print(s)

    

reverseandswapcases("aWESOME IS cODING")