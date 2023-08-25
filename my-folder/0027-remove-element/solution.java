class Solution {
    public int removeElement(int[] nums, int val) {
        int j;
        int index=0;
        int[] nums3=new int[100];
        for(j=0;j<(nums.length);j++)
        {
            if (nums[j]!=val)
            {
                nums[index]=nums[j];
                index++;
            }
            
        }
        
        
        return index;
    }
}
