import time
from input_files import fc_america_states,fc_america_graph,fc_australia_states,fc_australia_graph
import random
from Node import Node

"""
Intialising the default values so that they can be used for finding
the answer for the various functions.
"""
colors_for_states = []
states_present = []
back_propagation = 0
states = []
statedict={}

"""
This function is used for intialising the states with the 
random colors so that we may have a start point for everything.
""" 
def init(objects,statedict,number_of_colors):
    colors_used = colors_for_states
    value = Node(colors_used[0],objects[0])
    for j in range(number_of_colors):
        value.put_child(Node(colors_used[j],objects[0]))
    return value

"""
This function is used to assign the states with the 
random colors in the begning.
"""
def assigning_random_colors(number_of_colors):
    return tuple(colors_for_states)

"""
This function is used for initialisation of colors.
"""
def initialisation_of_colors(number_of_colors):
    for _ in range(number_of_colors):
        colors_for_states.append(random.randint(0,255))

"""
THIS FUNCTION IS USED TO GET THE STATE THEIR CURRENT
COLOR.    
"""
def getcolors(nodes_state,dict_of_state1):
    colors_of_list = []
    for _ in nodes_state:
        colors_of_list.append(dict_of_state1.get(_,""))
    return colors_of_list




"""
This function is used to generate the colors for the state and to 
create a node and assigning values to it.
"""
def assigning_of_colors(objects,k,number_of_colors,given_colors):
    temp_var = []
    for _ in range(number_of_colors):
        temp_var.append(Node(given_colors[_],objects[k]))
    return temp_var

"""
This function is used for the forward checking propagation of the 
graph.
"""
def checking_foward_propagation(dict_of_state1,dict_of_state,number_of_colors,present_cond_states,objects,count):

    global back_propagation
    colors_for_states.append(dict_of_state1.copy())
    for _ in range(len(present_cond_states.next)):
        time.sleep(0.000002)
        dict_of_state1[present_cond_states.next[0].myname] = present_cond_states.next[_].mycolor   
        if dict_of_state1.get(present_cond_states.next[0].myname) in getcolors(dict_of_state[present_cond_states.next[0].myname],dict_of_state1):
            
            continue  
        if count == len(objects) - 1:
            return 1,dict_of_state1

        tcolor_var_list = colourlist.copy()
        getting_color = getcolors(objects[count+1],dict_of_state1)
        tcolor_var_list = [x for x in tcolor_var_list if x not in getting_color]
        present_cond_states.next[_].next = assigning_of_colors(objects,count+1,number_of_colors,tcolor_var_list)

        result = checking_foward_propagation(dict_of_state1,dict_of_state,number_of_colors,present_cond_states.next[_],objects,count+1)
        if result[0] == 1:
            return 1,dict_of_state1
        continue
    back_propagation +=1

    return 0,dict_of_state1 




"""
This is the driver function of the program 
where the execution starts in the program.
"""
if __name__ == "__main__":
    numcolours = 4
    initialisation_of_colors(numcolours)

    colourlist = ["red","blue","green","black"]
    n=int(input("Enter the input for America or Australia states to be considered \n 1.America States \n2.Australia States"))
    if(n==1):
        statedict = fc_america_graph
        states = fc_america_states
    elif(n==2):
        states = fc_australia_states
        statedict  = fc_australia_graph
    
   
    dict_of_states = {}
    print(states)
    head = init(states,statedict,numcolours)
    iter = 0 
    now = time.time()
    result = checking_foward_propagation(dict_of_states,statedict,numcolours,head,states,0)
    then = time.time()
    
    for _ in result[1]:
        iter+=1
        if result[1][_] in getcolors(statedict[_],dict_of_states):
               print("THE COLORS COULD NOT BE ASSIGNED TO ALL THE VARIABLES")


    print("THE SOLUTION FOR THE SELECTED COUNTRY STATES IS THAT")
    print(result)
    print("NUMBER OF BACK TRACKING HAPPENED FOR FINDING THE ANSWER IS THAT: "+ str(back_propagation))
    print("THE RUNNING TIME OF THE DFS WITH HEURISTIC IS THAT" + str(then - now) + "seconds") 
    print("THE NUMBER OF THE COLORS ASSIGNED FOR THE ALL THE STATES",len(colors_for_states))
    time.sleep(10)
    


