#prints the fibonnaci sequence for length n

def fib(n):
    seq = [1, 1]
    while len(seq) < n+1:
        next = seq[-1] + seq[-2]
        seq.append(next)
    print(seq)

fib(8)

