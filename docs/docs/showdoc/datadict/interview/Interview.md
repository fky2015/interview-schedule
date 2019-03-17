# Interview
    
-  某场面试，储存多个面试表信息
- uid略去

| 字段        | 类型        | 空   | 默认  | 注释                      |
| :---------- | :---------- | :--- | ----- | ------------------------- |
| club        | foreign key |      |       | club                      |
| title       | char(100)   | 否   |       | 比如“XXX社团第二次面试” |
| description | text        | yes  |       | some description          |
| is_public   | bool        | no   | flase | 是否向没有关系的用户开放  |
| out_state   | 外键        |      |       | 指向的状态                |
| edit_finish | bool        | 否   | false | 是否开放                  |


