def sort(owo):
    for n in range(len(owo)-1,0,-1):
        for i in range(n):
            if owo[i] > owo[i+1]:
                owo[i], owo[i+1] = owo[i+1],owo[i]

owo = []/*abwa! need to define the list to sort*/
print("unsorted: ")
print(owo)
sort(owo)
print("sorted: ")
print(owo)