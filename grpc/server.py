import grpc
from concurrent import futures
import time

import hello_pb2
import hello_pb2_grpc

class HelloService(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        print(f"Recebido nome: {request.name}")
        return hello_pb2.HelloReply(message=f"Olá, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando em porta 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()