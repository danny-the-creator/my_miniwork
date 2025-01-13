import Part_of_Iris_project as IrisProg
for i in range(100):
    with open("Iris_weights") as file:
        ex_accurasy = file.readline().split(' ')[1]
        ex_accurasy = float(ex_accurasy[:ex_accurasy.index("%")])
    IrisProg.iris_neural_network()
    print(str(IrisProg.accurasy * 100) + "%")
    if IrisProg.accurasy * 100 > ex_accurasy:
        print("New accurasy: " + str(IrisProg.accurasy * 100) + "%")
        print('Check "Iris_weights"!')
        quit()
print("Loop is over! Unfortunately, the accurasy hasn't increased...")
print("Maybe you should reapet the loop, or change something, or your accurasy is too high already...")
