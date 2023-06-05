#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("reduction-op")
sc = SparkContext(conf=conf)


# # Reduce
# - 사용자가 지정하는 함수를 받아(task) 여러 개의 값을 하나로 줄여준다.
# - 파티션 별로 작업이 일어난다!

# In[2]:


from operator import add # task


# In[3]:


add(1, 2)


# In[4]:


sample_rdd = sc.parallelize([1, 2, 3, 4, 5])
sample_rdd


# In[5]:


sample_rdd.reduce(add)


# In[6]:


# 파티션이 1개인 경우(입력하지 않으면 기본 1)
sample_rdd = sc.parallelize([1, 2, 3, 4], 1)
sample_rdd.reduce(lambda x, y : (x * 2) + y)

# 파티션이 1개
sample_rdd.glom().collect()


# In[7]:


# glom : 파티션 별 데이터를 보여주고 싶을 때 사용
sample_rdd_p2 = sc.parallelize([1, 2, 3, 4], 2)
sample_rdd_p2.glom().collect()


# In[8]:


sample_rdd_p2.reduce(lambda x, y : (x * 2) + y )


# In[9]:


sample_rdd_p3 = sc.parallelize([1, 2, 3, 4], 3)
sample_rdd_p3.reduce(lambda x, y : (x * 2) + y )


# In[10]:


sample_rdd_p3.glom().collect()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




