import argparse
import sys
import os
import tensorflow as tf
import matplotlib
import nn

def cli():
    
    parser=argparse.ArgumentParser(description='My example for Testing Deep Neural Networks')
    
    parser.add_argument('-m','--model', action='store', nargs='+',      help='The input neural network model (.h5)')
    parser.add_argument('-c','--cover', metavar='ss',   action='store', help='The covering method: ss, sv, ds, dv', default='ss')

    args=parser.parse_args()
    

    
    
def main():
    
    cli()
    
    mnist = tf.keras.datasets.mnist
    
    (X_train, y_train),(X_test, y_test) = mnist.load_data()
    
    X_train, X_test = X_train / 255.0, X_test / 255.0
    
    z = nn.NeuralNetwork()
    
    z.fit(X_train,y_train)
    
    C,RC,N,RN = z.get_layer_output(X_test)
    
    
    
  
     

if __name__=="__main__":
    main()
