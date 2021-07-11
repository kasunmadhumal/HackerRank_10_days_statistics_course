
import statistics
import collections

#input list size
sizeOfNumList = int(input())

#input elements in list
NumList = list(map(int, input().split()))





#calculate mean using statistics library(it's very easy way to find mean,median and mode)
mean = statistics.mean(NumList)

''' clear algorithm for calculate mean

mean = sum(NumList) / len(NumList)

'''





#calculate median using statistics library

median = statistics.median(NumList)

''' clear algorithm for calculate median 
In this point my opinion is don't waste  time to find list length is odd or even
    
    l = int((len(num)-1)/2)
    u = int(len(num)/2)
    median = (num[l]+num[u])/2

'''





#in below codes i don't use statistics library for find mode(some errors generated for me...... try it your self)

#make a dictionary using colloections library 
# this dictionary contains each elementa and elements count
# list = [2,2,5,4,2,4,5,5,5,4,2]
# dic = {'2':4 , '5' : 4 , '4' : 3}
elements_count = collections.Counter(NumList)

#find max value of dictionary
max_val = max(elements_count.values())

#make dictionary keys and values to items 
# 'key' :value  = (key,value) 
dictionary_items = elements_count.items()

#sorted items list
sorted_items = sorted(dictionary_items)
for i in range(sizeOfNumList):
    
    #find key of max_val
    '''if we have multiple values to choose from, we want to select the smallest one.
    thats why after the first mode value loop is break'''
    if sorted_items[i][1] == max_val:
        mode = sorted_items[i][0]
        break
       
 
print(mean,'\n',median,'\n',mode)




    
        
        
