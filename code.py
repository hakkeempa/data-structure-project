import pickle
import os
from dummy import calculate_recovery
from dummy import calculate_death

if os.path.exists("list1.pkl"):
    list1 = pickle.load(open("list1.pkl","rb"))
    list2 = pickle.load(open("list2.pkl","rb"))
    print(list1)
else:
    list1 = []
    list2 = []
    print(list1)

if(list1 == [] and list2 == []):
    list1.append(calculate_recovery)
    list2.append(calculate_death)
    pickle.dump(list1,open("list1.pkl","wb"))
    pickle.dump(list2,open("list2.pkl","wb"))
 
else:
    list1 = pickle.load(open("list1.pkl","rb"))
    list2 = pickle.load(open("list2.pkl","rb"))
    list1.append(calculate_recovery)
    list2.append(calculate_death)
    pickle.dump(list1,open("list1.pkl","wb"))
    pickle.dump(list2,open("list2.pkl","wb"))
    
print("Recovery percentage : ",list1)
print("Death percentage : ",list2)
