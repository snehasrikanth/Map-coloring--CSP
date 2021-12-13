import time
from input_files import singleton_america_graph,singleton_america_states,singleton_australia_graph,singleton_australia_states
import random
from Node import Node

"""
Intialising the default values so that they can be used for finding
the answer for the various functions.
"""
colors_for_states = []
states = []
statedict={}
states_present = []
back_propagation = 0

"""
Intialising the states to assign the corresponding colors to each state
so that we may not run into error.
"""
class State:
    """
    This is the constructor class for intialising the state object
    with the default.
    """
    def __init__(self,name,domain,status="not visited"):
        self.state_name=name
        self.state_colour_name=None
        self.state_singleton=False
        self.state_domain=domain
        self.state_adjacent=None
        self.state_status=status
       
        
    """
    Setting the states adjacent state to find the color of the
    current state.
    """
    def set_state_adjacent(self,state_adjacent):
        self.state_adjacent=state_adjacent
    """
    Getting the adjacent states object to know about their current
    state.
    """    
    def get_state_adjacent(self):
        return self.state_adjacent
    """
    Assigning color to the current state.
    """
    def assigning_colour(self,state_color):
        self.state_colour_name=state_color
    """
    Setting the state parent to know about the colors of the 
    parent and comparing with the descendents.
    """
    def set_state_predeccors(self,predeccors):
        self.parent=predeccors
    """
    Setting the state domain.
    """
    def setting_state_domain(self,state_domain):
        self.state_domain=state_domain
    """
    Getting the state_domain.
    These are the getters and the setters function.
    """
    def gettng_state_domain(self):
        return self.state_domain
    """
    To find the current state is singleton or not
    """
    def check_whether_singleton(self):
        if self.state_singleton:
            return self.state_singleton
        return False

"""
This function is used for initialisation of colors.
"""
def initialisation_of_colors(number_of_colors):
    for _ in range(number_of_colors):
        colors_for_states.append(random.randint(0,255))
"""
This function is used to assign the states with the 
random colors in the begning.
"""
def assigning_random_colors(number_of_colors):
    return tuple(colors_for_states)


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
THIS IS THE FUNCTION WHERE THE SINGLETON FUNCTION IS USED AND IMPLEMENTED SUCCESSFULLY.

"""
def singleton(dict_of_state1,dict_of_state,number_of_colors,pre_cond_state,states,count):
   
    global back_propagation
    states_present.append(dict_of_state1.copy())
    for i in range(len(pre_cond_state.next)):
        dict_of_state1[pre_cond_state.next[0].myname] = pre_cond_state.next[i].mycolor   
        if dict_of_state1.get(pre_cond_state.next[0].myname) in getcolors(dict_of_state[pre_cond_state.next[0].myname],dict_of_state1):
            #print("continued")
            continue
  
        if count == len(states) - 1:
            return 1,dict_of_state1

        temp_colorlist = colors_for_states.copy()
        remove_colors = getcolors(states[count+1],dict_of_state1)
        temp_colorlist = [x for x in temp_colorlist if x not in remove_colors]
        pre_cond_state.next[i].next = assigning_of_colors(states,count+1,number_of_colors,temp_colorlist)

        ans = singleton(dict_of_state1,dict_of_state,number_of_colors,pre_cond_state.next[i],states,count+1)
        if ans[0] == 1:
            return 1,dict_of_state1

        continue
        
    back_propagation +=1

    return 0,dict_of_state1 


"""
This function is used for intialising the states with the 
random colors so that we may have a start point for everything.
""" 
def init(objects,statedict,number_of_colors):
    colors_used = colors_for_states
    head = Node(colors_used[0],objects[0])
    for _ in range(number_of_colors):
        head.put_child(Node(colors_used[_],objects[0]))

    return head
if __name__ == "__main__":
    colors_for_states = ["red","blue","green","black"]
    number_of_colors = 4
    initialisation_of_colors(number_of_colors)

    
    n=int(input("Enter the input for America or Australia states to be considered \n 1.America States \n2.Australia States"))
    if(n==1):
        statedict = singleton_america_graph

        states = singleton_america_states
    elif(n==2):
        states=singleton_australia_states
        statedict  =singleton_australia_graph
    
    head = init(states,statedict,number_of_colors)
    dict_of_states = {}
    now = time.time()
    result = singleton(dict_of_states,statedict,number_of_colors,head,states,0)
    then = time.time()
    iter = 0 
    for _ in result[1]:
        iter+=1
        if result[1][_] in getcolors(statedict[_],dict_of_states):
            print("THE COLORS COULD NOT BE ASSIGNED TO ALL THE VARIABLES.")
    print(len(states_present))
    print("THE SOLUTION FOR THE SELECTED COUNTRY STATES IS THAT: ")
    print(result)
    print("NUMBER OF BACK TRACKING HAPPENED FOR FINDING THE ANSWER IS THAT: "+ str(back_propagation))
    print("THE RUNNING TIME OF THE SINGLETON WITH HEURISTIC IS THAT: " + str(then - now) + "SECONDS") 

    


