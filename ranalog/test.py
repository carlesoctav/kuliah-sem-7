count = 0

def ones(n):
    global count
    if n == 0:
        count+=1
    else:
        for i in range(1, 2**n + 1):
            ones(n - 1)

# Example usage
ones(5)  # Replace 3 with the desired value of n
print(count)