#include <iostream>
#include<bits/stdc++.h> 
using namespace std; 

bool Smaller(string s1, string s2) 
{ 
	int n1 = s1.length(), n2 = s2.length(); 

	if (n1 < n2) 
	return true; 
	if (n2 < n1) 
	return false; 

	for (int i=0; i<n1; i++) 
	if (s1[i] < s2[i]) 
		return true; 
	else if (s1[i] > s2[i]) 
		return false; 

	return false; 
} 

string diff(string s1, string s2) 
{ 

	if (Smaller(s1, s2)) 
		swap(s1, s2); 

	string p = ""; 

	int n1 = s1.length(), n2 = s2.length(); 

	reverse(s1.begin(), s1.end()); 
	reverse(s2.begin(), s2.end()); 
	
	int c = 0; 

	for (int i=0; i<n2; i++) 
	{ 
		
		
		int sub = ((s1[i]-'0')-(s2[i]-'0')-c); 
		
	
		if (sub < 0) 
		{ 
			sub = sub + 10; 
			c = 1; 
		} 
		else
			c = 0; 

		p.push_back(sub + '0'); 
	} 


	for (int i=n2; i<n1; i++) 
	{ 
		int sub = ((s1[i]-'0') - c); 
		
	
		if (sub < 0) 
		{ 
			sub = sub + 10; 
			c = 1; 
		} 
		else
			c = 0; 
			
		p.push_back(sub + '0'); 
	} 

	reverse(p.begin(), p.end()); 

	return p; 
} 

int main() 
{ 
	string s1; 
	string s2; 
	getline(cin, s1);
	getline(cin, s2);
	cout << diff(s1, s2); 
	
	return 0; 
} 
