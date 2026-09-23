#include <iostream>
#include <string>
using namespace std;

bool isHappy(int x){
    string s = to_string(x);
    while(s.length() > 1){
        int sum = 0;
        for(int i=0;i<s.length();i++){
            sum += (s[i]-'0')*(s[i]-'0');
        }
        s = to_string(sum);
    }
    return s == "1";
}
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int count=0;
    for(int i=0;i<n;i++){
        if(isHappy(a[i])){
            cout<<a[i]<<" ";
            count++;
        }
    }
    cout<<count;
    return 0;
}
