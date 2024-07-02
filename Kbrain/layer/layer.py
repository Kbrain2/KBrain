import numpy as np

class Dense:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights) + self.biases
        return self.output

    def backward(self, dvalues):
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        self.dinputs = np.dot(dvalues, self.weights.T)
        return self.dinputs

    def update(self, lr=0.001):
        self.weights -= lr * self.dweights
        self.biases -= lr * self.dbiases

class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)
        return self.output

    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0
        return self.dinputs

class Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        self.output = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return self.output

    def backward(self, dvalues):
        self.dinputs = dvalues
        return self.dinputs

# 입력 데이터 (예: 2개의 입력)
X = np.array([[1, 2, 3], [4, 5, 6]])

# 레이어 구성
dense1 = Dense(3, 2)  # 3개의 입력, 2개의 출력
activation1 = ReLU()

dense2 = Dense(2, 3)  # 2개의 입력, 3개의 출력
activation2 = Softmax()

# 순전파
output1 = dense1.forward(X)
output1 = activation1.forward(output1)

output2 = dense2.forward(output1)
output2 = activation2.forward(output2)

print("Final Output:")
print(output2)
