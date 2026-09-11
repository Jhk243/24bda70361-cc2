from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Tortoise and Hare (cycle detection)
        slow = nums[0]
        fast = nums[0]
        
        # Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find entrance to the cycle (the duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow