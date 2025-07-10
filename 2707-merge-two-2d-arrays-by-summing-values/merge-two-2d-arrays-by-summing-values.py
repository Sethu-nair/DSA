class Solution(object):
    def mergeArrays(self, nums1, nums2):
        result = []
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)

        # Iterate while both arrays have elements to compare
        while p1 < n1 and p2 < n2:
            id1, val1 = nums1[p1]
            id2, val2 = nums2[p2]

            # This block is now correctly indented to be INSIDE the while loop
            if id1 < id2:
                # The id from nums1 is smaller, add it and move its pointer
                result.append([id1, val1])
                p1 += 1
            elif id2 < id1:
                # The id from nums2 is smaller, add it and move its pointer
                result.append([id2, val2])
                p2 += 1
            else: # id1 == id2
                # IDs are the same, sum their values and move both pointers
                result.append([id1, val1 + val2])
                p1 += 1
                p2 += 1
        if p1 < n1:
            result.extend(nums1[p1:])
        if p2 < n2:
            result.extend(nums2[p2:])
        return result