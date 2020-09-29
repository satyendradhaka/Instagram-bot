#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    unsigned long long s1;
    cin>>s1;

    bool prime;
    if (s1==1 || s1==0)
        {
        cout<<"It is NOT a Prime Number";
        return 0;
        }

    prime=true;
    for(int i=2; i<=sqrt(s1);i++)
    {
        if(s1%i == 0)
        {
        prime=false;
        break;
        }
    }

    if (prime==true)
        cout<<"It is a Prime Number";
    else
        cout<<"It is NOT a Prime Number";
    return 0;
}