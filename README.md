# Micro

Small example of microservices with:
1. PROXY - nginx proxy
2. API - Flask server
3. SOCKETS - nodejs socket.io service to send sockets
4. TASK - pure python service to make long term tasks
5. BROKER - RabbitMQ broker to communicate between API, TASK and SOCKETS services   

# Run the service
1. Clone the repository:
```shell
  git clone https://github.com/artyomtugaryov/micro.git 
```
2. Go to the folder with repository 
```shell
cd micro
```
3. Run doocker-compose:
```shell
dokcer-compose up --build
```