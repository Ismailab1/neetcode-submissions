class Solution {
public:

    string encode(vector<string>& strs) {
        string coded = "";

        for (const string& word : strs) {
            coded += to_string(word.size()) + "#" + word;
        }

        return coded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;

        while (i < s.length()) {
            int j = i;

            while (j < s.length() && s[j] != '#'){
                j++;
            }

            int length = stoi(s.substr(i,j - i));

            string word = s.substr(j + 1, length);

            decoded.push_back(word);

            i = j + 1 + length;
        }

        return decoded;
    }
};
