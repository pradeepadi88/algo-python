# This program solves the K Sum question in Naive Sum

# Find maximum (or minimum) sum of a subarray of size k

class Solution:

    @staticmethod
    def max_sum_of_subarray(array: list, n, k):
        max_sum = 0
        if n < k:
            for i in range(n):
                max_sum += array[i]
        for i in range(n - k + 1):
            sum = array[i]
            for j in range(i+1, i+k):
                sum += array[j]
            max_sum = max(sum, max_sum)
        return max_sum


if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 11
    n = len(arr)
    max_sum = Solution.max_sum_of_subarray(arr, n, k);
    print(max_sum);
