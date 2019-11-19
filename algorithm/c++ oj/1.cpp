#include<iostream>
using namespace std;

void dec2bin(int num, int &count){
    for(int i = 31; i>=0; i--){
        if(num & (1<<i))
            count++;
    }
}
int main(){
    int t, n;
    cin>>t;
    int num;
    int count = 0;
    int judge[32] = {0};
    int c = 0;
    while(t!=0){
        t--;
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>num;
            dec2bin(num, count);
            judge[count]++;
            count = 0;
        }
        for (int i = 0; i < 32; i++)
        {
            if (judge[i] != 0){
                c++;
                judge[i] = 0;
            }
        }
        cout << c<<endl;
        c = 0;
    }
}