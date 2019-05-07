## 小程序调用api对应表

| 功能                         | api                                      | 备注   |
| ---------------------------- | ---------------------------------------- | ------ |
| 用户注册                     | `/api/user/`                             | POST   |
| 获取社团新闻                 |                                          | on dev |
| 获取个人面试提醒             |                                          |        |
| 获取社团列表                 | `/api/club/`                             |        |
| 该页面下的子页面“面试场次” | `/api/club/[ID]/interview/`              |        |
| 获取该面试场次及详细信息     | `/api/interview/[ID]/interviewTimeline/` |        |
| 获取该场次中所有时间片       | `/api/interviewTimeline/1/timeline/`     |        |
| 获取用户个人信息             | `/api/user/`                             |        |
| 退出某场面试                 | `/api/timeline/[ID]/apply/`              |        |  |

### 微信小程序登录方式

首次注册，或者通过小程序关联已有账户，需要提交`POST请求`
```json
{
    "code":"xxxxxx", // 用于供后端获取openID
    "username":"学号",
    "password":"xxxx", // 首次注册：提供密码；关联已有账户：提供相应用户名的密码
}
```
到接口`/api_token_auth/`

然后你会收到一个
```json
{
    "token":"xxxx"
}
```

在后续请求中，每次提交该`token`来维持session。

```python
Authorization: WToken 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```


如果已经拥有相应的账户，只需在`POST请求`时提交
```json
{
    "code":"xxxx"
}
```

即可，不需要用户名和密码。