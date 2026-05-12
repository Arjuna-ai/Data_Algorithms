import sys
import numpy as np

def main():
    n, m = map(int,sys.stdin.readline().strip().split())

    def encode(text):
        char_to_index ={
            'A':0,
            'B':1,
            'C':2,
            'D':3,
            'E':4,
            'F':5,
            'G':6
        }

        features = np.zeros(7)
        for char in text:
            if char in char_to_index:
                index = char_to_index[char]
                features[index] = 1.0

        return features
    
    train_data = []
    for _ in range(n):
        parts = sys.stdin.readline().strip().split()
        text = parts[0]
        label = int(parts[1])
        train_data.append((encode(text), label))

    test_data = []
    for _ in range(m):
        text = sys.stdin.readline().strip().split()
        test_data.append(encode(text))

    def solve(train_data,test_data):
        lr = 0.1
        epochs = 20

        weights = np.zeros(7)
        bias = 0.0

        def sigmoid(z):
            return 1.0 / (1.0 + np.exp(z))
        
        for _ in range(epochs):
            for features,label in train_data:
                z = np.dot(weights, features) + bias
                pred = sigmoid(z)
                error = pred - label

                weights = weights - lr * error * features
                bias = bias - lr * error
            
        result = []

        for features in test_data:
            z = np.dot(weights, features) + bias
            pred = sigmoid(z)

            if pred > 0.5:
                result.append(1)
            else:
                result.append(0)
            
        return result
    
    answers = solve(train_data, test_data)

    for ans in answers:
        print(ans)

if __name__ == '__main__':
    main()
