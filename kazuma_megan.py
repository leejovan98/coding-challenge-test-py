def kazuma_jovan(monsters):
    if len(monsters) < 2:
        return 0
    length = len(monsters) + 1
    dp = [[0 for _ in range(length)] for _ in range(4)] # 0 is att, 1 is prep, 2 is ret, 3 ret + prep
    dp[0][1] = -(monsters[0]) + monsters[1]
    dp[1][1] = -(monsters[1])
    dp[3][1] = -(monsters[0])
    for i in range(2, length - 1):
        dp[0][i] = max(dp[3][i - 1], dp[1][i - 1]) + monsters[i]
        dp[1][i] = dp[2][i - 1] - monsters[i]
        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1])
        dp[3][i] = max(dp[3][i - 1], dp[1][i - 1])
    return max(dp[0][-2], dp[1][-2], dp[2][-2], dp[3][-2])