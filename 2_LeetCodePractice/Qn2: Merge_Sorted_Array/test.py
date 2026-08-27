from solution import Solution

s = Solution()

def check(actual, expected, label):
    if actual != expected:
        print(f"FAIL [{label}]: got {actual}, expected {expected}")
    else:
        print(f"PASS [{label}]")


def check_merge(nums1, m, nums2, n, expected, label):
    s.merge(nums1, m, nums2, n)
    check(nums1, expected, label)


check_merge([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6], "test1")
check_merge([1], 1, [], 0, [1], "test2_empty_nums2")
check_merge([0], 0, [1], 1, [1], "test3_empty_nums1")
check_merge([2,0], 1, [1], 1, [1,2], "test4_nums2_goes_first")
check_merge([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6], "test5_nums2_all_smaller")
check_merge([-3,-1,0,0,0], 2, [-2,-1,4], 3, [-3,-2,-1,-1,4], "test6_negatives_and_duplicates")