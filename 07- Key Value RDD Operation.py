#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('key-value_rdd_op_joins')
sc = SparkContext(conf = conf)


# # Operations
# - `groupByKey`: 이미 그룹이 지어진 상태에서 진행
#     - 그룹핑 후에 특성 Transformations같은 연산
#     - key값이 있는 상태에서 시작
# 
# - `groupBy()` :그룹을 생성하기 위함
#     - `RDD.grouBy(numPartitions=None, partitionFunc=<function portable_hash>)`
#     - 함수에 의해서 그룹이 생기는 연산

# In[4]:


rdd = sc.parallelize([
    ('짜장면',15),
    ('짬뽕',10),
    ('짜장면',5)
])


# In[5]:


# 항상 제일 앞에 있는 것이 Key임.
g_rdd = rdd.groupByKey()
g_rdd.collect()


# In[6]:


for i,j in g_rdd.collect():
    print(i,len(list(j)))


# In[7]:


g_rdd.mapValues(len).collect()


# In[8]:


g_rdd.mapValues(list).collect()


# In[9]:


# groupBy 사용하기
rdd = sc.parallelize([
    
    'c','c++','c#','Python','Java','JavaScript'
])


# In[10]:


rdd


# In[11]:


# groupBy는 그룹핑 할 키에 대한 정의를 개발자가 직접 해준다.
grouped = rdd.groupBy(lambda x : x[0])
grouped.glom().collect()


# In[12]:


grouped.mapValues(list).collect()


# In[13]:


grouped.getNumPartitions()


# In[14]:


g_rdd.getNumPartitions()


# In[15]:


# groupByKey는 K-V RDD를 사용할 때 Key가 알아서 그룹핑의 기준이 된다.

x = sc.parallelize([
    ("MATH", 7), ("MATH", 2), ("ENGLISH", 7),
    ("SCIENCE", 7), ("ENGLISH", 4), ("ENGLISH", 9),
    ("MATH", 8), ("MATH", 3), ("ENGLISH", 4),
    ("SCIENCE", 6), ("SCIENCE", 9), ("SCIENCE", 5)
], 3)

y = x.groupByKey()


# In[16]:


y.collect()


# In[17]:


y.glom().collect()


# #Join

# In[18]:


# Inner Joins : 서로 간에 존재하는 키만 합쳐줍니다. (only 교집합)
rdd1 = sc.parallelize([
    ('foo',1),
    ('goo',2),
    ('hoo',3)
])

rdd2 = sc.parallelize([
    ('foo',1),
    ('goo',2),
    ('goo',10),
    ('moo',6)
])

rdd1.join(rdd2).collect()


# **Outer Join**
# - 기준이 되는 한쪽에 데이터가 있고, 다른쪽에는 데이터가 없는 경우
#     - 설정한 기준에 따라서 기준에 맞는 데이터가 항상 남아있는다.
# - `leftOuterJoin`: 왼쪽에 있는 rdd가 기준이 됩니다.(함수를 호출하는 쪽)
# - `rightOuterJoin`: 오른쪽에 있는 rdd가 기준이 됩니다.(함수에 매개변수로 들어가는 쪽)

# In[19]:


rdd1.leftOuterJoin(rdd2).collect()


# In[20]:


rdd1.rightOuterJoin(rdd2).collect()


# In[21]:


sc.stop()


# 데이터 관리는 RDD 가 아닌 SQL 같은것으로 하는 것이 최고
