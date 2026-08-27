from solution import Solution

s = Solution()

def check(actual, expected, label):
    if actual != expected:
        print(f"FAIL [{label}]: got {actual}, expected {expected}")
    else:
        print(f"PASS [{label}]")


check(s.twoSum([2,7,11,15], 9), [1,0], "test1")
check(s.twoSum([3,2,4], 6), [2,1], "test2")
check(s.twoSum([3,3], 6), [1,0], "test3")