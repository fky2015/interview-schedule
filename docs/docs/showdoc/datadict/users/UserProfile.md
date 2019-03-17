# UserProfile
    
-  用户表，储存用户信息 继承原有的`AbstractUser`
- username, first_name, last_name, email, is_staff, is_active, data_joined 属于`AbstractUser`，在此略去，详见源码或者数据库。

| 字段          | 类型      | 空   | 默认        | 注释                                         |
| :------------ | :-------- | :--- | ----------- | -------------------------------------------- |
| intro         | text      | 是   |             | 自我介绍                                     |
| real_name     | char(50)  | 否   |             | 真实姓名                                     |
| gender        | char(8)   | 否   | secret      | 性别，实际上是一个choice(male,female,secret) |
| wechat_openID | char(100) | 否   | 0           | 注册时间                                     |
| mobile        | char(11)  | 是   |             | 手机号                                       |
| avatar        | char(100) | 是   | default.png | 存储头像路径                                 |

- 备注：为了保证CAS插件可用，可能还要修改扩展策略（乖乖使用User+Profile) // TODO: 待测试

目前用户表的创建规则是：
- 如果从小程序打开
  - 如果已有网页版账号
    - 输入网页版账户并登陆
    - 进行连接
  - 如果没有网页版账户
    - 新建并注册
- 如果从网页打开
  - 注册or登录

当然如果小程序的端为了体验的优化，也可以等到进行数据库操作之前再注册
