def makeChange(coins, total):
    # Initialize an array to store the minimum number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total of 0
    
    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each amount from coin value to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still float('inf'), it means the total cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]