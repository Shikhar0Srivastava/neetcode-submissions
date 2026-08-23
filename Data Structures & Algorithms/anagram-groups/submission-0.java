class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answer = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();
        for (String s: strs) {
            int[] alphabets = new int[26];
            for (char c: s.toCharArray()) {
                alphabets[c - 'a']++;
            }
            String keyToMap = Arrays.toString(alphabets);

            List<String> currentGroup = map.getOrDefault(keyToMap, new ArrayList<>());
            currentGroup.add(s);
            map.put(keyToMap, currentGroup);
        }

        for (Map.Entry<String, List<String>> entry: map.entrySet()) {
            answer.add(entry.getValue());
        }
        return answer;
    }
}
