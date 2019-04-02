
    
**简要描述：** 

- 所有club 

**请求URL：** 

`/api/user/info/`

  
**详见url**

(https://dev.fkynjyq.com/api/club/)[https://dev.fkynjyq.com/api/club/]

## 权限

| 用户\方法 | create | retrieve | update | destroy | list | interview      |
| --------- | ------ | -------- | ------ | ------- | ---- | -------------- |
| 普通用户  | y      | y        | n      | n       | y    | ro  只有可见的 |
| 管理员    |        | y        | y      | n       | y    | ro  只有可见的 |

create

创建社团时，会默认创建社团管理员和普通用户两种角色，会默认建立自己与社团的管理员关系。

update

没有在权限这一环节限制的原因是，调用一次接口会查询四次，好慢。
任意用户可以向任意uri post，但只有有权限用户才会修改成功

destroy


