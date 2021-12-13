import time
from input_files import dfs_australia_states,dfs_australia_graph,dfs_america_states,dfs_america_graph
import random
from Node import Node


"""
Intialising the default values so that they can be used for finding
the answer for the various functions.
"""
colors_for_states = []
states_present = []
states = []
statedict={}
back_propagation = 0
"""
This function is used for initialisation of colors.
"""
def initialisation_of_colors(number_of_colors):
    for _ in range(number_of_colors):
        colors_for_states.append(random.randint(0,255))
    

"""
This function is used for the heuristic calculation of the 
states whether the current color can be used to assign to them or not.
"""
def heuristic_calc_dfs(dict_of_state1,dict_of_state,number_of_colors,present_con_states,objects,count,colors_origi):
    global back_propagation
    states_present.append(dict_of_state1.copy())
    for _ in range(len(present_con_states.next)):
        dict_of_state1[present_con_states.next[0].myname] = present_con_states.next[_].mycolor   
        temp_colors_origi = colors_origi.copy()
        if dict_of_state1.get(present_con_states.next[0].myname) in getcolors(dict_of_state[present_con_states.next[0].myname],dict_of_state1):
          continue 
        if count == len(objects) - 1:
            return 1,dict_of_state1
        back_propagation +=1
        adjust_adjacent_states(present_con_states.next[0].myname,temp_colors_origi,statedict,present_con_states.next[_].mycolor,objects)
        temp_colors_origi = sorted(temp_colors_origi,key=lambda k:len(k[1]))
        temp_colors_for_states = colors_for_states.copy()
        present_con_states.next[_].next = assigning_of_colors(states,count+1,number_of_colors,temp_colors_for_states)
        result = heuristic_calc_dfs(dict_of_state1,dict_of_state,number_of_colors,present_con_states.next[_],objects,count+1,temp_colors_origi)
        if result[0] == 1:
            return 1,dict_of_state
        continue
    return 0,dict_of_state

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
This function is used to adjust the neighbouring
states based on the colors that are available to assign to the states.
"""
def adjust_adjacent_states(new_state,color_origi,dict_of_state,assigned_colors,state_nodes):
    for _ in dict_of_state[new_state]:
            if assigned_colors in list(filter(lambda y:y[0]==_,color_origi))[0][1]:
                result=list(filter(lambda y:y[0]==_,color_origi))[0][1]
                result.remove(assigned_colors)


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
This function is used to assign the states with the 
random colors in the begning.
"""
def assigning_random_colors(number_of_colors):
    return tuple(colors_for_states)



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
This function is used to calculate the dfs without heurisitcs
"""
def calc_dfs_without_heuristic(dict_of_state1,dict_of_state,number_of_colors,present_con_states,objects,count):
    
    global back_propagation
    for _ in range(len(present_con_states.next)):
        dict_of_state1[present_con_states.next[0].myname] = present_con_states.next[_].mycolor   
        if dict_of_state1.get(present_con_states.next[0].myname) in getcolors(dict_of_state[present_con_states.next[0].myname],dict_of_state1):
            continue
        states_present.append(dict_of_state1.copy())   
        temp_list_of_colors = colors_for_states.copy()
        if count == len(objects) - 1:
            return 1,dict_of_state1

        present_con_states.next[_].next = assigning_of_colors(objects,count+1,number_of_colors,temp_list_of_colors)  
       
        ans = calc_dfs_without_heuristic(dict_of_state1,dict_of_state,number_of_colors,present_con_states.next[_],objects,count+1)
        if ans[0] == 1:
            return 1,dict_of_state1
        continue

    back_propagation = back_propagation + 1
    return 0,dict_of_state1 

"""
This is the driver function of the program 
where the execution starts in the program.
"""
if __name__ == "__main__":
    number_of_colors = 4
    initialisation_of_colors(number_of_colors)
    colors_for_states = ["red","blue","green","black"]
    n=int(input("Enter the input for America or Australia states to be considered \n 1.America States \n2.Australia States"))
    if(n==1):
        statedict = dfs_america_graph
      
        states = dfs_america_states
    elif(n==2):
        states=dfs_australia_states
        statedict=dfs_australia_graph
    i=int(input("Enter the method:\n1.DFS with heuristic \n2.DFS without heuristics"))
    
    colors_original = []
    for _ in states:
        colors_original.append([_,colors_for_states.copy()])

    head = init(states,statedict,number_of_colors)
    dict_of_states = {}
    now = time.time()
    if(i==1):
        result = heuristic_calc_dfs(dict_of_states,statedict,number_of_colors,head,states,0,colors_original)
    elif(i==2):
        result= calc_dfs_without_heuristic(dict_of_states,statedict,number_of_colors,head,states,0)
    then = time.time()
    iter = 0 
    for _ in result[1]:
        iter+=1
        if result[1][_] in getcolors(statedict[_],dict_of_states):
            print("THE COLORS COULD NOT BE ASSIGNED TO ALL THE VARIABLES")
    print(len(states_present))
    print("THE SOLUTION FOR THE SELECTED COUNTRY STATES IS THAT")
    print(result)
    print("NUMBER OF BACK TRACKING HAPPENED FOR FINDING THE ANSWER IS THAT: "+ str(back_propagation))
    print("THE RUNNING TIME OF THE DFS WITH HEURISTIC IS THAT" + str(then - now) + "seconds") 

    

