#include <iostream>
#include <string>
#include <fstream>
using namespace std;
struct element
{
	string data;
	element* next;
	element*previous;
};
//amount of elements
int amount_of_elements(element*first)
{	
	int Number=0;
	element*current=first;
	if (first == NULL ){ return 0;}
	Number++;
	do
	{
		if(current->next==NULL)
		{
			break;
		}
		else
		{
			current = current->next;
			Number++;	
		}
	}
	while(true);
	return Number;
}
//function to add an item to the list
element* Add_Element(element*first,string New_Element)
{	
	if (first==NULL)
	{
		first = new element;
		first->next = first->previous = NULL;
		first->data=New_Element;
		return first;
	}
	else
	{
		element*temp;
		element*current=first;
		while (current->next != NULL)
		{
			current = current->next;
		}	
		current->next = new element;
		temp = current;
		current = current->next;
		current->previous = temp;
		current->next = NULL;
		current->data = New_Element;
		return first;
	}
}
//function to display the list on the screen
void Show_List(element*first)
{	
	cout<<"\nYour List:\n";
	if (first==NULL)
	{
		cout<<"Empty";
	}
	else
	{
		element*current=first;
		do
		{
			cout<<current->data<<endl;
			if(current->next==NULL)
			{
				break;
			}
			else
			{
				current = current->next;	
			}
		}
		while(true);
	}
	
}
//function for deleting the list
void Delete_List(element*first)
{ 
	if (first==NULL)
	{
		cout<<"\nList is Empty";
	}
	else
	{
		element*temp;
		element*current=first;
		while(current->next != NULL)
		{
			current = current->next;
		}
		while(current->previous != NULL)
		{
			temp = current;
			current = current->previous;
			delete temp;
		}
		delete first;		
	}

}
//function for deleting the element
element* Delete_Element(element*first,int number_of_element)
{
	element*temp;
	element*Temp;
	element*current=first;
	if(number_of_element < 0 or number_of_element > amount_of_elements(first) or first ==NULL)
	{
		cout<<"Uncorrect delete"; 
		return first;
	}
	if(number_of_element == 0)
	{
		if(amount_of_elements(first)!=1)
		{
			temp=first;
			first=current;
			current=current->next;
			first=current;
			first->previous=NULL;
			delete temp;
			return first;	
		}
		else
		{
			delete first;
			return NULL;	
		}
		temp=first;
		first=current->next;
		first->previous=NULL;
		delete temp;
		return first;
	}
	else
	{
		int index_of_element = 0;
		while(index_of_element <(number_of_element -1))
		{
			current=current->next;
			index_of_element++;
		}
		if(number_of_element == (amount_of_elements(first)-1))
		{
			temp = current->next;
			current->next = NULL;
			delete temp;
			return first;
		}
		else
		{
			temp = current;
			Temp=current->next;
			current = current->next;
			current = current->next;
			current->previous=temp;
			temp->next = current;
			delete Temp;
			return first;
		}
	}
}
//Tasks
element* first_task(element*first)
{
	cout<<"\nFirst Task";
	element*current=first;
	string temp;
		do
		{	
			temp="";
			if ((current->data).length() % 2 == 1)
			{	
				for(int index=1; index < (current->data.length()-1); index++)
				{
					temp+=current->data[index];		
				}
				current->data = temp;	
				cout<<endl<<current->data;
			}
			if(current->next==NULL)
			{
				break;
			}
			else
			{
				current = current->next;	
			}

		}
		while(true);
		if(first->data.length() %2 ==1)
		{
				for(int index=1; index < (first->data.length()-1); index++)
				{
					temp+=first->data[index];		
				}
				first->data = temp;	
		}
		return first;
}
bool check_for_alphabet(string word)
{
	string alphabet="abcdefghijklmnopqrstuvwxyz",temp="";	
	for( int index = 0; index<word.length() ;index++)
	{
		temp+=alphabet[index];
	}
	if(temp==word)
	{
		return true;	
	}
	else
	{
		return false;
	}		
}
element* second_task(element*first)
{
	element*current=first;
	cout<<"\n"<<"Second Task"<<"\n";
	do
	{
		if((current->data != first->data) and check_for_alphabet(current->data))
		{
			current->data+=".";
			current->data.replace(0,1,"");
			cout<<current->data<<endl;
		}
		if(current->next==NULL)
		{
			break;
		}
		else
		{
			current = current->next;	
		}
	}
	while(true);
	return first;	
}
element* third_task(element*first)
{
	element*current=first;
	cout<<"\n"<<"Third Task"<<"\n";
	do
	{
		if(current->data[0] != first->data[0])
		{
			for(int index = 0 ; index < current->data.length(); index++)
			{
				if(current->data[index]=='a' or current->data[index]=='o' ) current->data.replace(index,1,"");
			}
			cout<<current->data<<endl;
		}
		if(current->next==NULL)
		{
			break;
		}
		else
		{
			current = current->next;	
		}
	}
	while(true);
	return first;
}
element* fourth_task(element*first)
{
	if(amount_of_elements(first) <=2) cout<<"\n"<<"fewer than two words"<<"\n";
	element*current=first;
	string temp;
	cout<<"\n"<<"Fourth Task"<<"\n";
	do
	{
		if(current->data != first->data)
		{			
			if(current->data.length() % 2 == 0)
			{
				temp=current->data[0];
				temp+=temp;
				current->data.replace(0,1,temp);
			}
			else
			{
				current->data.replace((current->data.length()-1),1,"");
			}
			cout<<current->data<<endl;
		}
		if(current->next==NULL)
		{
			break;
		}
		else
		{
			current = current->next;	
		}
	}
	while(true);
	return first;
}
int main()
{
	string temp_string;
	element *first,*current;
	int number_of_task;
	ifstream in("data.txt");
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
		first = new element;
		first->next = first->previous = NULL;
		first->data=temp_string;
  	}
	while(!in.eof())
	{ 
		in>>temp_string;
		Add_Element(first,temp_string);
	}			
	Show_List(first);/*
	cout<<"\n"<<"enter job number: ";
	cin>>number_of_task;
	switch(number_of_task)
	{
		case 1: 
		{
			first = first_task(first); 
			break;
		}
		case 2: 
		{
			first = second_task(first); 
			break;
		}
		case 3: 
		{
			first = third_task(first); 
			break;
		}
		case 4: 
		{
			first = fourth_task(first); 
			break;
		}
		default: cout<<"\n"<<"invalid job number"<<"\n";
	}*/
	first = Delete_Element(first,0);
	first = Delete_Element(first,0);
	first = Delete_Element(first,0);
	first = Delete_Element(first,0);
	Show_List(first);
	Delete_List(first);
	return 0;
}
