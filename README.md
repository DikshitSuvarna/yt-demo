# yt-demo
Documentation:


::APICallingTesting::
1.The First page is APICallingTesting
The layout is defined..
Dash have n_Clicks to trigger the button click

Function Search:
Check whether user have inputted something or not...
if not:
return "", "Please Enter Channel ID", dash.no_update, ""
Same page, value will remain same, dash will not update, no store value

if channel id is some other keywords
then Except:
return "", "Something Went Wrong", dash.no_update, ""

If channel ID is correct:


Youtube Module will trigger

::Youtube_Module::
Inside Youtube module getinfo will trigger(ticker is channel ID)
Inside getinfo, get_dataset will trigger 
Inside get_dataset, func will trigger:

The Func Function will check for Youtube API key and channel ID, if reponse is 200 then it will send data in JSON format
Per page is 50 videos and it will check for next page token will trigger till last page token (500 Videos is MAX limit for YOUTUBE API)

Once the func is exceuted it will store in res in get_dataset
The get_dataset will extract necessary data from the JSON value, and simultaneously triggering video stats where will get additional data and once all data is gathered,
the data will append and store in pandas dataframe in statistics
The statistics will store in Dataset varible in getinfo
Channel Name will trigger getchannelname
Final_dataset will trigger meaningful function
The meaningful function will transform the dataset by including all data types and adding additional data


The Final_dataset will return to dataframe variable in APICallingTesting 
The Channel name will return to name variable in APICallingTesting 
The Subscribercount will return to Subscount in APICallingTesting


Once everything is Done the value will changes to Success and all this three varible in dcc.store which is somewhat similar to session

This will return 
return '/pages/hometestpage', value, "Click on to See...Results", store

'/pages/hometestpage'        : Next page
value   		           : Success
"Click on to See...Results"  : Button text change to this
store				     : The Three variable



If any one thing is missing while getting data it goes to except block:
and return 
return "", "Something Went Wrong", dash.no_update, ""


""			           : Same page
value   		           : Something Went Wrong
dash.no_update		     : No Update in button text
store				     : Nothing saved


=====================================================================================================================================================================

Once clicked in Click on to See...Results it will go in next page HomeTestPage

The first page is Youtube Logo animation...here all the calculation takes place


HomeTestPage:


The First thing triggers the tabs
There are total three Tabs 
1.Home 
2.Trend
3.Datatable



def update(data):
     name=data.get('name')
     some=data.get("data")
     subcount=data.get("subscount")
     data1=pd.DataFrame(some)
     return True,tb.functionoflayout(data1,subcount,name)

.get('name') is store value coming from APICalling page for channel name,Similarly data and subscount

Since the data getting in dict format, that is converted into pandas dataframe

All this value is returned to functionoflayout in Tabs module



The First or Default tab

if tab_choosen == 'Home_Tab':
   return tb.Home_layout()


This will trigger function Home_layout inside Tabs module:
Inside Home_layout, tab1 will trigger
Inside tab1, generate_cards will trigger 
Inside generate_cards, generate_card_content will trigger

generate cards will return name of channel, Total views and subs count and no of videos



elif tab_choosen == 'Trend_Tab':
	time.sleep (10)
      return tb.Trend_layout()

This will trigger Trends Function inside Tabs Module
Inside Trends tab2 will trigger
Inside tab2 tesalyout function will trigger(This will trigger YoutubeAnalyticsTest Module) The value is the pandas dataframe

The teslayot will trigger another Module GraphsModule12

GraphsModule12:
The data will be Pandas Dataframe

This module will call all Graphs 

Once all the Graphs method is executed it will assigned to YoutubeAnalytics and all that things will be called by Analytics layout

Which will pass to tab2 in Tabs Module which will eventually passed to Trend Layout



elif tab_choosen == 'DataTable_Tab':
	time.sleep (10)
      return tb.Datatable_layout()

This will trigger Datatabale_layout inside Tabs Module
Inside Datatable_layout it will trigger tab3() Function

Inside tab3 Datatest module will trigger
The dataset module:
table(data) will have Pandas dataframe as parameter
This dataframe is Converted into dictionary and all styling and export button is created..
Once done dictionary is returned in the form of Datatable


========================================================================================================================================================================================



 

