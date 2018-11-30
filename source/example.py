import argparse
import sys
import os
import tensorflow as tf
import matplotlib

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


    
    input_layer       = 800
    number_neurons_1  = 400
    number_neurons_2  = 200
    number_neurons_3  = 100
    number_neurons_4  = 64
    number_target     = 10
    
    X = tf.placeholder(name="in",dtype=tf.float32, shape=[None, input_layer])
    
    sigma = 1
    weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale=sigma)
    bias_initializer   = tf.zeros_initializer()
    
    W_hidden_1    = tf.Variable(weight_initializer([input_layer, number_neurons_1]))
    bias_hidden_1 = tf.Variable(bias_initializer([number_neurons_1]))
    
    W_hidden_2    = tf.Variable(weight_initializer([number_neurons_1, number_neurons_2]))
    bias_hidden_2 = tf.Variable(bias_initializer([number_neurons_2]))
    
    W_hidden_3    = tf.Variable(weight_initializer([number_neurons_2, number_neurons_3]))
    bias_hidden_3 = tf.Variable(bias_initializer([number_neurons_3]))

    W_hidden_4    = tf.Variable(weight_initializer([number_neurons_3, number_neurons_4]))
    bias_hidden_4 = tf.Variable(bias_initializer([number_neurons_4]))

    W_output      = tf.Variable(weight_initializer([number_neurons_4, number_target]))
    bias_output   = tf.Variable(bias_initializer([number_target]))


    hidden_1      = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1),        bias_hidden_1))
    hidden_2      = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
    hidden_3      = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))
    hidden_4      = tf.nn.relu(tf.add(tf.matmul(hidden_3, W_hidden_4), bias_hidden_4))
     
    output        = tf.transpose(tf.add(tf.matmul(hidden_4, W_output), bias_output))

    out           = tf.identity(output, name="out")
    
    init          = tf.global_variables_initializer()
    saver         = tf.train.Saver()
    
    with tf.Session() as sess:
        
        sess.run(init)
        save_path = saver.save(sess, './tmp/model.ckpt')
     
     
  
     

if __name__=="__main__":
    main()
