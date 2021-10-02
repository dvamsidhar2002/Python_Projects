#include<iostream>

using namespace std;

int main()
{
	int r,i,j,k,t=1;
	cout<<"Enter no. of rows you want : ";
	cin>>r;
	for(i=1;i<=r;i++)
	{
		for(j=0;j<r-i;j++)
		
			cout<<"   ";
			k=(i*2)-1;
			for(j=0;j<k;j++)
			{
				if(t>99)
				cout<<t;
				else if(t<10)
				cout<<"  "<<t;
				else 
				cout<<" "<<t;
				t++;
			}
			cout<<"\n";
		
		
	}
	return 0;
}
