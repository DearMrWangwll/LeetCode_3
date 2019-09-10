class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> my_map;
        int length = s.size();
        int last = 0;int ans = 0;
        for (int i=0;i<length;++i){
            if (my_map.count(s[i])>0){
                last = max(my_map[s[i]],last);
            }
            ans = max(ans,i-last+1);
            my_map[s[i]] = i+1;
        }
        return ans;
    }
};
