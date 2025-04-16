# Hanoi Rings.

def hanoi(n,start,end,aux):
    if n == 1:
        print("Move ring 1 from " + start + " to " + end + ".")
    else:
        hanoi(n-1, start, aux, end)
        print("Move ring " + str(n) + " from " + start + " to " + end + ".")
        hanoi(n-1, aux, end, start)

n = 6 
hanoi(n, "a", "c", "b")
        
