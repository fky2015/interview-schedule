
    
## 简要描述

返回个人信息 

## 权限

查看，可新建,无法删除

## 请求URL

`/api/user/info/`

  
**详见url**

(https://dev.fkynjyq.com/api/user/info/)[https://dev.fkynjyq.com/api/user/info/]

## 如果需要修改

```json
{
    "url": "http://127.0.0.1:8000/api/user/info/1/",
    "username": "test",
    "realname": "",
    "email": "test@bit.edu.cn",
    "mobile": "",
    "groups": []
}
```

注意属性中有`url`一项，该`url`唯一标识用户身份。

通过对该url的提交修改后的json可以完成修改的目的

也就是不能在`info/`修改，而是在`info/n/`

## 如果没有该用户

会用json返回错误