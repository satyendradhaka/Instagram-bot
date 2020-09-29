#include<bits/stdc++.h>
using namespace std;
#define endl "\n"

int compare( string x, string y){
    string xy = x.append(y);
    string yx = y.append(x);

    return xy.compare(yx)>0?1:0;
}

int main()
{
    int t,n;
    cin>>t;
    int i,j,z;
    for(i=0;i<t;i++)
    {
        cin>>n;
        string a[n];
        for(j=0;j<n;j++)
        {
            cin>>a[j];
        }
        sort(a,a+n,compare);
        for( z = 0; z < n; z++)
        {
             cout<<a[z];
        }
        cout<<endl;
    }
  
return 0;
}
