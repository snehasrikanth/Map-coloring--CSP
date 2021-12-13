from input_files import heuristic_america_graph,heuristic_america_states,heuristic_australia_graph,heuristic_australia_state
import time
import random
from Node import Node


"""
Intialising the default values so that they can be used for finding
the answer for the various functions.
"""
colorlist = []
all_states = []
states = []
statedict={}
backtracks = 0
"""
THIS FUNCTION IS USED TO SELECT THE NEIGHBOURING
STATES IN GRAPH 
"""
def pick_big_state(legal_colors):
    for k in sorted(legal_colors, key=lambda k: len(legal_colors[k]), reverse=True):
        #print k
        return k

def update_neighbors(statechanged,legal_colors,statedict,color_assigned,states):
    for state in statedict[statechanged]:
            #print(state)
            if color_assigned in list(filter(lambda x:x[0]==state,legal_colors))[0][1]:
                list(filter(lambda x:x[0]==state,legal_colors))[0][1].remove(color_assigned)


def init_colors(n):
    for i in range(n):
        colorlist.append(random.randint(0,255))

def random_color(n):
    return tuple(colorlist)
"""
Building graph for the states
which can be traversed for assigning the values with
"""
def constructing_state_color_graph(num,numstates,states):
    colors = random_color(3)
    a = Node(colors[0],states[0])
    root = a
    mystates = {}
    for i in range(1,numstates,1):
        w = Node(colors[0],states[i])
        a.put_child(w)
        a.nextnode = w
        #a = w
        mystates[states[i]] = a

        for j in range(1,num,1):
            b = Node(colors[j])
            a.put_child(b)
        a = w
    print(root)
    print(root.next)
    print(root.next[1].next)

"""
This is the getter function for getting the corresponding 
colors of the states.
"""
def colors_getter_function(states,mystatedict):
    listcol = []
    for i in states:
        listcol.append(mystatedict.get(i,""))

    return listcol

"""
This function is used to assign the 
colors to the states so that we can generate 
colors for the states

"""
def assigning_colors_state(states,i,numcolors,colors):
    tlist = []
    #colors = random_color(numcolors)
    for j in range(numcolors):
        tlist.append(Node(colors[j],states[i]))

    return tlist

"""
This is used to calculate the heuristic value for 
assigning the colors to the states.
"""
def heuristic_function_colors(dict_of_state1,dict_of_state,number_of_colors,present_con_states,objects,count,colors_origi):
    global backtracks
    all_states.append(dict_of_state1.copy())
    for _ in range(len(present_con_states.next)):
        dict_of_state1[present_con_states.next[0].myname] = present_con_states.next[_].mycolor   
        temp_colors_origi = colors_origi.copy()
        if dict_of_state1.get(present_con_states.next[0].myname) in colors_getter_function(dict_of_state[present_con_states.next[0].myname],dict_of_state1):
          continue 
        if count == len(objects) - 1:
            return 1,dict_of_state1
        backtracks +=1
        update_neighbors(present_con_states.next[0].myname,temp_colors_origi,statedict,present_con_states.next[_].mycolor,objects)
        temp_colors_origi = sorted(temp_colors_origi,key=lambda k:len(k[1]))
        temp_colors_for_states = colorlist.copy()
        present_con_states.next[_].next = assigning_colors_state(states,count+1,number_of_colors,temp_colors_for_states)
        result = heuristic_function_colors(dict_of_state1,dict_of_state,number_of_colors,present_con_states.next[_],objects,count+1,temp_colors_origi)
        if result[0] == 1:
            return 1,dict_of_state
        continue
    return 0,dict_of_state

"""
Reading the nodes and initialising 
with the colors from the list.
"""
def init(states,statedict,numcolors):
    colors = colorlist
    root = Node(colors[0],states[0])
    for j in range(numcolors):
        root.put_child(Node(colors[j],states[0]))

    return root
"""
This is the main driver function where the user gives the input '
""" 
if __name__ == "__main__":
    numcolors = 4
    init_colors(numcolors)
    n=int(input("ENTER THE STATES THAT YOU WANT TO CONSIDER \n1.America State \n2.Australia State"))
    colorlist = ["red","blue","green","black"]
    if(n==1):
        statedict =heuristic_america_graph
       
        states = heuristic_america_states
    elif(n==2):
        statedict = heuristic_australia_graph
        states= heuristic_australia_state

    legal_colors = []

    for state in states:
        legal_colors.append([state,colorlist.copy()])
    mystatedict = {}
    root = init(states,statedict,numcolors)
    start_time = time.time()
    answer = heuristic_function_colors(mystatedict,statedict,numcolors,root,states,0,legal_colors)
    end_time = time.time()
    count = 0 
    for key in answer[1]:
        count+=1
        if answer[1][key] in colors_getter_function(statedict[key],mystatedict):
            print("We are not able to assign the colors for the states in the graph ")
    print("THE COLORS ASSIGNED FOR THE STATES OF THE GRAPH ARE: ")
    print(answer)
    print("THE NUMBER OF EXECUTION THAT HAPPENED IN THE PROGRAM "+ str(backtracks))
    print("THE TOTAL RUNTIME OF THE PROGRAM" + str(end_time - start_time) + " seconds") 

    

