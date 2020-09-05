# Implementation of Binary Search using Python: Binary Search needs sorted data to work
class Runner(object):
    def __init__(self, name, age, distance_ran):
        self.name=name
        self.age=age
        self.distance_ran=distance_ran
    
    def __str__(self):
        return f"{self.name} of age {self.age} ran {self.distance_ran} kms."

runners_list=[]
while(True):
    choice=input('Add a runner(Y/N): ')
    if choice in ('Y','y'):
        name=input('Enter name of the runner: ')
        age=input('Enter age of the runner: ')
        distance_ran=input('Enter the distance ran: ')
        try:
            distance_ran=int(distance_ran)
        except:
            print('Not a valid input for distance ran.')
        new_runner=Runner(name, age, distance_ran)
        runners_list.append(new_runner)
    else:
        break

# The runners_list needs sorting based on the name before we can apply binary search on it
def sort_runners(runners_list):
    for i, runner_i in enumerate(runners_list):
        for j, runner_j in enumerate(runners_list):
            if getattr(runner_i, 'name') < getattr(runner_j, 'name'):
                runners_list[i], runners_list[j]=runners_list[j], runners_list[i]
    return runners_list

runners_list=sort_runners(runners_list)

#Binary Search function using recursion
def binary_search(runner, runners_list):
    mid=len(runners_list)//2
    if(runner == getattr(runners_list[mid], 'name')):
        return runners_list[mid]
    elif(runner < getattr(runners_list[mid], 'name')):
        return binary_search(runner, runners_list[:mid])
    elif(runner > getattr(runners_list[mid], 'name')):
        return binary_search(runner, runners_list[mid:])
    else:
        return 'Not Found!'


search_runner=input('Enter Runner Name for search: ')
print(binary_search(search_runner, runners_list))