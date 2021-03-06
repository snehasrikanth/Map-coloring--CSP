#THESE ARE THE INPUTS THAT ARE BEING USED FOR VARIOUS FUNCTIONS.
csp_singleton_america_states= ['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland', 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa', 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington', 'Delaware', 'colourado', 'Mississippi', 'Arkansas']
csp_singleton_america_graph ={
        'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],  
        'Arizona':['California', 'colourado', 'Nevada', 'New Mexico', 'Utah'],
        'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
        'California':['Arizona', 'Nevada', 'Oregon'], 
        'colourado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'], 
        'Connecticut':['Massachusetts', 'New York', 'Rhode Island'], 
        'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'], 
        'Florida':['Alabama', 'Georgia'], 
        'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],  
        'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'], 
        'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'], 
        'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'], 
        'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
        'Kansas' :['colourado', 'Missouri', 'Nebraska', 'Oklahoma'],
        'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
        'Louisiana':['Arkansas', 'Mississippi', 'Texas'], 
        'Maine':["New Hampshire"],
        "Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'], 
        'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
        'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'], 
        'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'], 
        'Mississippi':['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'], 
        'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'], 
        'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'], 
        'Nebraska' :['colourado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
        'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'], 
        'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
        'New Jersey':["Delaware", "New York", "Pennsylvania"], 
        'New Mexico':['Arizona', 'colourado', 'Oklahoma', 'Texas', 'Utah'], 
        'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'], 
        'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'], 
        'North Dakota':['Minnesota', 'Montana', 'South Dakota'], 
        'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'], 
        'Oklahoma' :['Arkansas', 'colourado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
        'Oregon':["California", 'Idaho', 'Nevada', "Washington"], 
        'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
        'Rhode Island':['Connecticut', 'Massachusetts', 'New York'], 
        'South Carolina':['Georgia', 'North Carolina'], 
        'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'], 
        'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'], 
        'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'], 
        'Utah':['Arizona', 'colourado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'], 
        'Vermont':['Massachusetts', 'New Hampshire', 'New York'], 
        'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'], 
        'Washington':['Idaho', 'Oregon'], 
        'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'], 
        'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'], 
        'Wyoming':['colourado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
        'Hawaii':[],
        'Alaska':[]}
csp_singleton_australia_states=['wa','nt','q','nsw','v','sa']
csp_singleton_australia_graph={
            'wa':['nt','sa'],
            'nt':['wa','q','sa'],
            'sa':['wa','q','nsw','nt','v'],
            'q':['nt','sa','nsw'],
            'nsw':['q','v','sa'],
            'v':['sa','nsw']
            }
