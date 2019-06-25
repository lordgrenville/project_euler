def count_ways(total, coins):
    if total < 0:
        return 0
    if total == 0:
        return 1
    if len(coins) <= 0:
        return 0
    return count_ways(total - coins[-1], coins) + count_ways(total, coins[:-1])

count_ways(200, [1, 2, 5, 10, 20, 50, 100, 200])
