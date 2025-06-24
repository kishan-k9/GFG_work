class Solution {
    public static String maxSubseq(String s, int k) {
        // code here
        int n = s.length();
        int toKeep = n - k;
        StringBuilder stack = new StringBuilder();

        for (char c : s.toCharArray()) {
            while (stack.length() > 0 && k > 0 && stack.charAt(stack.length() - 1) < c) {
                stack.deleteCharAt(stack.length() - 1);
                k--;
            }
            stack.append(c);
        }

        // Only keep the required number of characters
        return stack.substring(0, toKeep);
    }
}