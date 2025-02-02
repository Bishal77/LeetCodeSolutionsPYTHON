class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        int j = n-1;

        while(j >= 0){
            
            
            if(digits[j]==9){
                digits[j]=0;
                j--;
            }
            else
                break;
        }

        if(j==-1){
            digits.insert(digits.begin(), 1);
        }
        else
            digits[j]++;
        return digits;
    }
};