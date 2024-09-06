class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
    
        # Step 2: Create an extended array by duplicating the original one
        extended_data = nums + nums
    
        # Step 3: Calculate number of 1's in the first window of size k
        current_ones = sum(extended_data[:k])
    
        # Initialize maximum number of 1's in a window
        max_ones_in_window = current_ones
    
        # Step 4: Use sliding window technique to find max number of 1's in any window of size k
        for i in range(k, len(extended_data)):
            current_ones += extended_data[i] - extended_data[i - k]
            max_ones_in_window = max(max_ones_in_window, current_ones)
    
        # Step 5: The result is the difference between k and max_ones_in_window
        return k - max_ones_in_window
            
