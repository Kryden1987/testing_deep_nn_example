import tensorflow        as tf










class NeuralNetwork():
    
    def __init__(self):
        
        self.model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)),
                                          tf.keras.layers.Dense(256),
                                          tf.keras.layers.ReLU(input_shape=(None,256)),
                                          tf.keras.layers.Dense(128),
                                          tf.keras.layers.ReLU(input_shape=(None,128)),
                                          tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
        
        self.model.compile(optimizer=tf.train.AdamOptimizer(),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
        
    
    def fit(self,X_train,y_train):
        self.model.fit(X_train, y_train, epochs=7)
        
        
    def get_layer_output(self,X):
        
        get_current_layer_output   = tf.keras.backend.function([self.model.layers[0].input],[self.model.layers[1].output])
        get_relu_layer_output      = tf.keras.backend.function([self.model.layers[0].input],[self.model.layers[2].output])
        get_next_layer_output      = tf.keras.backend.function([self.model.layers[0].input],[self.model.layers[3].output])
        get_relu_next_layer_output = tf.keras.backend.function([self.model.layers[0].input],[self.model.layers[4].output])
        
        
        return get_current_layer_output,get_relu_layer_output,get_next_layer_output,get_relu_next_layer_output 
    
    def get_weights(self,i):
        return self.model.layers[i].get_weights()
            
    def predict(self,X):
        return self.model.predict(X)

            
                
                
            
        
        
            
            
            
    
    
    