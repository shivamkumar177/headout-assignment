
# 
# Headout-assignment





## Deployment

To run this project

First build the docker image  

Navigate to BASE directory of the project

RUN
```bash
    docker build -t file-server .

    docker run -p 8080:8080 --memory=1500m --cpus=2 --name=file-server file-server
```

Here we are running with all the mentioned limitation (RAM, CPU). 

If You want to generate files which are used as input then RUN

#### Make sure of Docker Container Name
``` bash
    docker exec -it file-server sh
```
This will open a executable terminal

RUN
```bash
    python gen_file.py
```

This command generates 30 files of size around 100MB
## API Info

#### Get all items

```http
  GET /data
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `n` | `int` | **Required**. Filename |
| `m` | `int` | **Optional**. Line Number |

#### Health

```http
  GET /health
```
returns 200 
