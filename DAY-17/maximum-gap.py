class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        # Init bucket.
        max_val, min_val = max(nums), min(nums)
        gap = max(1, (max_val - min_val) / (len(nums) - 1))
        bucket_size = (max_val - min_val) / gap + 1
        bucket = [{'min':float("inf"), 'max':float("-inf")} \
                    for _ in xrange(bucket_size)]

        # Find the bucket where the n should be put.
        for n in nums:
            # min_val / max_val is in the first / last bucket.
            if n in (max_val, min_val):
                continue      
            i = (n - min_val) / gap
            bucket[i]['min'] = min(bucket[i]['min'], n)
            bucket[i]['max'] = max(bucket[i]['max'], n)
        
        # Count each bucket gap between the first and the last bucket.
        max_gap, pre_bucket_max = 0, min_val
        for i in xrange(bucket_size):
            # Skip the bucket it empty.
            if bucket[i]['min'] == float("inf") and \
                bucket[i]['max'] == float("-inf"):
                continue
            max_gap = max(max_gap, bucket[i]['min'] - pre_bucket_max)
            pre_bucket_max = bucket[i]['max']
        # Count the last bucket.
        max_gap = max(max_gap, max_val - pre_bucket_max) 
        
        return max_gap


class Solution2:
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
            
        num.sort()
        pre = num[0]
        max_gap = float("-inf")
        
        for i in num:
            max_gap = max(max_gap, i - pre)
            pre = i
        return max_gap
     
if __name__ == "__main__":
    print Solution().maximumGap([3, 1, 1, 1, 5, 5, 5, 5])
