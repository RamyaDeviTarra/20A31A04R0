#abc pattern
n=int(input())
for i in  range(1, n+1):
    ch='A'
    print()
    for i in range(1, i+1):
        print(ch,end=' ')
        ch = chr(ord(ch)+1)
