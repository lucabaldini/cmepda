from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import numpy as np
import tensorflow as tf

from scipy.optimize import minimize

tf.set_random_seed(1234)

fdtype = tf.float32

ntoys = 10

stddev = 1.0
theta_points = np.array([-1.0, 2.0, 0.0, 0.0, 0.0])
n_theta = theta_points.size
theta = tf.Variable( theta_points , trainable=False,  dtype=fdtype)
theta_hat_num = tf.Variable( theta_points,  dtype=fdtype, trainable=True)

x_points = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], dtype=np.float32)
n_x = x_points.size
x_vars = tf.constant( x_points, dtype=fdtype )

A = tf.constant([math.pow(x_points[i], j)/math.factorial(j) for i in range(n_x) for j in range(n_theta) ], dtype=fdtype)
A = tf.reshape(A, shape=(n_x,n_theta))
V = tf.diag( [(stddev*stddev)]*n_x )
Vinv = tf.matrix_inverse(V)
B = tf.matmul(A, Vinv, transpose_a=True)    

npA = np.array([math.pow(x_points[i], j)/math.factorial(j) for i in range(n_x) for j in range(n_theta) ]).reshape( (n_x,n_theta) )
npV = np.diag( [(stddev*stddev)]*n_x )
npVinv = np.linalg.inv(npV)
npB = np.matmul(npA.T, npVinv)

##########################
np.random.seed(1234)
rnd_data = np.random.multivariate_normal( np.matmul(npA, theta_points), npV, ntoys  )
np.save('data', rnd_data)
##########################

def fun(x, args):
    delta = args - tf.reshape(tf.matmul(A,tf.reshape(x,[n_theta,1])), shape=[n_x])
    delta = tf.reshape(delta, shape=[n_x,1])
    loss = tf.matmul( tf.matmul( delta, Vinv, transpose_a=True ), delta)
    return tf.reduce_sum(loss, -1)[0]/(n_x-n_theta)

def npfun(x, args):
    npy = args
    npdelta = npy - np.matmul(npA,x)
    nploss = np.matmul( np.matmul( npdelta.T, npVinv), npdelta )
    return np.sum(nploss)/(n_x-n_theta)

with tf.compat.v1.Session() as sess:
    #optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.01)
    optimizer = tf.compat.v1.train.AdagradOptimizer(learning_rate=0.01)
    #optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.00001)
    sess.run(tf.compat.v1.global_variables_initializer())

    y_vars = tf.matmul(A, tf.reshape(theta,[n_theta,1]))
    y_vars = tf.reshape(y_vars, shape=[n_x])
    print('theta:  ', sess.run(theta))
    print('x_vars: ', sess.run(x_vars))
    print('A-matrix:\n',sess.run(A))
    print('V-matrix:\n',sess.run(V))
    print('y_vars: ', sess.run(y_vars))

    try:
        data = np.load('./data.npy')
        dataset = tf.data.Dataset.from_tensor_slices(data)
        print(dataset.output_types)
        print(dataset.output_shapes)
        iterator = dataset.make_one_shot_iterator()
        next_element = iterator.get_next()
        itoy = 0
        while True:
            try:
                y_vars_rnd = next_element
                y = sess.run(y_vars_rnd)
                #print(y)
                ynp = np.array( [y[i] for i in range(n_x)] )
                res_BFGS = minimize(fun=npfun, x0=theta_points, args=ynp, method='BFGS')
                res_NM = minimize(fun=npfun, x0=theta_points, args=ynp, method='Nelder-Mead')
                res_CG = minimize(fun=npfun, x0=theta_points, args=ynp, method='CG')
                res_PO = minimize(fun=npfun, x0=theta_points, args=ynp, method='Powell')
                res_LBFGS = minimize(fun=npfun, x0=theta_points, args=ynp, method='L-BFGS-B')
                y_vars_rnd = tf.constant( y, dtype=fdtype)
                y_vars_rnd = tf.reshape(y_vars_rnd, shape=[n_x,1])
                theta_hat_ana = tf.matmul(tf.matmul(tf.matrix_inverse( tf.matmul(B,A) ), B), y_vars_rnd)    
                theta_hat_ana =  tf.reshape(theta_hat_ana,  shape=[n_theta])
                lossAna = fun(x=theta_hat_ana, args=tf.reshape(y_vars_rnd, [n_x]))
                print('Toy {}:'.format(itoy))

                delta = tf.reshape(y_vars_rnd, [n_x]) - tf.reshape(tf.matmul(A,tf.reshape(theta_hat_num,[n_theta,1])), shape=[n_x])
                delta = tf.reshape(delta, shape=[n_x,1])
                loss = tf.matmul( tf.matmul( delta, Vinv, transpose_a=True ), delta)
                lossNum = tf.reduce_sum(loss, -1)[0]/(n_x-n_theta)
                opt = optimizer.minimize(lossNum, var_list=[theta_hat_num])
            
                sess.run(tf.compat.v1.global_variables_initializer())
                for i in range(1000): sess.run(opt) 
                #print('POI\tLSQ          :', sess.run(theta_hat_ana))
                #print('POI\tSciPy - BFSG :', res_BFGS.x  )
                #print('POI\tSciPy - NM   :', res_NM.x  )
                #print('POI\tSciPy - CG   :', res_CG.x  )
                #print('POI\tSciPy - PO   :', res_PO.x  )
                #print('POI\tSciPy - LBFSG:', res_LBFGS.x  )
                #print('POI\tTF - Adagrad :', sess.run(theta_hat_num))
                print('-------------------------------------------------------------------')
                print('Loss\tLSQ          :', sess.run(lossAna))
                print('Loss\tSciPy - BFSG :', res_BFGS.fun  )
                print('Loss\tSciPy - NM   :', res_NM.fun  )
                print('Loss\tSciPy - CG   :', res_CG.fun  )
                print('Loss\tSciPy - PO   :', res_PO.fun  )
                print('Loss\tSciPy - LBFSG:', res_LBFGS.fun  )
                print('Loss\tTF - Adagrad :', sess.run(lossNum))
                itoy += 1
                
            except tf.errors.OutOfRangeError:
                print("End of dataset")
                break

    except:
        print('Not a file')
        
