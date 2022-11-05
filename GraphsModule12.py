
# coding: utf-8

# In[1]:

import plotly.express as px
import pandas as pd
import numpy as np


#This will return Bar graph of total number of Years
def Videos_Uploaded_in_Year(Data):
    Videos_uploaded=Data.groupby('Year').count().reset_index().sort_values(by='Video_ID',ascending=False)
    fig=px.bar(data_frame=Videos_uploaded,x='Year',y='Video_ID',title='No of Vidoes Uploaded in Given Years')
    return fig


# In[4]:

#This will return Total no of views in Years
def Views_in_Year(Data):
    dataset=Data.groupby('Year').sum().reset_index()
    figure=px.line(data_frame=dataset,x='Year',y='View_count',title='Total no of View Per Year')
    return figure


# In[9]:

#This will return Total number of views with respect to number of videos uploaded
def Average_views(Data):
    Videos_uploaded=Data.groupby('Year').count().reset_index().sort_values(by='Video_ID',ascending=False)
    Video_count=Videos_uploaded.sort_values(by='Year',ascending=True)
    SuccessYear=Data.groupby('Year').sum().reset_index()
    SuccessYear['Count']=Video_count['Video_ID']
    SuccessYear['Views']=np.round(SuccessYear['View_count']/SuccessYear['Count'],2)
    return px.line(data_frame=SuccessYear,x='Year',y='Views',title='Average Views Per videos in Given Year')


# # Month

# In[14]:

#This will return Total Number of vidoes Uploaded in Months
def formonths(Data):
    test=Data.copy()
    test['Month']=test['Month'].map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})
    videMonth=test.groupby('Month').count().reset_index().sort_values(by='Title',ascending=False)
    return px.bar(data_frame=videMonth,x='Month',y='Title',title='Videos Published in given Month')


# In[13]:

#This wiil return Views
def formonthsViews(Data):
    test=Data.copy()
    test['Month']=test['Month'].map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})
    videview=Data.groupby('Month').sum().reset_index().sort_values(by='Month',ascending=False)
    return px.line(data_frame=videview,x='Month',y='View_count',title='No of views in a given Month')


# # Weeks

# In[15]:

#This will return Total Number of Uploads in Weeks
def Videos_Uploaded_in_Week(Data):
    Videos_in_weeks=Data['Weekday'].value_counts()
    Videos_in_weeks
    return px.bar(Videos_in_weeks,title='No of Videos Published in Weeks')


# In[16]:

#Percentage of Million views in Weeks
def Million_per_weeks(Data):
    Video_cou=Data.groupby('Weekday')['Video_ID'].count().reset_index().sort_values(by='Weekday',ascending=False)
    Week_Mill=Data.groupby('Weekday')['Videos_with_Mill'].sum().reset_index().sort_values(by='Weekday',ascending=False)
    Week_Mill=Week_Mill['Videos_with_Mill']
    Video_cou['Mill']=Week_Mill
    Video_cou['Perc']=(Video_cou['Mill']/Video_cou['Video_ID'])*100
    Video_cou
    fig=px.pie(data_frame=Video_cou,names='Weekday',values='Mill',hole=.3,
                hover_data=['Mill'], labels={'Mill':'Videos_with_Million'},title='No of Million Views videos in Given week')
    fig.update_traces(textinfo='percent+label')
    return fig


# # Duration

# In[18]:




# In[21]:

def showDurationsum(Data):
    testdur=Data.copy()
    d1=testdur['Duration'].str.replace('PT','')
    data1=[]
    for i in d1:
        data1.append(i.split('M')[0])
    testdur['testDur']=data1
    testdur['testDur']=pd.to_numeric(testdur['testDur'],errors='coerce')
    testdur['testDur']= testdur['testDur'].fillna(-1)
    bins=[-1,0,10,20,45,60]
    labels=['N/A','Short','Medium','Long','Ultimate']
    testdur['testDur']=pd.cut(testdur.testDur,bins,labels=labels,include_lowest=True)
    DurationSum=testdur
    tescou=DurationSum.groupby('testDur').count().reset_index()
    return px.bar(data_frame=tescou,x='testDur',y='Video_ID')



# In[28]:

def showDurationViews(Data):
    testdur=Data.copy()
    d1=testdur['Duration'].str.replace('PT','')
    data1=[]
    for i in d1:
        data1.append(i.split('M')[0])
    testdur['testDur']=data1
    testdur['testDur']=pd.to_numeric(testdur['testDur'],errors='coerce')
    testdur['testDur']= testdur['testDur'].fillna(-1)
    bins=[-1,0,10,20,45,60]
    labels=['N/A','Short','Medium','Long','Ultimate']
    testdur['testDur']=pd.cut(testdur.testDur,bins,labels=labels,include_lowest=True)
    DurationSum=testdur
    tessum=DurationSum.groupby('testDur').sum().reset_index()
    return px.line(data_frame=tessum,x='testDur',y='View_count')



# In[ ]:




# In[ ]:



