# api 接口文档

api具体操作全部由django-rest-famework提供

请访问

[api](https://dev.fkynjyq.com/api)

查看具体细节


- 专门针对普通用户的
- 专门针对管理用户的 


## 小程序

小程序使用post请求将用户的code发送给该视图,obtai_auth_token会生成并返回一个token

```python
{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }
```

将token存储在本地,之后的请求只需要在请求头中携带Authorization即可

```python
Authorization: WToken 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```


