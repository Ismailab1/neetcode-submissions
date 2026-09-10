class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maximum_water = 0;

        int lo = 0;
        int hi = heights.size() - 1;

        while (lo < hi) {
            int width = hi - lo;
            int height = min(heights[lo], heights[hi]);

            int current_area = width * height;

            maximum_water = max(maximum_water, current_area);

            if (heights[lo] < heights[hi]) {
                lo++;
            }
            else {
                hi--;
            }
        }

        return maximum_water;
    }
};
