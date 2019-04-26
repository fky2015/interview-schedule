## 简要描述 

- 用户查看全部合法Interview

## 请求URL

`/api-admin/interview/`
  
## 详见url

[https://dev.fkynjyq.com/api-admin/interview/](https://dev.fkynjyq.com/api-admin/interview/)

## 权限设计

list、retrieve

只显示自己有权限修改的

create destroy update

只能创建、删除、修改有权限的社团的


### interviewTimeline

查看某个面试下的所有面试表

### export

导出数据

以timeline 为单位

- 姓名
- 学号
- 年级
- 联系方式
- 备注信息
- 是否通过
- 面试Timeline信息
- 面试Interiew信息
- 面试InterviewTimeline信息

### commit

使得状态转移
具体来说就是，通过的变更为`instate`，没有通过的不变