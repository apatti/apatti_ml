from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from sklearn.datasets import fetch_mldata

mnist = None
#mnist_sklearn = fetch_mldata("MNIST original",data_home="./MNIST_Orig")

def readDataTf(size):
    global mnist
    if mnist is None:
        mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

    return mnist.train.next_batch(size)
    pass

def readDataSK(size):
    global mnist
    if mnist is None:
        mnist = fetch_mldata("MNIST original",data_home="./MNIST_Orig")

    mnist

def main():
    x = tf.placeholder(tf.float32,[None,784])
    w = tf.Variable(tf.zeros([784,10]))
    b = tf.Variable(tf.zeros([10]))

    y = tf.nn.softmax(tf.matmul(x,w)+b) # implement model

    trueY = tf.placeholder(tf.float32,[None,10])

    #cross entrophy = -Sigma(trueY*log(y))
    cross_entrophy = tf.reduce_mean(-tf.reduce_sum(trueY*tf.log(y),reduction_indices=[1])) #reduction_indices=1 to add elements in 2nd dimension
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entrophy) #learning rate=0.5

    init = tf.initialize_all_variables()

    with tf.Session() as session:
        session.run(init)
        for i in range(1000):
            batchX,batchY=readDataTf(100)
            session.run(train_step,feed_dict={x:batchX,trueY:batchY})

        correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(trueY,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
        print(session.run(accuracy,feed_dict={x:mnist.test.images,trueY:mnist.test.labels}))

if __name__ == '__main__':
    main()