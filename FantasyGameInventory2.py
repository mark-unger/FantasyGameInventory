#!/usr/bin/env python
# coding: utf-8

# In[1]:


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','skull']



#adds items to dictionary or updates their totals if already in dictionary
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory:
            inventory.setdefault(i, 1)
        else:
            inventory[i] += 1
    


#displays the inventory#
def displayInventory(inventory):
    print("Inventory")
    item_total = 0
    for k, v in inventory.items():
        print (str(v) + ' ' + str(k))
        item_total += int(v)
    print("Total number of items: " + str(item_total))
    
    
addToInventory(inv, dragonLoot)   
displayInventory(inv)


# In[ ]:




