
    
## 简要描述 

- 所有club 

## 请求URL

`/api-admin/club/`

  
## 详见url

(https://dev.fkynjyq.com/api-admin/club/)[https://dev.fkynjyq.com/api-admin/club/]

## 权限

| 用户\方法  | create | retrieve | update | destroy | list | interview      | verification |
| ---------- | ------ | -------- | ------ | ------- | ---- | -------------- | ------------ |
| 普通用户   | n      | y        | n      | n       | y    | ro  只有可见的 | n            |
| 超级管理员 | y      | y        | y      | y       | y    | ro  只有可见的 | y            |  |

<!-- | 管理员     |        | y        | y      | n       | y    | ro  只有可见的 | n            | -->



## future

- [x] 计划增加审核状态，只有创建完之后审核通过的社团才能被看到。
- [x] `list`只能看到`pass`的
 