dfs_america_graph = {
    'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
    'Arizona':['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
    'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
    'California':['Arizona', 'Nevada', 'Oregon'],
    'Colorado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
    'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
    'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
    'Florida':['Alabama', 'Georgia'],
    'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
    'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
    'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
    'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
    'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
    'Kansas' :['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
    'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
    'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
    'Maine':["New Hampshire"],
    "Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
    'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
    'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
    'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
    'Mississippi':['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
    'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
    'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
    'Nebraska' :['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
    'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
    'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
    'New Jersey':["Delaware", "New York", "Pennsylvania"],
    'New Mexico':['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
    'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
    'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
    'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
    'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
    'Oklahoma' :['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
    'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
    'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
    'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
    'South Carolina':['Georgia', 'North Carolina'],
    'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
    'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
    'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
    'Utah':['Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
    'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
    'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
    'Washington':['Idaho', 'Oregon'],
    'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
    'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
    'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah']
    }
dfs_america_states = ['Maine', 'Minnesota', 'South Dakota', 'Illinois', 'Utah', 'Wyoming', 'Texas', 'Idaho', 'Wisconsin', 'Connecticut', 'Pennsylvania', 'Kansas', 'West Virginia', 'North Carolina', 'Colorado', 'California', 'Florida', 'Vermont', 'Virginia', 'North Dakota', 'Michigan', 'New Jersey', 'Nevada', 'Arkansas', 'Mississippi', 'Iowa', 'Kentucky', 'Maryland', 'Louisiana', 'Alabama', 'Oklahoma', 'New Mexico', 'Rhode Island', 'Massachusetts', 'South Carolina', 'Indiana', 'Delaware', 'Tennessee', 'Georgia', 'Arizona', 'Nebraska', 'Missouri', 'New Hampshire', 'Ohio', 'Oregon', 'Washington', 'Montana', 'New York']
dfs_australia_states=['wa','nt','q','nsw','v','sa']
dfs_australia_graph={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}
fc_america_graph={
    'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
    'Arizona':['California', 'colourado', 'Nevada', 'New Mexico', 'Utah'],
    'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
    'California':['Arizona', 'Nevada', 'Oregon'],
    'colourado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
    'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
    'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
    'Florida':['Alabama', 'Georgia'],
    'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
    'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
    'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
    'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
    'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
    'Kansas' :['colourado', 'Missouri', 'Nebraska', 'Oklahoma'],
    'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
    'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
    'Maine':["New Hampshire"],
    "Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
    'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
    'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
    'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
    'Mississippi':['Alabama', 'Arkanssas', 'Louisiana', 'Tennessee'],
    'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
    'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
    'Nebraska' :['colourado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
    'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
    'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
    'New Jersey':["Delaware", "New York", "Pennsylvania"],
    'New Mexico':['Arizona', 'colourado', 'Oklahoma', 'Texas', 'Utah'],
    'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
    'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
    'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
    'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
    'Oklahoma' :['Arkansas', 'colourado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
    'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
    'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
    'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
    'South Carolina':['Georgia', 'North Carolina'],
    'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
    'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
    'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
    'Utah':['Arizona', 'colourado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
    'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
    'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
    'Washington':['Idaho', 'Oregon'],
    'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
    'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
    'Wyoming':['colourado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
    "Hawai":[],
    "Alaska":[]
    }
fc_america_states =['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland', 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa', 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington', 'Delaware', 'colourado', 'Mississippi', 'Arkansas']
fc_australia_states=['wa','nt','q','nsw','v','sa']
fc_australia_graph={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}

heuristic_america_graph={
'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
'Arizona':['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
'California':['Arizona', 'Nevada', 'Oregon'],
'Colorado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
'Florida':['Alabama', 'Georgia'],
'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
'Kansas' :['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
'Maine':["New Hampshire"],
"Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
'Mississippi':['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
'Nebraska' :['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
'New Jersey':["Delaware", "New York", "Pennsylvania"],
'New Mexico':['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
'Oklahoma' :['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
'South Carolina':['Georgia', 'North Carolina'],
'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
'Utah':['Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
'Washington':['Idaho', 'Oregon'],
'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah']
}
heuristic_america_states=['Illinois', 'Oklahoma', 'California', 'Utah', 'Wyoming', 'Missouri', 'Michigan', 'Texas', 'Iowa', 'Delaware', 'Tennessee', 'Maryland', 'Kentucky', 'Montana', 'Minnesota', 'Connecticut', 'Louisiana', 'West Virginia', 'Pennsylvania', 'Nebraska', 'Kansas', 'Indiana', 'Rhode Island', 'Arizona', 'Florida', 'Massachusetts', 'South Dakota', 'Nevada', 'South Carolina', 'Ohio', 'New Hampshire', 'Idaho', 'Washington', 'Colorado', 'Oregon', 'New Jersey', 'Mississippi', 'Arkansas', 'Vermont', 'Wisconsin', 'Alabama', 'Georgia', 'Maine', 'New Mexico', 'North Carolina', 'New York', 'Virginia', 'North Dakota']
heuristic_australia_graph={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}
heuristic_australia_state=['wa','nt','q','nsw','v','sa']
singleton_america_graph = {
        'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
        'Arizona':['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
        'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
        'California':['Arizona', 'Nevada', 'Oregon'],
        'Colorado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
        'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
        'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
        'Florida':['Alabama', 'Georgia'],
        'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
        'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
        'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
        'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
        'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
        'Kansas' :['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
        'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
        'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
        'Maine':["New Hampshire"],
        "Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
        'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
        'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
        'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
        'Mississippi':['Alabama', 'Arkanssas', 'Louisiana', 'Tennessee'],
        'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
        'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
        'Nebraska' :['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
        'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
        'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
        'New Jersey':["Delaware", "New York", "Pennsylvania"],
        'New Mexico':['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
        'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
        'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
        'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
        'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
        'Oklahoma' :['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
        'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
        'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
        'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
        'South Carolina':['Georgia', 'North Carolina'],
        'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
        'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
        'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
        'Utah':['Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
        'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
        'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
        'Washington':['Idaho', 'Oregon'],
        'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
        'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
        'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
        "Hawai":[],
        "Alaska":[]
        }
singleton_america_states= ['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland', 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa', 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington', 'Delaware', 'Colorado', 'Mississippi', 'Arkansas']

singleton_australia_graph={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}
singleton_australia_states=['wa','nt','q','nsw','v','sa']