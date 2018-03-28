#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
#why encodings?

import requests

import facebook
 
token="EAACEdEose0cBAPmetJso6fRJzrXT2KFDCEZAQcIlfhIWpn9BD9vBw2cGputuGZBdVpDGnLM1eNXcgVmAXZAoY06Q7IAZBcLP1ATD5fUAOGb9u6Wv3wqjVCPUuH1jhfNoZAZAC7IrxhWhxhos4l3ZCvOF0XpFP6v3g7ag4tVR7B9Tvs19Sgs2qEAtv6lO6aT5rEZD"
graph = facebook.GraphAPI(access_token=token, version = 2.7)

#find information on events for any search term say “Poetry”
# and limiting those events’ number to 10000:
events = graph.request("/search?q=Poetry&type=event&limit=10000")

#to get list of events
eventList = events["data"]
#use "" only

#Get the EventID of the first event in the list by
eventid = eventList[1]["id"]

#For this EventID, get all information and set few variables which will be used later by:
event1 = graph.get_object(id=eventid,
 fields="attending_count,can_guests_invite,category,cover,declined_count,description,end_time,guest_list_enabled,interested_count,is_canceled,is_page_owned,is_viewer_admin,maybe_count,noreply_count,owner,parent_group,place,ticket_uri,timezone,type,updated_time")
attenderscount = event1["attending_count"]
declinerscount = event1["declined_count"]
interestedcount = event1["interested_count"]
maybecount = event1["maybe_count"]
noreplycount = event1["noreply_count"]

#Getting the list of all those who are attending an event and converting the response into json format:

attenders = requests.get(“https://graph.facebook.com/v2.11/"+eventid+"/attending?access_token="+token+”&limit=”+str(attenderscount)) 

attenders_json = attenders.json()

