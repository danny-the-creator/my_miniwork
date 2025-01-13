import numpy as np
def sigmoid(x):                     # функция сигмоиды
    return 1 / (1 + np.exp(-x) )
# Обучающая выборка
training_inputs = np.array([[0, 0, 1],          # входные данные
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1],])
training_outputs = np.array([[0, 1, 1, 0]]).T   # что мы должны молучить

# Подбор рандомных весов
np.random.seed(1)
synaptic_weigts = 2 * np.random.random((3,1)) - 1         # [[12.00870061], [-0.2044116 ], [-5.8002822 ]] - можно сразу подставить веса
                                                                                                            # (поэтому неплохо, чтобы они сохранялись в каком-то файле)
# Метод обратного распространения ошибки
for i in range(100000):
    inputs_layer = training_inputs
    outputs = sigmoid(np.dot(inputs_layer, synaptic_weigts))

    err = training_outputs - outputs
    regulation = np.dot(inputs_layer.T, err * (outputs * (1 - outputs)))
    synaptic_weigts += regulation
print("Веса после обучения: {}".format(synaptic_weigts))
print("Rezult : {}".format(outputs))

# TEST
test_inputs = np.array([1, 1, 0])
output = sigmoid(np.dot(test_inputs, synaptic_weigts))
print(output)