class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length == 0) {
            return 0;
        }
        int k = nums.length;
        int startIndex = 0, endIndex = nums.length - 1;
        while (nums[endIndex] == val) {
            k--;
            endIndex--;
            if (endIndex <= startIndex) {
                return 0;
            }
        }
        while (startIndex < endIndex) {
            if (nums[startIndex] == val) {
                k--;
                int temp = nums[startIndex];
                nums[startIndex] = nums[endIndex];
                nums[endIndex] = temp;
            }
            startIndex++;
            while (nums[endIndex] == val) {
                endIndex--;
                if (endIndex <= startIndex) {
                    break;
                }
            }
        }
        return k;
    }
}