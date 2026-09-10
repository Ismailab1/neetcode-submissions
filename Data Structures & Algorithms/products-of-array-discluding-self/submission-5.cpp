class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefixes(n);
        vector<int> postfixes(n);
        vector<int> result(n);

        prefixes[0] = 1;
        postfixes[n - 1] = 1;

        for (int i = 1; i < n; i++) {
            prefixes[i] = nums[i - 1] * prefixes[i - 1];
        }

        for (int i = n - 2; i >= 0; i--) {
            postfixes[i] = nums[i + 1] * postfixes[i + 1];
        }

        for (int i = 0; i < n; i++) {
            result[i] = postfixes[i] * prefixes[i];
        }

        return result;
    }
};
