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