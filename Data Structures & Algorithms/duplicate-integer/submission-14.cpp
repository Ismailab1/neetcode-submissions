class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dupes;

        for (int num : nums) {
            if (dupes.count(num)) {
                return true;
            }

            dupes.insert(num);
        }
        return false;
    }
};