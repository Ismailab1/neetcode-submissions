class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int,int> differences;

        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];

            if (differences.find(diff) != differences.end()) {
                return {differences[diff], i};
            }

            differences.insert({nums[i], i});
        }
    }
};
