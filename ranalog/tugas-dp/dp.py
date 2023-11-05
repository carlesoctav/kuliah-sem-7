def solve(weights, profits, n, max_w):
    dp = [[0 for _ in range(max_w+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, max_w+1):
          left_over = j - weights[i-1]
          dp[i][j] = dp[i-1][j]
          if (left_over>=0):
             dp[i][j] = max(dp[i][j], dp[i-1][left_over]+profits[i-1])

    
    return dp[n][max_w]

def solve_with_traceback(weights, profits, n, max_w):
    dp = [[0 for _ in range(max_w+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, max_w+1):
          left_over = j - weights[i-1]
          dp[i][j] = dp[i-1][j]
          if (left_over>=0):
             dp[i][j] = max(dp[i][j], dp[i-1][left_over]+profits[i-1])

    queue = [(n, max_w, [])]
    list_of_solution = set()

    while queue:
        i, j, curr_solution = queue.pop(0)
        if (i==0 or j==0):
            list_of_solution.add(tuple(curr_solution))
            continue

        if (dp[i][j] == dp[i-1][j]):
            queue.append((i-1, j, curr_solution))
            continue

        for left_over in range(j-1, 0, -1):
            if(j-weights[i-1]> left_over):
                continue

            if (dp[i][j] == dp[i-1][left_over]+profits[i-1]):
                nxt_node = (i-1, left_over, curr_solution+[(i,weights[i-1],profits[i-1])])
                queue.append(nxt_node)

    return list_of_solution , dp[n][max_w]
       

def main():
    n, max_w = input().split()
    n = int(n)
    max_w = int(max_w)

    weights = input().split()
    weights = [int(w) for w in weights]
     
    profits = input().split()
    profits = [int(profit) for profit in profits]
    
    list_of_sol, max_profit = solve_with_traceback(weights, profits, n, max_w)

    print(f"==>> list_of_sol: {list_of_sol}")

    print(max_profit)


main()