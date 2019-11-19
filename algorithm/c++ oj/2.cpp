#include <iostream>
using namespace std;

void get_time(int time, int t, int &yushu, int &shang){
    shang = time / t;
    yushu = time % t;
}

int main()
{
    int t;
    cin>>t;
    int m, time, t1, t2, m1, m2;
    int yushu, shang;
    int zhuru, paichu;
    int total;
    while (t != 0)
    {
        t--;
        cin >> m >> time >> m1 >> t1 >> m2 >> t2;

        get_time(time, t1, yushu, shang);
        cout<<shang<<" "<<yushu<<endl;
        if(shang % 2 == 0){
            zhuru = shang / 2 * t1 * m1 + yushu * m1;
        }
        else{
            zhuru = (shang+1) / 2 * t1 * m1;
        }
        cout<<zhuru<<endl;
        get_time(time, t2, yushu, shang);
        cout << shang << " " << yushu << endl;
        if (shang % 2 == 0)
        {
            paichu = shang / 2 * t2 * m2 + yushu * m2;
        }
        else
        {
            paichu = (shang+1) / 2 * t2 * m2;
        }
        cout<<paichu<<endl;
        total = zhuru - paichu;
        if(total <= 0){
            cout<< 0<<endl;
        }
        else if(total >= m){
            cout<<m<<endl;
        }
        else
        {
            cout<<total<<endl;
        }
    }
}