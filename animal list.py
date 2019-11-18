animal_list = ['cat','goat','cat']
print("look at all the animals"+str(animal_list))

def my_function(new):

        if new=='':
            animal_list.pop()
        elif new in animal_list:
            
            return animal_list.remove(new)
        else:
            return animal_list.append(new)
        
            
while animal_list:
    new=input('enter the name of the animal:')
    if new.lower() =="quit":
        print("Good bye")
        break
    else:
        my_function(new)
        print(animal_list)
        
print("The list is empty")
