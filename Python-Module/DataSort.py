""" Tech Academy Drill Python Item 46
By Logan Boespflug Using Python 3.5.2
Date 11-13-2016
Sort Algorithm
"""

#Setting up Initial Inputs for Sorting
#Other Future version may switch this section to have it as user input
Input1=[67,45,2,13,1,998]
Input2=[89,23,33,45,10,12,45,45,45]

#Validating Initial Unsorted Data
print ("Initial Lists that have not been sorted:")
print (Input1)
print (Input2)

Unsorted=Input1

def MaxMin(Unsorted):
    results=[]
    while len(Unsorted)<>0: #Sorting based on popping off min value to new list
        entry=min(Unsorted)
        results.append(entry)
        Unsorted.remove(entry)
    Unsorted=results
    print (' ')
    print ('List in Order')
    return(Unsorted)
NewInput1=MaxMin(Unsorted)
print (NewInput1)

Unsorted=Input2
NewInput2=MaxMin(Unsorted)
print (NewInput2)

                
            
        
       

                
                
    
