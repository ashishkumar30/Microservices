import math


def square_root(x):
    output = math.sqrt(x)
    return output

# python3 -m grpc_tools.protoc -I.python_out=. --grpc_python_out=. Calculator.proto
