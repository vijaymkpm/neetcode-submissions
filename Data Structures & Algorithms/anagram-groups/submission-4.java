class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new TreeMap<>();
        for (String s: strs)
        {
            char[] chars = s.toCharArray(); Arrays.sort(chars);
            map.computeIfAbsent("#"+new String(chars), k-> new ArrayList()).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
