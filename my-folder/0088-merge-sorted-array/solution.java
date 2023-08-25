class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int j=0, i=m;j<n;j++)
        {
            nums1[i]=nums2[j];
            i++;
        }
        for (int w=0; w<(m+n)-1; w++){
            for (int y=0; y<m+n-w-1; y++){
                //if (nums1[y]==nums1[y+1])
                //{
                   //break;
                //}
                if(nums1[y]>nums1[y+1])
                {
                    int temp = nums1[y];
                    nums1[y]= nums1[y+1];
                    nums1[y+1]=temp;
                }
            }
        }
    }
}   
        
