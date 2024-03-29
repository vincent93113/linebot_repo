from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import pandas as pd
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from app import *
from crud import *





credentials = ServiceAccountCredentials.from_json_keyfile_name('sheet-api-412107-d39a802a3637.json', ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])

gc = gspread.authorize(credentials)

spreadsheet = gc.open('series_db')
spreadsheet2 = gc.open('collect_db')
worksheet1 = spreadsheet.sheet1
worksheet2 = spreadsheet2.sheet1
data1 = worksheet1.get_all_values()
data2 = worksheet2.get_all_values()
col_df = pd.DataFrame(columns = data2[0],data=data2[1:])
df = pd.DataFrame(columns = data1[0],data=data1[1:])





#4
def get_dicts(key):

    if  (key == 'school_us'):
        assign_df = df[(df['country'] == '美國') & (df['category'] == '校園')]
    elif (key == 'med_us'):
        assign_df = df[(df['country'] == '美國') & (df['category'] == '醫療')]
    elif (key == 'love_us'):
        assign_df = df[(df['country'] == '美國') & (df['category'] == '愛情')]
    elif (key == 'comedy_us'):
        assign_df = df[(df['country'] == '美國') & (df['category'] == '喜劇')]
    elif (key == 'law_us'):
        assign_df = df[(df['country'] == '美國') & (df['category'] == '法政')]
    elif (key == 'school_kr'):
        assign_df = df[(df['country'] == '韓國') & (df['category'] == '校園')]
    elif (key == 'med_kr'):
        assign_df = df[(df['country'] == '韓國') & (df['category'] == '醫療')]
    elif (key == 'love_kr'):
        assign_df = df[(df['country'] == '韓國') & (df['category'] == '愛情')]
    elif (key == 'comedy_kr'):
        assign_df = df[(df['country'] == '韓國') & (df['category'] == '喜劇')]
    elif (key == 'law_kr'):
        assign_df = df[(df['country'] == '韓國') & (df['category'] == '法政')]

    dicts = []
    for index, row in assign_df.iterrows():
        row_dict = row.to_dict()
        dicts.append(row_dict)
    return dicts    

#2
def item_func(country):

    items=QuickReply([
                            QuickReplyButton(
                                action=PostbackAction(label="醫療片", data=f"med_{country}",text="我想看醫療片")
                            ),
                            QuickReplyButton(
                                action=PostbackAction(label="校園片", data=f"school_{country}",text="我想看校園片")
                            ),
                            QuickReplyButton(
                                action=PostbackAction(label="愛情片", data=f"love_{country}",text="我想看愛情片")
                            ),
                            QuickReplyButton(
                                action=PostbackAction(label="喜劇片", data=f"comedy_{country}",text="我想看喜劇片")
                            ),
                            QuickReplyButton(
                                action=PostbackAction(label="法政片", data=f"law_{country}",text="我想看法政片")
                            ),
                            
                        ])
    
    return items

#5
def flex_func(key):
    dicts = get_dicts(key)
    content_list = [] #為了routine做flexmessage
    i = 0
    for each in dicts:
        each_card = {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "image",
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "2:3",
                                    "gravity": "top",
                                    "url": dicts[i]['photo']
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": dicts[i]['name'],
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0
                                        }
                                        ],
                                        "spacing": "lg"
                                    }
                                    ],
                                    "position": "absolute",
                                    "offsetBottom": "0px",
                                    "offsetStart": "0px",
                                    "offsetEnd": "0px",
                                    "paddingAll": "20px",
                                    "paddingTop": "18px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": dicts[i]['country'],
                                        "color": "#ffffff",
                                        "align": "center",
                                        "size": "xs",
                                        "offsetTop": "3px"
                                    }
                                    ],
                                    "position": "absolute",
                                    "cornerRadius": "20px",
                                    "offsetTop": "18px",
                                    "backgroundColor": "#ff334b",
                                    "offsetStart": "18px",
                                    "height": "25px",
                                    "width": "53px"
                                }
                                ],
                                "paddingAll": "0px"
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "data": "getplot"+str(i),
                                    "label": "劇情",
                                    "displayText": "我想了解劇情"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "label": "演員",
                                    "data": "getactor"+str(i),
                                    "displayText": "我想了解演員"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "label": "收藏",
                                    "data": "collect"+str(i),
                                    "displayText": "我要收藏此劇"
                                    }
                                }
                                ]
                            }
                            }
        content_list.append(each_card)
        i = i+1




    flex_content= {
                        "type": "carousel",
                        "contents": content_list
    }

    return flex_content


    message = TemplateSendMessage(
        alt_text='泡麵推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://cdn.cybassets.com/media/W1siZiIsIjE1NjgwL3Byb2R1Y3RzLzMxOTc4NDk1LzE2MDM3Njg1MDlfN2MzMDcxMDRjYTAzMjY4YzdlZjAuanBlZyJdLFsicCIsInRodW1iIiwiNjAweDYwMCJdXQ.jpeg?sha=b237442379719d23',
                    action=URITemplateAction(
                        label="辛拉麵",
                        uri='https://www.mrsuspenders.com.tw/products/%E8%BE%B2%E5%BF%83%E8%BE%9B%E6%8B%89%E9%BA%B5%E6%9D%AF'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://media.etmall.com.tw/nximg/002338/2338962/2338962-1_xxl.jpg?t=18393086831',
                    action=URITemplateAction(
                        label='滿漢大餐',
                        uri='https://www.etmall.com.tw/i/2338962'
                    )
                ),
            ]
        )
    )
    return message


