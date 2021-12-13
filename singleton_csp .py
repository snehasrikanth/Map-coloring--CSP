#CSP_singleton for American States and Australian States
states=[]
full = []
restriction_graph={}
back_propagation = 0
from copy import deepcopy
from input_files import csp_singleton_america_states,csp_singleton_america_graph,csp_singleton_australia_states,csp_singleton_australia_graph
import time

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
This function is used to get the available state from the current
state and seeing whether the states is currently traversed or not.
"""
def states_that_currently_available(objects):
    states_that_traversed=[]
    for _ in objects:
        if _.state_status=="not visited":
            states_that_traversed.append(_)
    return states_that_traversed

"""
This function is used to select the color from the list 
to find out whether there is any color available in the list or not.
"""
def colors_that_can_be_assigned(state,state_domain):
    domain_free=state_domain.copy()
    for _ in state.state_adjacent:
        color = _.colour_name
        if color!=None and (color in domain_free) :
            domain_free.remove(color)
    return domain_free

"""
This function is used to change the domain of the current state.
"""
def change_domain(state_object,color):
    for _ in state_object.state_adjacent:
        if (_.state_status=="not visited") and (color in _.state_domain):
            (_.state_domain).remove(color)

"""
This function is used to get the single domain status of the 
states of the graph.
"""           
def single_domain_states(objects):
    for _ in objects:
        if _.state_singleton==False and len(_.gettng_state_domain())==1:
            _.state_singleton=True
            color = _.state_domain[0]
            print("The singleton status of the current state.",_.state_domain)
            return _,color
    return None,None

"""
This function is used to generate the singleton propagation of 
each states.
"""
def singleton_propagtion(objects):
    print("The singleton propagation of the states")
    singleton_states={}
    while True:
        state,color = single_domain_states(objects)
        if state==None:
            return singleton_states,"The status of the singleton propagation is success"
        else:
            print("The singleton propagation of the",state.state_name)
            print("The domain status of the states is that",state.state_domain)
            singleton_states[state]=color
            for _ in state.state_adjacent:
                if _.state_status=="not visited" and color in _.state_domain:
                    print("The adjacent the state of the states "+_.state_name)
                    print("The domain adjacent of the state: ",_.state_domain)
                    if len(_.state_domain)==1:
                        print("The state",_.state_name)
                        #print(_.state_domain)
                        return singleton_states,"The singleton propagation is unsuccessfull"
                    (_.state_domain).remove(color)
                    print("The state domain status of the state is that : ",_.state_domain)

"""
THIS FUNCTION IS USED TO FOR ARRANGING COLORS FOR DIFFERENET STATES 
WHERE EACH STATES IS ASSIGNED WITH VALUE.
"""
def colour_arranging(domain,state_domain):
    domain_1=deepcopy(domain)
    domain_2=deepcopy(domain_1)
    state_domain=deepcopy(state_domain)
    for colour in dom:
        count=0
        for state_colour in state_domain:
            
            if colour!=state_colour:
        
                count+=1

        if count==len(state_domain):
           
            domain_2.remove(colour)

    return domain_2
                
"""
Assigning colors to the states
"""
def assigning_color(objects,color):
    print("The assigning colors to the state")

    states_updated=[]
    for _ in objects.state_adjacent:
        if _.state_status=="not visited" and color in _.state_domain:
            (_.state_domain).remove(color)
            states_updated.append(_)
    return states_updated

"""
Resetting the values of the status.
"""
def resetting_the_values(state,domain,color,states_updated):
    print("Inside the resetting method")
    color_position = domain.index(color)
    for _ in state.state_adjacent:
        if _.status=="not visited" and (_ in states_updated):
            (_.domain).insert(color_position,color)
            copy_of_domain= assigning_color(domain,_.state_domain)
            _.domain=deepcopy(copy_of_domain)

"""
Reversing the singleton propagation
"""
def resetting_the_singleton(singleton_states,domain,colour):
    print("The reversing the singleton propagation")
    for state,colour in singleton_states.items():
        temp_var = domain.index(colour)
        for _ in state.state_adjacent:
            if _.status=="not visited" and (_.is_singleton()):
                (_.domain).insert(temp_var,colour)
                domain_1 = colour_arranging(domain,_.domain)
                _.domain=domain_1
        state.state_singleton=False

"""
Constraint satisfaction problem function 
"""       
def constraint_satisfaction_function(state_objects,domain,states_and_colours):
        global back_propagation 
        if len(states_and_colours)==len(state_objects):
            return states_and_colours
        
        un_assigned_states=states_that_currently_available(state_objects)
        
        state=un_assigned_states[0]
        print(state.state_name)
        available_domain=deepcopy(state.state_domain)
        iter1 = 0
        for colour in available_domain:
            iter1+=1 
            state.state_status="visited"
            state.state_colour_name=colour
            states_and_colours[state.state_name]=colour
            
            updated_states=assigning_color(state,colour)
            print("total updated states",len(updated_states))
            singleton_states,status=singleton_propagtion(state_objects)
            print(len(singleton_states),status)
            
            if status!="unsucessful":
                result=constraint_satisfaction_function(state_objects,domain,states_and_colours)
            else:
                result=status
            if result!="unsucessful":
                return result
            del states_and_colours[state.state_name]
            state.colour_name=None
            state.status="not visited"
            
        
        back_propagation+=1
        return "unsucessful"

"""
Assigning the object.
"""        
def value_to_object(objects,domain_to_Values):
    temp_var = []
    dom=deepcopy(domain_to_Values)
    for _ in objects:
        cr_state_oj=State(_,dom)
        temp_var.append(cr_state_oj)
        dom=deepcopy(dom)
    return temp_var


"""
This is the main function
"""
def main():
    n=int(input("Enter the country for which states to be considered\n 1.America States \n2.Australia States"))
    if(n==2):
        
        states = csp_singleton_australia_states
        restriction_graph = csp_singleton_australia_graph
    elif(n==1):
        
        states = csp_singleton_america_states
        restriction_graph= csp_singleton_america_graph

    domain=["blue","green","black","red"]
    state_objects = value_to_object(states,domain)
    
    states_and_colours={}   
    for _ in state_objects:
        key = _.state_name
        values=restriction_graph[key]
        neighbours=[]
        for value in values:
            objects=[objects_form for objects_form in state_objects if objects_form.state_name==value ]   
            neighbours.append(objects[0])
            
        _.set_state_adjacent(neighbours)
    state_constraint=constraint_satisfaction_function(state_objects,domain,states_and_colours)
    print(state_constraint)
start_time = time.time()
main()
end_time = time.time()
print("NUMBER OF BACKTRACKING HAPPENED IN THE PROGRAM : " + str(back_propagation))
print()
print("THE TOTAL RUNNING TIME OF THE PROGRAM IS :" + str(end_time - start_time) + " SECONDS")

        










    
    

    
    

    
    
        
    
