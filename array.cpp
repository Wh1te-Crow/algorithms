#include "iostream"
#include <string>
#include <fstream>
using namespace std;
class array_of_string
{
	protected:
		int ammount;
		string*array;
	public:
		array_of_string()
		{
			array = new string[1];
			array[0]='0';
			ammount = 1;	
		}
		void delete_element()
		{
			if(ammount!= 0)
			{
				ammount--;
				string*temp = new string[ammount];
				for(int i=0; i<ammount; i++)
				{
					temp[i]=array[i];
				}
				delete []array;
				array = new string[ammount];
				for(int i=0; i<ammount; i++)
				{
					array[i]=temp[i];
				}	
			}
			else
			{
				cout<<"\nEmpty\n";
			}

		}
		void add_element(string new_element)
		{
			string*temp = new string[ammount];
			for(int i=0; i<ammount; i++)
			{
				temp[i]=array[i];
			}
			delete []array;
			array = new string[ammount+1];
			for(int i=0; i<ammount; i++)
			{
				array[i]=temp[i];
			}
			array[ammount]=new_element;
			ammount++;
		}
		void task()
		{
			string temp;
			for(int i=1; i<ammount; i++)
			{
				if(array[i]==array[0])
				{
					temp=(array[i])[0];
					temp+=(array[i])[array[i].length()-1];
					cout<<temp<<"\n";
				}
			}
			
		}
		void show_array()const
		{
			if(ammount ==0)
			{
				cout<<"\nEmpty\n";
			}
			else
			{
				cout<<"\nYour List:\n";
				for(int i=0; i<ammount; i++)
					cout<<array[i]<<"\n";		
			}
		}
		void First_Task()
		{
			string temp_string;
			cout<<"\nFirst Task\n";
			for(int i=0; i<ammount; i++)
			{
				if(array[i].length()%2==1)
				{
					temp_string = "";
					for(int j=1; j<array[i].length()-1; j++)
						temp_string += (array[i])[j];
					cout<<temp_string<<"\n";
				}
			}
		}
		~array_of_string()
		{
			delete[]array;
		}		
};
int main()
{
	
	array_of_string text;
	text.delete_element();
	text.show_array();	
	string temp_string;
	ifstream in("text.txt");
   	if(!in)
   	{ 
	   cout << "file error!";
    	return 0;
   	}
   	if(!in.eof())
   	{
		in>>temp_string;
		if(temp_string=="")
		{
			cout<<"Your file is Empty";
			return 0;
		}
		text.add_element(temp_string);			
  	}
	while(!in.eof())
	{ 
		in>>temp_string;
		text.add_element(temp_string);
	}
	text.show_array();
	cout<<"---\n";
	//text.task();
	text.First_Task();	
		
	return 0;
}
