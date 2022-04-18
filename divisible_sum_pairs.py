def divisibleSumPairs(n,k,ar):
    count = 0
    '''for i in ar:
        for j in range(n):
            if i<ar[j]:
                s = i + ar[j]
                if s%k ==0:
                    count+=1'''
    for i, e in enumerate(ar):
        for j in range(i+1, len(ar)):
            s = e+ar[j]
            if s%k==0:
                count+=1
    return count
                    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
