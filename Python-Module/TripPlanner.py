'''Trip Note Program written w/Python 2.7
By Logan Boespflug
Created 11-7-2016
'''

#Program will ask the user where they are going, how many days, and calculate the grand total

print 'Trip Planning Tool 1.0'
print ' '
Timeoff=raw_input('How many total days is your vacation?:')
Timeoff=int(Timeoff)
if Timeoff==1:
    print 'Are you sure you cannot go longer?'

Destination=raw_input('How many cities are you planning to visit?: ')
Destination=int(Destination) #This variable is used to define loop lengths for each Dictionary

#Section to initilize values going through functions (Ran into less problems this way)
Cities=[] #List of Cities
Summary={} #Dictionary for Internary
HPricing={} #Dictionary for Hotel Prices
TPricing={} #Dictionary for Travel Prices
GrandPricing=0
print ' '

#This part creates the list of cities the user is travelin too
if Destination>1:
    for x in range(0,Destination):
        City_input=raw_input('Name a single city:').upper()
        Cities.append(City_input)

#This function breaks down days for each city
def Internary(Summary):
    for x in range(0,Destination):
        Internary_input=raw_input('How many days spent at '+Cities[x]+'?:')
        Internary_input=int(Internary_input)
        Summary[Cities[x]]=Internary_input
    return Summary

#This function asks for hotel pricing at each city and travel price to that city
def Trips(HPricing,TPricing):
    for x in range(0,Destination):
        Travel_input=raw_input('How much does it cost to get to '+Cities[x]+'?: $')
        Hotel_input=raw_input('How much is hotel per night at '+Cities[x]+'?: $')
        print ' '
        Travel_input=int(Travel_input)
        Hotel_input=int(Hotel_input)
        HPricing[Cities[x]]=Hotel_input
        TPricing[Cities[x]]=Travel_input
    return HPricing,TPricing

IntSum=Internary(Summary)
Grand=Trips(HPricing,TPricing)
print ' '
print 'Days Recap:'
#This Breaks down the City List for a nice Summary
for x in Cities:
    print x +' For '+str(IntSum[x])+' Days'
    GrandPricing=GrandPricing+HPricing[x]*IntSum[x] #Calculate total for Lodging
print ' '
print 'Hotel Prices and Transporation Prices '
print Grand
print ' '
Movement=sum(TPricing.values())
print 'Total Price for Transporation :$'+str(Movement)
print 'Total Price for Lodging :$'+str(GrandPricing)





    

    

