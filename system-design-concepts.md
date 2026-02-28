## System Desgin Concepts:

### Capabilities based Design
- **Worker declares** what it can do (capabilities) to the server.
- **Server assigns** tasks based on worker capabilities.

(This'how real distributed system works like Kubernetes works with Pods and Nodes)

### Task Assignment Model
- **Pull Model**: Workers request tasks when they are ready, and the server assigns tasks based on worker capabilities and availability.

- **Push Model**: Server pushes tasks to workers randomly, which can lead to inefficiencies if workers are not ready or capable of handling the tasks.

#### Real-world Examples where Pull Model is used: 
- Most large systems use pull model:
- Celery workers pull from queue
- Kafka consumers pull messages
- SQS workers poll for messages
- Kubernetes pods request tasks



