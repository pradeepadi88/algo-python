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
            for j in range(i + 1, i + k):
                sum += array[j]
            max_sum = max(sum, max_sum)
        return max_sum

    @staticmethod
    def max_sum_of_Subarray_sliding_window_1(array: list, n, k):
        sum = 0
        for i in range(k):
            sum += array[i]
        max_sum = sum
        for i in range(k, n):
            sum += (array[i] - array[i - k])
            max_sum = max(sum, max_sum)
        return max_sum

    @staticmethod
    def max_sum_of_Subarray_sliding_window_2(array: list, n, k):





if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    n = len(arr)
    max_sum_naive = Solution.max_sum_of_subarray(arr, n, k)
    max_sum_sw_1 = Solution.max_sum_of_Subarray_sliding_window_1(arr, n, k)
    print(max_sum_naive)
    print(max_sum_sw_1)
