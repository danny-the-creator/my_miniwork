import matplotlib.pyplot as plt
import random
import re
import numpy as np
from sklearn import datasets
accurasy = 'accurasy'
def iris_neural_network():
    iris = datasets.load_iris()
    dataset = [(iris.data[i][None, ...], iris.target[i]) for i in range(len(iris.target))]          # Объединение данных и правильного ответа в один dataset
    # Глобальные параметры                                                                                                            # (ниже есть работающий мой собственный прииер [30 строка])
    Input_Dim = 4
    Out_Dim = 3
    H_Dim = 10

    def relu(t):
        return np.maximum(t, 0)
    def softmax(t):
        out = np.exp(t)
        return out / np.sum(out)
    def sparse_cross_entropy(z, y):
        return -np.log(z[0,y])

    def to_full(y, num_classes):
        y_full = np.zeros((1, num_classes))
        y_full[0, y] = 1
        return y_full
    def relu_deriv(t):
        return (t >= 0).astype(float)

# dataset = [(training_inputs[i][None, ...], int(training_outputs[i])) for i in range(len(training_inputs))]            # пример

    W1 = np.random.rand(Input_Dim, H_Dim)
    b1 = np.random.rand(1, H_Dim)
    W2 = np.random.rand(H_Dim, Out_Dim)
    b2 = np.random.rand(1, Out_Dim)

    W1 = (W1 - 0.5) * 2 * np.sqrt(1/Input_Dim)
    b1 = (b1 - 0.5) * 2 * np.sqrt(1/Input_Dim)
    W2 = (W2 - 0.5) * 2 * np.sqrt(1/H_Dim)
    b2 = (b2 - 0.5) * 2 * np.sqrt(1/H_Dim)

    loss_arr = []
    SPEED = 0.00015
    Num_Epochs = 1000

    for Epoch in range(Num_Epochs):
        random.shuffle(dataset)
        for i in range(len(dataset)):
            x, y = dataset[i]
            # Forward
            t1 = x @ W1 + b1
            h1 = relu(t1)
            t2 = h1 @ W2 + b2
            z = softmax(t2)
            E = sparse_cross_entropy(z, y)

            # BackPropagation
            y_full = to_full(y, Out_Dim)
            de_dt2  = z - y_full
            de_dW2 = h1.T @ de_dt2
            de_db2 = de_dt2
            de_dh1 = de_dt2 @ W2.T
            de_dt1 = de_dh1 * relu_deriv(t1)
            de_dW1 = x.T @ de_dt1
            de_db1 = de_dt1

            # Update
            W1 = W1 - SPEED * de_dW1
            b1 = b1 - SPEED * de_db1
            W2 = W2 - SPEED * de_dW2
            b2 = b2 - SPEED * de_db2

            loss_arr.append(E)

    def predict(x):
        t1 = x @ W1 + b1
        h1 = relu(t1)
        t2 = h1 @ W2 + b2
        z = softmax(t2)
        return z
    def calculate_accurasy():
        correct = 0
        for x, y in dataset:
            z = predict(x)
            y_pred = np.argmax(z)
            if y_pred == y:
                correct += 1
        acc = correct / len(dataset)
        return acc
    global accurasy
    accurasy = calculate_accurasy()
    file = open("Iris_weights")
    ex_accurasy = file.readline().split(' ')[1]
    ex_accurasy = float(ex_accurasy[:ex_accurasy.index("%")])
    if accurasy * 100 > ex_accurasy:
        W1 = ",\n".join([str(W1[i]).replace('\n', '') for i in range(len(W1))])
        W2 = ",\n".join([str(W2[i]).replace('\n', '') for i in range(len(W2))])
        W1, W2 = re.sub("\[ ", "[", W1), re.sub("\[ ", "[", W2)
        W1, W2 = re.sub(' {1,}]', ']', W1), re.sub(' {1,}]', ']', W2)
        W1, W2 = re.sub(' {1,}', ', ', W1), re.sub(' {1,}', ', ', W2)

        b1, b2 = str(b1).replace('\n', ''), str(b2).replace('\n', '')
        b1, b2 = re.sub("\[ ", "[", b1), re.sub("\[ ", "[", b2)
        b1, b2 = re.sub(' {1,}]', ']', b1), re.sub(' {1,}]', ']', b2)
        b1, b2 = re.sub(' {1,}', ', ', b1), re.sub(' {1,}', ', ', b2)
        file.close()
        file = open("Iris_weights", "w")
        file.write("Accurasy: " + str(accurasy * 100 )+ "% \n\n")
        file.write("W1 = " + '[{}]'.format(W1) + "\n\nW2 = " + '[{}]'.format(W2) + "\n\nb1 = " + b1 + "\n\nb2 = " + b2)
    file.close()
if __name__ == '__main__':
    iris_neural_network()
    print('Accurasy: ' + str(accurasy * 100) + "%" )
    plt.plot(loss_arr)
    plt.show()


