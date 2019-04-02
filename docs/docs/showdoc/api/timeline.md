
    
**简要描述：** 

- 查看自己所有的timeline
- 并且可以取消报名

## 权限

只读，除非是超级管理员

**请求URL：** 

`/api/user/timeline/`

- apply
- cancel

分别报名和取消，详见api
  
**详见url**

(https://dev.fkynjyq.com/api/user/timeline/)[https://dev.fkynjyq.com/api/user/timeline/]

```json
[
    {
        "url": "http://localhost:8000/api/user/timeline/3/",
        "interviewTimeline": {
            "url": "http://localhost:8000/api/public/interviewTimeline/1/",
            "interview": {
                "url": "http://localhost:8000/api/public/interview/1/",
                "club": "http://localhost:8000/api/public/club/1/",
                "title": "春招面试"
            },
            "location": "2b301"
        },
        "user": "http://localhost:8000/api/user/info/1/",
        "startTime": "2019-01-01T01:00:00Z",
        "duration": 4,
        "timeID": 0
    }
]
```

