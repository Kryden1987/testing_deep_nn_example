import cplex





# X - input  vector
# Y - output vector
# |X[i] - Y[i]| <= d -> X[i] - Y[i] <= d and Y[i] - X[i] <= d
#

class CplexOptimization():
    
    def __init__(self,X):
        
        self.number_layers = 2
        self.input_size    = len(X)
        self.X             = X
        
        self.constraints   = []
        self.rhs           = []
        self.senses        = []
        self.names         = []
        
       
        self.lower_bounds  = [0.0]            # d >= 0 
        self.upper_bounds  = [1.0]            # d <= 1
        
        self.lower_bounds.append(-cplex.infinity)
        self.upper_bounds.append( cplex.infinity)
    
        # variable with index == 0 is d
        self.variable_names = ['d']   
    
    
    
    
    
    def add_constraints(self):
        
        for i in range(self.input_size):
            
            add_constraints_x(i)
            

            
    # For layer                     - i
    # For neuron                    - k
    # For neurons in previous layer - j
    # x[i][k] = summ w[i-1][k][j] 
    
    def add_constraint(self,i,j):
        
        constraint = [ [] , [] ]
        
        constraint[0].append("x_"+str(i)+"_"+str(j))
        constraint[1].append(-1)
        
        for k in range(1, len(act[i-1])):
            constraint[0].append("x_"+str(i-1)+"_"+str(k))
            
        
        
    def add_constraints_x(self,i):
        
        # X[i+1] - X[i] <= d 
        self.constraints.append([[0, i+1], [-1, 1]])
        self.rhs.append(X[i])
        self.senses.append("L")
        self.names.append("x<=x"+str(i)+"+d")
        
        # X[i] - X[i+1] <= d
        self.constraints.append([[0, i+1], [1, 1]])
        self.rhs.append(X[i])
        self.senses.append("G")
        self.names.append("x>=x"+str(i)+"-d")
            
        # X[i] <= 1
        self.constraints.append([[i+1], [1]])
        self.rhs.append(1.0)
        self.senses.append("L")
        self.names.append("x<=1")
        
        # X[i] <= 0
        self.constraints.append([[i+1], [1]])
        self.rhs.append(0.0)
        self.senses.append("G")
        self.names.append("x>=0")
        
    
    def solver(self):
        
        problem = cplex.Cplex()
        
        problem.variables.add(obj = objective,lb = self.lower_bounds,ub = self.upper_bounds,names = variable_names)
        
        problem.linear_constraints.add(lin_expr=self.constraints,senses = self.senses,rhs = self.rhs,names = self.names)
        
        problem.solve()
            
    

        
        
        
    
    
    