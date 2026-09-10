class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;

        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int l = i + 1, r = nums.size() - 1;

            while (l < r) {
                if (nums[i] + nums[l] + nums[r] == 0) {
                    result.push_back({nums[i], nums[l], nums[r]});
                    int last_l = nums[l], last_r = nums[r]; 
                    while(nums[l] == last_l && l < r) l++;
                    while(nums[r] == last_r && l < r) r--;
                }
                else if (nums[i] + nums[l] + nums[r] < 0) {
                    l++;
                }
                else {
                    r--;
                }
            }
        }

        return result;
    }
};
