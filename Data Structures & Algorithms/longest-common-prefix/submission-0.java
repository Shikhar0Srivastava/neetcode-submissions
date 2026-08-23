class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs, Comparator.comparingInt(a -> a.length()));
        String prefix = strs[0];
        for (String s: strs) {
            int first = 0, second = 0;
            while (first < prefix.length() && second < s.length()) {
                if (prefix.charAt(first) != s.charAt(second)) {
                    prefix = s.substring(0, first);
                    break;
                }
                first++;
                second++;
            }
        }

        return prefix;
    }
}