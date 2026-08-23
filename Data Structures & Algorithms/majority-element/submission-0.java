class Solution {
    public int majorityElement(int[] nums) {
        int majorElement = 0, majorityValue = 0;
        for (int i = 0; i < nums.length; i++) {
            if (majorityValue == 0) {
                majorElement = nums[i];
            }
            if (nums[i] == majorElement) {
                majorityValue++;
            } else {
                majorityValue--;
            }
        }
        return majorElement;
    }
}