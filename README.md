# POSRocketTask
I started coding using C++ because Im familiar with it, then I went to python tutorials to convert the code to python.

the following is my c++ code:
#include <iostream>

using namespace std;

void readInputArray(int InArr[], int size) { 
    for(int i=0; i < size; i++) {
        cout<<"please enter a positive value"<<endl;
        cin>>InArr[i]; 
        if(InArr[i] < 0) {
     cout<<"negative values are invalid"<<endl;
        }    
    }
    
}

void GiveOutputArray(int InArr[], int OutArr[], int size) {
    int sum =0;
    for(int i=0; i< size; i++) {
        for(int j=InArr[i]; j>=0 ; j--) {
            if(j == 0) {
                 sum+=j;
                 OutArr[i]=sum;
                 sum =0;
            }
      sum+=j;  } 
    }
}

int main()
{
    int size =4;
    int InputArray[size];
    int OutputArray[size];
    
    readInputArray(InputArray,size);
    GiveOutputArray(InputArray,OutputArray,size);
    
    for(int i = 0; i < size; i++) {
        cout<<"[ "<<OutputArray[i]<<" ] ";
    }
    

    return 0;
}


A task for POSRocket company as a python developer.
