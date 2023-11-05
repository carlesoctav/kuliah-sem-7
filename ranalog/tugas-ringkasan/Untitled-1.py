def schedule_tasks(d:list[list[int]],  n):
    # Initialize variables
    j = [0] * (n + 1)
    j[0] = 0
    k = 0

    # Sort tasks by profit in non-increasing order
    tasks = sorted(range(1, n), key=lambda x: d[x][0], reverse=True)

    # Assign tasks to the latest possible time slot before their deadline
    for i in tasks:
        r = k # r is the latest possible time slot
        while d[j[r]][1] > max(d[i][1], r): # Find the latest possible time slot
            r -= 1 
        if d[j[r]][1] <= d[i][1] and d[i][1] > r:
            for l in range(k, r, -1):
                j[l + 1] = j[l]
            j[r + 1] = i
            k += 1

    # Return the number of selected tasks and their indices
    return k, j[1:k+1]


if __name__ =="__main__":
    # Read input
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    d = sorted(d)
    print(f"==>> d: {d}")

    # Solve
    k, j = schedule_tasks(d, n)

    # Print output
    print(k)
    print(*j)
