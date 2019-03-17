# UserProfileClub

- 由UserProfile与Club的many to many 关系而来
- 这里存储用户与社团的关系，具体关系在membership中定义
- uid 略去

| 字段        | 类型 | 空   | 默认 | 注释 |     |
| :---------- | :--- | :--- | ---- | ---- | --- |
| userProfile | 外键 | 否   |      | 用户 |     |
| club        | 外键 | 否   |      | 社团 |     |
| membership  | 外键 | 是   |      | 关系 |     |


约束： userProfile, club

