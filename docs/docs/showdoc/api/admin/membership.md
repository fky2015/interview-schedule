
    
**简要描述：** 

<!-- - 查看自己所有的membership -->

## 权限

超级管理员
貌似就不应该对外开放的

**请求URL：** 

`/api/user/info/`

  
**详见url**

(https://dev.fkynjyq.com/api/user/membership/)[https://dev.fkynjyq.com/api/user/membership/]

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/api/user/membership/1/",
            "club": {
                "url": "http://127.0.0.1:8000/api/admin/club/1/",
                "name": "TEST社团",
                "intro": "testtest",
                "avatar": null
            },
            "name": "defulat1",
            "can_edit": false,
            "can_schedule": false,
            "can_export": false,
            "date_created": "2019-03-15"
        },
    ]
}
```

