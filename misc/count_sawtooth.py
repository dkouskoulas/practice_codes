def count_sawtooth_patterns(s: str) -> int:
    """
    Counts the number of sawtooth patterns in the input string using dynamic programming.
    A sawtooth pattern is defined as a sequence where characters strictly alternate between increasing and decreasing.
    Individual numbers/characters are also counted as sawtooth patterns.
    """
    n = len(s)
    if n == 0:
        return 0
    # dp[i] will store the number of sawtooth patterns ending at index i
    dp = [1] * n  # Each single character is a sawtooth pattern
    count = n     # Start with n single-character patterns
    for i in range(1, n):
        for j in range(i):
            if (s[j] < s[i] and (j == 0 or s[j-1] > s[j])) or (s[j] > s[i] and (j == 0 or s[j-1] < s[j])):
                dp[i] += dp[j]
        count += dp[i] - 1  # Exclude the single character already counted
    return count

if __name__ == "__main__":
    test_str = input("Enter a string: ")
    result = count_sawtooth_patterns(test_str)
    print(f"Number of sawtooth patterns: {result}")
