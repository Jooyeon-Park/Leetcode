class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,k,writing_index = m-1, n-1, m+n-1

        while k>=0:
            if i <0 or nums1[i] <= nums2[k]:
                nums1[writing_index] = nums2[k]
                k -= 1
            else:
                nums1[writing_index] = nums1[i]
                i -= 1

            writing_index -= 1
            


