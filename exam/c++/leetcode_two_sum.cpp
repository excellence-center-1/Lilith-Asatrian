#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         for (int i = 0; i < nums.size()-1; ++i) {
//             for (int j = i + 1; j < nums.size(); ++j) {
//                 if (nums[i] + nums[j] == target) {
//                     return {i,j};
//                 }
//             }
//         }
//         return {};
//     }
// };
class Solution{
    public:
        vector<int> twoSum(vector<int>& nums, int target){
            unordered_map<int, int> table;
            for(int i = 0; i<nums.size(); ++i){
                table[nums[i]]=i;
            }
            for(int i = 0; i<nums.size(); ++i){
                int complement = target-nums[i];
                if(table.count(complement) && table[complement]!=i)
                    return {i, table[complement]};
            }
            return {};
        }
};