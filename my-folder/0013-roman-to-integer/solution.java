class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> nmap = new HashMap<>();
        nmap.put('I',1);
        nmap.put('V',5);
        nmap.put('X',10);
        nmap.put('L',50);
        nmap.put('C',100);
        nmap.put('D',500);
        nmap.put('M',1000);
        int result =0;
        
       
            for(int i=0;i<s.length();i++)
            {
                char ch = s.charAt(i);
                
                if(i>0 && nmap.get(ch) > nmap.get(s.charAt(i-1)))
                {
                    result += nmap.get(ch) - 2*nmap.get(s.charAt(i-1));
                }
      
                else{
                    result += nmap.get(ch);}
            
            }
        return result;
}
}
