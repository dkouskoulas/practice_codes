def count_sawtooth_parity_patterns(s: str) -> int:
    """
    Counts sawtooth patterns in a string of digits where the parity (even/odd) flips with each number.
    Single numbers are counted as sawtooth patterns.
    """
    n = len(s)
    if n == 0:
        return 0
    

    dp = [1] * n  # Each single digit is a sawtooth pattern
    count = n
    
    for i in range(1, n):
        for j in range(i):
            if (int(s[j]) % 2) != (int(s[i]) % 2):
                dp[i] += dp[j]
        count += dp[i] - 1
    return count

def count_sawtooth_parity_patterns_simple(s: str) -> int:
    """
    Counts sawtooth patterns in a string of digits where the parity flips with each number.
    Single numbers are counted as sawtooth patterns.
    This version is simpler and uses a running count.
    """
    n = len(s)
    if n == 0:
        return 0
    
    count = 1  # First digit is always a sawtooth pattern

    for i in range(1, n):
        if (int(s[i]) % 2) != (int(s[i-1]) % 2):
            count += 1
            
    return count

def count_alternating_parity(nums):
    """
    Counts all contiguous substrings in a list of numbers where the parity alternates.
    Each single element is counted.
    Efficient O(n) approach.
    """
    if not nums:
        return 0
    total = 1   # first element alone
    run = 1     # length of current alternating run
    for i in range(1, len(nums)):
        if nums[i] % 2 != nums[i - 1] % 2:
            run += 1
        else:
            run = 1
        total += run
    return total

if __name__ == "__main__":
    num_str = input("Enter a string of digits: ").strip()
    # Remove any quotes or non-digit characters
    num_str = ''.join(c for c in num_str if c.isdigit())
    result = count_sawtooth_parity_patterns(num_str)
    print(f"Number of sawtooth parity patterns: {result}")
    # Optionally show results for other functions
    print(f"Simple count: {count_sawtooth_parity_patterns_simple(num_str)}")
    nums = [int(c) for c in num_str]
    print(f"Alternating parity substrings: {count_alternating_parity(nums)}")
