import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    channel = grpc.insecure_channel('10.211.1.32:50051')
    stub = hello_pb2_grpc.HelloServiceStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='Gleidson'))
    print("Resposta do servidor:", response.message)

if __name__ == '__main__':
    run()