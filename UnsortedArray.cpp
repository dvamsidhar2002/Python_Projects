#include<iostream>

using namespace std;

int main()
{
	int n,i,j,key;
	cout<<"Enter the size of the array - ";
	cin>>n;
	int uns_arr[n];
	cout<<"Enter the values in the array -";
	for(i=0;i<n;i++)
	{
		cin>>uns_arr[i];
	}
	
	for(i=1;i<n;i++)
	{
		key=uns_arr[i];
		j=i-1;
		while(j>=0&&uns_arr[j]>key)
		{uns_arr[j+1]=uns_arr[j];
		j=j-1;}
		uns_arr[j+1]=key;
	}
	
	for(i=0;i<n;i++)
	{
		cout<<uns_arr[i]<<" ";
	}
	
	
		cout<<"\n\n"<<"Smallest element in array : "<<uns_arr[0]<<endl<<"Largest element in array : "<<uns_arr[n-1];
	
	
return 0;	
}
