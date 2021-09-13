class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)
        {
            return false;
        }
        else
        {
            int r=0;
            int rev=0;
            int org=x;
            while (x !=0)
            {
                r=x%10;
                rev=rev*10+r;
                x=x/10;
            }
            if (rev==org)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
