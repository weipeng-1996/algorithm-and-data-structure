#include<iostream>
using namespace std;
int coin[3] = {3,6,7}; 
int dp[19] ;
void dp_fun(int num)
{
	dp[0] = 0;
	for(int i=1;i<=num;i++)
	{
		dp[i] = 9999;
		for(int j=0;coin[j]<=i&&j<3;j++)
		{
			if(dp[i-coin[j]]+1 < dp[i])
				dp[i] = dp[i-coin[j]]+1;
		}
	} 
}
int main()
{
	dp_fun(18);		//表示要凑齐11元的硬币
	for(int i=0;i<19;i++)
	{
		cout<<"凑齐"<<i<<"元，至少需要"<<dp[i]<<"枚硬币"<<endl;
	} 
	return 0; 
}