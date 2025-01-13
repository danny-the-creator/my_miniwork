import re
import random
import numpy as np
def between_markers(text, begin, end = "Hello!"):
    if begin not in text and end not in text:
        return text
        breakpoint()
    if begin not in text:
        return text[:text.index(end)]
        breakpoint()
    if end not in text:
        return text[text.index(begin) + len(begin):]
        breakpoint()
    return text[text.index(begin)+len(begin):text.index(end)]
def Kostili(list):                              # Заменяет все str(цифры) на float(цифры)
    kostili_1 = []                                      # Очень, ОЧЕНЬ, ОЧЕНЬ!!! большой костыль
    for i in list:
        kostili_2 = []
        for j in i:
            kostili_2.append(float(j))
        kostili_1.append(kostili_2)
    return kostili_1
# Глобальные параметры (Здесь они ничего не решают!)
Input_Dim = 4
Out_Dim = 3
H_Dim = 10

# Входные данные
x = [7.9, 3.1, 7.5, 1.8]
# Веса взятые из Iris_project (Достаточно один раз получить хорошие веса и их легко можно использовать везде)
                                                                            # Автоматически подставляются из файла, при изменении файла веса автоматически меняются
with open("Iris_weights") as file:
    W1 = between_markers(file.read(), 'W1 = ', '\n\nW2 = ' )
    W1 = [re.sub(']', '', re.sub('\[', '', i)) for i in W1.split(",\n")]
    W1 = [j.split(', ') for j in W1]
    W1 = np.array(Kostili(W1))
with open("Iris_weights") as file:
    W2 = between_markers(file.read(), 'W2 = ', '\n\nb1 = ' )
    W2 = [re.sub(']', '', re.sub('\[', '', i)) for i in W2.split(",\n")]
    W2 = [j.split(', ') for j in W2]
    W2 = np.array(Kostili(W2))
with open("Iris_weights") as file:
    b1 = between_markers(file.read(), 'b1 = ', '\n\nb2 = ' )
    b1 = [re.sub(']', '', re.sub('\[', '', i)) for i in b1.split(",\n")]
    b1 = [j.split(', ') for j in b1]
    b1 = np.array(Kostili(b1))
with open("Iris_weights") as file:
    b2 = between_markers(file.read(), 'b2 = ')
    b2 = [re.sub(']', '', re.sub('\[', '', i)) for i in b2.split(",\n")]
    b2 = [j.split(', ') for j in b2]
    b2 = np.array(Kostili(b2))

def relu(t):
    return np.maximum(t, 0)
def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)
def predict(x):
    t1 = x @ W1 + b1
    h1 = relu(t1)
    t2 = h1 @ W2 + b2
    z = softmax(t2)
    return z
probs = predict(x)
pred_class = np.argmax(probs)
class_name = ['Setosa', 'Versicolor', 'Virginica']
print("Class name: " + class_name[pred_class])

