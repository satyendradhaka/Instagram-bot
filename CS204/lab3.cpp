#include<bits/stdc++.h>
using namespace std;

int check (string b)
{	
	stack <char> a;

	int k = 1;
	int i = 0;

	while(b[i] != '\0')
	{
		if(b[i] == '(' || b[i] == '{' || b[i] == '[' || b[i] == '<')
		{
			a.push(b[i]);
		}

		else if(b[i] == '|')
		{
			if(a.empty() || a.top() == '(' || a.top() == '[' || a.top() == '<' || a.top() == '{')
				a.push(b[i]);

			else
			{	
					a.pop();
			}
		}

		else if(b[i] == ')')
		{	
			if(!a.empty())
			{
				char c = a.top();
			 	if(c!='(')
				{
					k = 0;
					break;
				}
				
				else
					a.pop();
			}

			else
			{
				k = 0;
				break;
			}
		}

		else if(b[i] == '}')
		{
			if(!a.empty())
			{
				char c = a.top();
			 	if(c!='{')
				{
					k = 0;
					break;
				}
				
				else
					a.pop();
			}

			else
			{
				k = 0;
				break;
			}
		}

		else if(b[i] == ']')
		{
			if(!a.empty())
			{
				char c = a.top();
			 	if(c!='[')
				{
					k = 0;
					break;
				}
				
				else
					a.pop();
			}

			else
			{
				k = 0;
				break;
			}
		}
	
		else if(b[i] == '>')
		{
			if(!a.empty())
			{
				char c = a.top();
			 	if(c!='<')
				{
					k = 0;
					break;
				}
				
				else
					a.pop();
			}

			else
			{
				k = 0;
				break;
			}
		}
	
		i++;
	}   

	if(!a.empty())
		k = 0;

 	return k;
}

int main(){

	string b;
	int n;
	cin >> n;

	for(int i=1; i<=n; i++)
	{
		cin >> b;
		if(check(b) == 1)
			cout << "YES\n";

		else
			cout << "NO\n";
	}

	return 0;
}
