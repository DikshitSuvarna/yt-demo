
# coding: utf-8

# #Documentation:
# 
# 1.The User will get all the videos info about the Youtube channel data which is publicly availiable.. whcih is grabbed through Youtube API
# 
# 2.The user needs first define the OS path(Which folder the data has to be saved)
# 
# 3.Next thing is User needs to get their Own Youtube API key(Instruction will be given below)(This is only for one time)
# 
# 4.User can enter channel ID of particular Youtube channel(for their like) and function will return all Videos information and channel information will be grabbed...
# 
# 5.This will be saved as (.csv) which user has defined in OS path..
# 
# 6.The function will also return some insights regarding the channel..

# In[1]:

#Importing the Libraries
import requests
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os


# In[2]:

'AIzaSyBPLaPWwTyUgnLLs8QjOkmcDLYx1MrxSDs'


# In[3]:

#Definig the Path where dataset needs to be saved



# In[4]:

#Function For API
def API_key(API):
    API_KEY=API
    return API_KEY
    


# In[5]:

API_KEY=API_key('Your API KEY')


# In[6]:

#Function one in which User input the Channel ID

def func(Channel_ID):
    contentDetails='snippet'
    pageToken=''
    videos=[]
    while 1:
        Url='https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&channelId='+Channel_ID+'&part='+contentDetails+'&id&order=date&maxResults=10000'+'&pageToken='+pageToken
        response=requests.get(Url).json()
        videos+=response['items']
        pageToken=response.get('nextPageToken')

        if pageToken is None:
            break
    return videos


# In[7]:

def videostats(Video_ID):
    try:
        secondurl='https://www.googleapis.com/youtube/v3/videos?key='+API_KEY+'&id='+Video_ID+'&part=statistics'+'&part=contentDetails'
        secondreq=requests.get(secondurl).json()
        for stats in secondreq['items']:
            try:
                Comment_count=stats['statistics']['commentCount']
            except KeyError:
                 Comment_count=stats['statistics'].get('commentCount',0)
            try:
                Like_count=stats['statistics']['likeCount']
            except KeyError:
                Like_count=stats['statistics'].get('likeCount',0)
            View_count=stats['statistics']['viewCount']
            duration=stats['contentDetails']['duration']
            definition=stats['contentDetails']['definition']
            caption=stats['contentDetails']['caption']
        return Comment_count,Like_count,View_count,duration,definition,caption
        
    except KeyError as e:
        print(e)


# In[8]:

def get_dataset(ID):
     try:
          data=[]
          res=func(ID)
          for video in res:
               if video['id']['kind']=='youtube#video':
                    Video_ID=video['id']['videoId']
                    Title=video['snippet']['title']
                    Published_Date=video['snippet']['publishedAt'].split('T')[0]
                    Comment_count,Like_count,View_count,duration,definition,caption=videostats(Video_ID)
                    data.append([Video_ID,Title,Published_Date,View_count,Like_count,Comment_count,duration,definition,caption])
          statistics=pd.DataFrame(data,columns=['Video_ID','Title','Published_Date','View_count','Like_count','Comment_count','Duration','Defintion','Caption'])
          return statistics
     except:
          print('Something Went wrong')


# In[9]:

def getchannelname(ID):
    res=func(ID)
    for video in res:
               if video['id']['kind']=='youtube#video':
                Channel_Title=video['snippet']['channelTitle']
                return Channel_Title

def subscribercount(ID):
    subsurl='https://www.googleapis.com/youtube/v3/channels?key='+API_KEY+'&id='+ID+'&part=statistics'
    subsresponse=requests.get(subsurl).json()
    subscount=subsresponse['items'][0]['statistics']['subscriberCount']
    return subscount


# In[10]:

#This function Will transform from data into further with meaningful data's
def meaningful(Test):
    urldata=[]
    Test[['View_count','Like_count','Comment_count']]=Test[['View_count','Like_count','Comment_count']].astype(int)
    Test['Published_Date']=Test['Published_Date'].astype('datetime64')
    #Test['Published_Date']=Test.Published_Date.astype('datetime64[ns]')
    Test['Month']=Test.Published_Date.dt.month
    Test['Year']=Test.Published_Date.dt.year
    Test['Weekday'] = Test['Published_Date'].dt.day_name()
    Test['LikeRatio']=round((Test['Like_count']/Test['View_count'])*100,2)
    Test['Videos_with_Mill'] = [1 if x > 1000000 else 0 for x in Test['View_count']]
    for url in  Test['Video_ID']:
        urldata.append('https://www.youtube.com/watch?v='+url)
    Test['url']=urldata
    return Test


# In[11]:

def path(dataset,channelname):
    newpath=os.path.expanduser( '~\Documents\\YTDataset')
    if not os.path.exists (newpath):
        os.makedirs (newpath)
        os.chdir (newpath)
        dataset.to_csv(channelname)
    else:
        os.chdir (newpath)
        dataset.to_csv (channelname)

def getinfo(ID):
    Dataset=get_dataset(ID)
    Channel_name=getchannelname(ID)
    Test=Dataset.copy()
    Final_dataset=meaningful(Test)
    path(Final_dataset,Channel_name+'channel.csv')
    return Final_dataset






