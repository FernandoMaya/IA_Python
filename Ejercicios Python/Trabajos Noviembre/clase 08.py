import math

def sigmoide(x):
    return 1/1+ math.exp(-x)

print("sigmoide: ",sigmoide(-3.8))

def tanh(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
print("tan: ",tanh(2))

def step(x):
    if (math.exp(x)) <= 0:
        return 0
    elif (math.exp(x)) > 0:
        return 1
print("step: ",step(-40))

def relu(x):
    return max(0,x)
print("relu: ",relu(8))

def leaky_relu(x):
    return max(0.1*x,x)
print("leaky relu: ",leaky_relu(1))