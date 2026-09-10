class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = sum(range(1, n + 1))
        divisible = sum(i for i in range(1, n + 1) if i % m == 0)
        non_divisible = total - divisible
        return non_divisible - divisible