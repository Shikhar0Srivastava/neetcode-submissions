class MyHashSet {

    ArrayList<Integer> set;
    public MyHashSet() {
        set = new ArrayList<>();
    }

    public void add(int key) {
        int keyIndex = -1;
        int start = 0, end = set.size() - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (set.get(mid) == key) {
                keyIndex = key;
                break;
            } else if (set.get(mid) > key) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        if (keyIndex == -1) {
            set.add(key);
        }
        Collections.sort(set);
    }

    public void remove(int key) {
        int keyIndex = -1;
        int start = 0, end = set.size() - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (set.get(mid) == key) {
                keyIndex = mid;
                break;
            } else if (set.get(mid) > key) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        if (keyIndex != -1) {
            set.remove(keyIndex);
        }
    }

    public boolean contains(int key) {
        return set.contains(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */