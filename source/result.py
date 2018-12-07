import cplex





# X - input  vector
# Y - output vector
# |X[i] - Y[i]| <= d -> X[i] - Y[i] <= d and Y[i] - X[i] <= d
#

class CplexOptimization():
    
    def __init__(self):
        
        self.instance    = cplex.Cplex()
        self.constraints = []
        self.senses      = []
        self.names       = []
        
        
    def add_senses(self):
        pass
    
    
    
    def add_constraints(self):
        pass
    
    
    def add_names_inputs(self):
        self.names_inputs=[]
        for i in range(2*28*28):
            self.names_inputs.append('input_'+str(i))
            
        
        
        
    
    
    