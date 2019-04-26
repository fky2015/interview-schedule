# Timeline

-  时间表，储存某一个具体时间间隔的信息
- uid略去

| 字段               | 类型                   | 空   | 默认  | 注释             |
| :----------------- | :--------------------- | :--- | ----- | ---------------- |
| interviewTimelines | InterviewTimelines外键 | 否   |       |                  |
| user               | UserProfile外键        | 否   |       |                  |
| timeID             | Int(4)                 | true | 0     | 同一时间的多个人 |
| startTime          | DateTime               | 否   |       | 开始时间         |
| duration           | Int(5)                 | 是   |       | 时长/分钟        |
| passed             | bool                   | no   | false | 是否通过         |

- 备注：这里还可以存评价，不过这是之后的事情了，需要添加field。