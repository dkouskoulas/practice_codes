def num_islands(grid):

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    count = 0

    def dfs(r, c):

        if (
            r < 0 or
            c < 0 or
            r >= rows or
            c >= cols or
            grid[r][c] == "0"
        ):
            return

        grid[r][c] = "0"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == "1":
                count += 1
                dfs(r, c)

    return count


def search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # left half sorted
        if nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # right half sorted
        else:

            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1