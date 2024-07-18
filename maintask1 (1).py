

#criating a list
my_list = [1,2,3,4,5]

#Adding an element to the List
my_list.append(6)

#Removing an element from the list
my_list.remove(3)

#Modifying an element in thr list 
my_list[0] =10

print("Updated List:" , my_list)


# In[2]:


#Creating a dictionary
my_dict = {'name' : 'John', 'age' :25, 'city' : 'Delhi'}

#Adding 
my_dict['gender'] = 'Male'

#Removing 
del my_dict['age']

#Modifying 
my_dict['city'] = 'Mumbai'

print("Updated Dictionary:" ,my_dict) 


# In[5]:


#creating a set 
my_set = {1,2,3,4,5}

#Adding 
my_set.add(6)

#Removing
my_set.remove(3)

#Modifying
my_set.discard(1)
my_set.add(10)

print("Updated Set:", my_set)





