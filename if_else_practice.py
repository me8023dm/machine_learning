#!/usr/bin/env python
# coding: utf-8


age = [18,20,30]
activities = [5,3,6]
for i,j in age,activities : 
    if i >= 20  and j > 5 :
        print('可访问CDP')
    else :
        print('不可访问')


# In[3]:


# 示例：遍历Hive数据
user_actions = ["click", "view", "purchase"]  # 模拟Hive查询结果
for idx, action in enumerate(user_actions):
    print(f"用户第{idx+1}次行为是：{action}")


# In[5]:


# 示例：遍历Hive数据
user_actions = ["click", "view", "purchase"]  # 模拟Hive查询结果
for i in range(len(user_actions)):
    print(f"用户第{i+1}次行为是：{user_actions[i]}")


# In[2]:


# 从Hive读取最近7天用户登录次数，用for循环计算日均活跃度
users = ['A', 'B' , 'C']
num = 0
for i in users[:]: 
    num += 1
avg_num = round(num/7,2)
print(f'活跃人数：{num},{avg_num}')
    


# In[8]:


# 用while循环实现猜数字游戏（随机数范围1-100，最多尝试5次）
import random
x = 0
y = random.randint(1, 100)
while x < 5 :
    if y == 10 : 
        print('you win ')
    else :
        print(f'y值为：{y}')
        print('you lose')
    y = random.randint(1, 100)
    x += 1


# In[20]:


# 使用for循环统计高价值用户（单笔消费≥500且总次数≥3）
consumption_amount = [100,300,500,600]
consumption_times = [5,3,6,4]
x = 0
for i in range(len(consumption_amount)):
    if consumption_amount[i] >= 500 and consumption_times[i] >= 3 :
        x += 1
print(f'{x}')


# In[23]:


# 用if嵌套判断用户等级（普通/白银/黄金）
consumption_amount = [100,300,500,600]
for i in range(len(consumption_amount)):
    if consumption_amount[i] <= 100 :
        print('普通会员')
    elif consumption_amount[i] > 100 and consumption_amount[i] <= 300:
        print('白银会员')
    else :
        print('黄金会员')
        






