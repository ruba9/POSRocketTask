import numpy 
# range function has 3 parameteres start of loop , the end not equal to , and increment
# you can refer to this article regarding range function https://www.pythoncentral.io/pythons-range-function-explained/

def readInputArray(InArr, size) :
    for i in range(0,size):
        InArr[i]=int(input("please enter a positive value"))
        while InArr[i] < 0:   # i assumed there is no negative summation ,
            print("negative values are invalid ") # your C code generate garabage values if we take negative inputs 
            InArr[i]=int(input("please enter a positive value"))
        

def GiveOutputArray(InArr,  OutArr,  size):
    sum=0
    for i in range(0,size):
        for j in range(InArr[i],-1 , -1 ): # for ( int j=InArr[i]; j>-1 , j--) equals j>=0  
            if j==0:
                sum+=j
                OutArr[i]=sum
                sum=0
            sum+=j



if __name__ == "__main__":
    size=4
    InputArray=numpy.empty(size, dtype=int) #this numpy array which works similar to C fixed array 
    OutputArray=numpy.empty(size, dtype=int) # python has no built in array type so we used numpy 
    readInputArray(InputArray,size)
    GiveOutputArray(InputArray,OutputArray,size)
    for i in range(0,size):
        print("[{}]".format(OutputArray[i]))