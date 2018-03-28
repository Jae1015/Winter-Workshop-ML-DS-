#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
#why encodings?

import requests

import facebook
 
token="EAACEdEose0cBAPmetJso6fRJzrXT2KFDCEZAQcIlfhIWpn9BD9vBw2cGputuGZBdVpDGnLM1eNXcgVmAXZAoY06Q7IAZBcLP1ATD5fUAOGb9u6Wv3wqjVCPUuH1jhfNoZAZAC7IrxhWhxhos4l3ZCvOF0XpFP6v3g7ag4tVR7B9Tvs19Sgs2qEAtv6lO6aT5rEZD"
graph = facebook.GraphAPI(access_token=token, version = 2.7)

#find information on events for any search term
# and limiting those events’ number to 10000:
friends = graph.request("/me?fields=friends&type=user")

print(friends)
#only those friends are listed who use facebook developer API.And total_Scount shows the number of friends
#all the friends can be accessed using taggable friends

#For this EventID, get all information and set few variables which will be used later by:
#event1 = graph.get_object(id=eventid,
fields="me?fields=about,birthday,address,education,email,favorite_teams,first_name,gender,hometown,favorite_athletes,inspirational_people,devices,age_range,can_review_measurement_request,context,install_type,interested_in,is_shared_login,languages,cover,id,link,last_name,location,installed,is_verified,middle_name,name_format,name,political,meeting_for,public_key,quotes,relationship_status,religion,security_settings,shared_login_upgrade_required_by,short_name,significant_other,sports,locale,test_group,timezone,updated_time,verified,achievements,albums,accounts,apprequestformerrecipients,asset3ds,apprequests,books,video_broadcasts,brand_teams,viewer_can_send_gift,commission_splits,curated_collections,domains,rich_media_documents,family,favorite_requests,friendlists,taggable_friends,groups,games,request_history,session_keys,likes,locations,live_videos,currency,leadgen_forms,live_encoders,video_upload_limits,website,work,updates,movies,ratings,tagged,tagged_places,videos,feed.since(2015).show_expired(true).include_hidden(true).limit(10).until(2017){actions,admin_creator,call_to_action,is_live_audio,is_app_share,backdated_time,caption,child_attachments,comments_mirroring_domain,comments,coordinates,created_time,is_crossposting_eligible,description,instagram_eligibility,feed_targeting,from,full_picture,is_hidden,icon,is_expired,is_popular,instream_eligibility,is_spherical,parent_id,link,likes,message,message_tags,name,permalink_url,place,privacy,picture,reactions,story,source,story_tags,status_type,timeline_visibility,type,updated_time,with_tags,to,width,expanded_width}"


