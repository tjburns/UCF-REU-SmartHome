import tensorflow as tf
import pandas as pd
import scipy
import math
import numpy as np
from sklearn import preprocessing
from sklearn.utils import shuffle

global scalar

# data = pd.read_csv("valid.csv", header=None, skiprows=[0], usecols=(range(1, 13)))

data1 = pd.read_csv("valid.csv", header=None, skiprows=[0], usecols=(range(1, 2)))
data2 = pd.read_csv("valid.csv", header=None, skiprows=[0], usecols=(range(3, 13)))
frames = [data1, data2]
data = pd.concat(frames, axis=1)

data = shuffle(data.values)
train_size = math.floor(0.8 * len(data))
test_size = math.floor(0.1 * len(data))
valid_size = math.floor(0.1 * len(data))

training = data[0:train_size]
validating = data[train_size:train_size + valid_size]
testing = data[-test_size:]

training_x = training[:, 1:12]
scalar = preprocessing.StandardScaler().fit(training_x)
training_x = scalar.transform(training_x)
training_y = training[:, 0]
training = np.column_stack((training_y, training_x))

valid_x = validating[:, 1:12]
valid_x = scalar.transform(valid_x)
valid_y = validating[:, 0]

testing_x = testing[:, 1:12]
testing_x = scalar.transform(testing_x)
testing_y = testing[:, 0]

n_classes = 11  # features
batch_size = 16
hidden_layer = 64
x_ph = tf.placeholder('float', [None, n_classes - 1], name='x')
y_ph = tf.placeholder('float', [None, 1], name='y')
dropout_ph = tf.placeholder('float', [], name='dropout')


def next_batch(epoch, batch_size):
    global training
    start = epoch * batch_size
    end = epoch * batch_size + batch_size

    shuffleArray = shuffle(training)
    x = shuffleArray[:, 1:12]
    y = shuffleArray[:, 0]

    return x, y


def neural_network_model(data):
    # model = tf.keras.Sequential([
    #     tf.keras.layers.Dense(batch_size, activation=tf.nn.relu),
    #     tf.keras.layers.Dense(batch_size, activation=tf.nn.relu),
    #
    # ])

    layer1 = tf.layers.dense(data, hidden_layer, activation=tf.nn.relu)
    # dropout = tf.layers.dropout(layer1, 0.5)
    layer2 = tf.layers.dense(layer1, hidden_layer, activation=tf.nn.relu)
    layer3 = tf.layers.dense(layer2, hidden_layer, activation=tf.nn.relu)
    # layer4 = tf.layers.dense(layer3, batch_size, activation=tf.nn.relu)
    # dropout2 = tf.layers.dropout(layer2, 0.5)
    # layer3 = tf.layers.dense(dropout2, batch_size, activation=tf.nn.relu)
    # dropout3 = tf.layers.dropout(layer3)
    output = tf.layers.dense(layer3, 1)

    return output


def accuracy(x, y, data_size):
    acc = 0
    for i in range(0, data_size):
        if abs(x[i] - y[i]) < 0.2:
            acc += 1
    return float(acc / data_size)


def validation_accuracy(x, y, data_size):
    acc = 0
    for i in range(0, data_size):
        if abs(x[i] - y[i]) < 0.2:
            acc += 1

    print("Validation accuracy: ", float(acc / data_size))
    if float(acc / data_size) > .90:
        return True
    else:
        return False


def train_neural_network():
    prediction = neural_network_model(x_ph)
    cost = tf.losses.huber_loss(y_ph, prediction)
    # tf.summary.scalar("cost", cost)
    # reduce mean - average the batch
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(cost)
    hm_epochs = 200000

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        counter = 0
        for epoch in range(hm_epochs):
            epoch_loss = 0
            for i in range(1):
                counter += 1
                epoch_x, epoch_y = next_batch(i, batch_size)
                epoch_y = epoch_y.reshape(-1, 1)  # looks at size of epoch 1, how to convert it to 20,1
                _, c = sess.run([optimizer, cost], feed_dict={x_ph: epoch_x, y_ph: epoch_y})
                epoch_loss += c

            if epoch % 1000 == 0:
                print('Epoch', epoch, 'completed out of', hm_epochs, 'loss:', epoch_loss)

                if validation_accuracy(prediction.eval({x_ph: valid_x}), valid_y.reshape(-1, 1), len(valid_y)) is True:
                    break
                else:
                    pass

        print("Accuracy on Train:",
              accuracy(prediction.eval({x_ph: training_x}), training_y.reshape(-1, 1), len(training_y)))
        # print('Huber Loss on Test:', cost.eval({x_ph:testing_x, y_ph:testing_y.reshape(-1,1)}))
        acc = accuracy(prediction.eval({x_ph: testing_x}), testing_y.reshape(-1, 1), len(testing_y))
        print("Accuracy on Test:", float(acc))


train_neural_network()
