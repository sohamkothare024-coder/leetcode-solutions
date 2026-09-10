class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        def cost(i, j):
            length = j - i + 1
            best = float('inf')
            for d in range(1, length):          # d < length, not <= length
                if length % d != 0:
                    continue
                groups = [[] for _ in range(d)]
                for idx in range(length):
                    groups[idx % d].append(s[i + idx])
                changes = 0
                for g in groups:
                    l, r_ = 0, len(g) - 1
                    while l < r_:
                        if g[l] != g[r_]:
                            changes += 1
                        l += 1
                        r_ -= 1
                best = min(best, changes)
            return best

        precost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                precost[i][j] = cost(i, j)

        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for p in range(1, min(k, i) + 1):
                for j in range(p - 1, i):
                    if dp[j][p - 1] != INF:
                        dp[i][p] = min(dp[i][p], dp[j][p - 1] + precost[j][i - 1])
        return dp[n][k]