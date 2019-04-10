
    
## 简要描述  

- 所有club 

## 请求URL 

`/api/club/`

  
## 详见url 

(https://dev.fkynjyq.com/api/club/)[https://dev.fkynjyq.com/api/club/]

## 权限

| 用户\方法  | create | retrieve | update | destroy | list | interview      | verification |
| ---------- | ------ | -------- | ------ | ------- | ---- | -------------- | ------------ |
| 管理员   | y      | y        | n      | n       | y    | ro  只有可见的 | n            |
| 超级管理员 | y      | y        | y      | y       | y    | ro  只有可见的 | y            |  |

<!-- | 管理员     |        | y        | y      | n       | y    | ro  只有可见的 | n            | -->

create

创建社团时，会默认创建社团管理员和普通用户两种角色，会默认建立自己与社团的管理员关系。

list

只列出自己管理的

retrieve

只列出自己管理的

update

有update权限才能执行

destroy

不允许非超级用户操作
