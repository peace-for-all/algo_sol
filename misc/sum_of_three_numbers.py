#!/bin/python3

# Do we have a triplet, that sums to target number, in this array?

def find_sum_of_three(nums, target):
   nums.sort()

   for k,v in enumerate(nums):
      lo = k + 1
      hi = len(nums) - 1
      while lo < hi:
         s = v + nums[lo] + nums[hi]

         print(f"{v} + {nums[lo]} + {nums[hi]} = {s}, target {target}")

         if s == target:
            return True
         elif s < target:
            lo += 1
         elif s > target:
            hi -= 1

   return False

if __name__ == '__main__':
   r = find_sum_of_three([1, -1, 0] , -1)
   print(r)