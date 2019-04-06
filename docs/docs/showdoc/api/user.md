
    
## 简要描述

返回个人信息 

## 权限

查看，可新建,无法删除

## 请求URL

`/api/user/`

  
**详见url**

(https://dev.fkynjyq.com/api/user/)[https://dev.fkynjyq.com/api/user/]


注意属性中有`url`一项，该`url`唯一标识用户身份。

通过对该url的提交修改后的json可以完成修改的目的

也就是不能在`user/`修改，而是在`user/n/`

## 额外方法

- `club` 查看自己所有的club
- `timeline` 查看自己所有的timeline

## 权限

| 用户\方法 | update| | club | timeline |
| --------- | --------- | ---- | -------- |
| 普通用户  |y | r    | r        ||\


### club

所有和自己有关系（membership）的，并且`verified`为`pass`的（通过验证的）

### timeline

所有自己的timeline，也会进一步显示所属interviewTimeline。
