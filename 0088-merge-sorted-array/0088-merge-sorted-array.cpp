class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1; // Index for nums1 (from the end of the valid elements)
        int j = n - 1; // Index for nums2 (from the end)
        int k = m + n - 1; // Index for the merged array (nums1)

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
        
    }
};