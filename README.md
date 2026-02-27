# Distrubuted-Task-System

A **distributed task execution system** in which server is going to take task and assign the task to the worker and worker is going to execute the task and send the result back to the server. 
Which eventually send the result to the user/client. 

## Protocol Design for communication between server and worker
*Design Goals*

**Your distributed system needs to support:**
- Worker registration
- Task request
- Task assignment
- Result submission
- Error reporting
- Heartbeat (later)

### Base Message Structure
```json
{
  "version": "1.0",
  "type": "MESSAGE_TYPE",
  "request_id": "unique-id",
  "payload": { }
}
```

### Message Types
1. **Worker Registration**

    *Worker ---> Server*
```json
{
    "version": "1.0",
    "type": "WORKER_REGISTRATION",
    "payload": {
        "worker_id": "req-001",
        "capabilities": [
                        "add", 
                        "subtract", 
                        "multiply", 
                        "divide"
                    ]
    }
}
```

*Server → Worker*

```json
{
    "version": "1.0",
    "type": "REGISTER_ACKNOWLEDGEMENT",
    "request_id": "req-001",
    "payload": {
        "status": "success"
    }
}
```

2. **Task Assignment**

*Server → Worker*

```json
{
    "version": "1.0",
    "type": "TASK_ASSIGNMENT",
    "request_id": "task-101",
    "payload": {
        "task_id": "task-101",
        "operation": "add",
        "data": {
            "a": 5,
            "b": 10
        }
    }
}
```

3. **Task Result**

*Worker → Server*

```json
{
  "version": "1.0",
  "type": "TASK_RESULT",
  "request_id": "task-101",
  "payload": {
    "task_id": "task-101",
    "status": "success",
    "result": 15
  }
}
```

4. **Task Failure**

*Worker → Server*

```json
{
    "version": "1.0",
    "type": "TASK_RESULT",
    "request_id": "task-101",
    "payload": {
        "task_id": "task-101",
        "status": "failed",
        "error": "Division by zero"
    }
}
```

5. **Worker Requests Task**

instead of server pushing tasks randomly,
better design is:
Worker asks for work.


*Worker → Server*

```json
{
    "version": "1.0",
    "type": "REQUEST_TASK",
    "request_id": "req-555",
    "payload": {
        "worker_id": "worker-1"
    }
}
```
6. **Server → Worker (If No Task)**

*Server → Worker*

```json
{
  "version": "1.0",
  "type": "NO_TASK",
  "request_id": "req-555",
  "payload": {}
}
```


**System Design Pattern:** Capability-based design

Server knows what worker can do

Worker only executes **whitelisted operations**

`Server, Worker Communication `

- Server maintains a registry of workers and their capabilities.
- **Pull Model** for task assignment: Workers request tasks when they are ready, and the server assigns tasks based on worker capabilities and availability.

