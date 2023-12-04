from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import pandas as pd
import requests
import json

YOUR_SHEET_ID='11FqGhLV_j1d4D-oWnF4-sXiSxpWg5ZfynOf2LijDmDQ'

r = requests.get(f'https://docs.google.com/spreadsheet/ccc?key={YOUR_SHEET_ID}&output=csv')
open('dataset.csv', 'wb').write(r.content)
df = pd.read_csv('dataset.csv')
# df = df.head()

# school_us_df = df[(df['country'] == '美國') & (df['category'] == '校園')]


# school_us_dicts = []
# for index, row in school_us_df.iterrows():
#     row_dict = row.to_dict()
#     school_us_dicts.append(row_dict)

# print(df)



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

print(get_dicts('love_kr'))

def flex_func(key):
    dicts = get_dicts(key)
    # if (key == 'school_us'):
    #     assign_df = df[(df['country'] == '美國') & (df['category'] == '校園')]
    # elif (key == 'med_us'):
    #     assign_df = df[(df['country'] == '美國') & (df['category'] == '醫療')]

    # dicts = []
    # for index, row in assign_df.iterrows():
    #     row_dict = row.to_dict()
    #     dicts.append(row_dict)    
        
    flex_content= {
                        "type": "carousel",
                        "contents": [
                            {
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
                                    "url": dicts[0]['photo']
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
                                            "text": dicts[0]['name'],
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
                                        "text": dicts[0]['country'],
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
                                    "data": "getplot0",
                                    "label": "劇情",
                                    "displayText": "我想了解劇情"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "label": "演員",
                                    "data": "getactor0",
                                    "displayText": "我想了解演員"
                                    }
                                }
                                ]
                            }
                            },
                            {
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
                                    "url": dicts[1]['photo']
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
                                            "text": dicts[1]['name'],
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
                                        "text": dicts[1]['country'],
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
                                    "data": "getplot1",
                                    "label": "劇情",
                                    "displayText": "我想了解劇情"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "label": "演員",
                                    "data": "getactor1",
                                    "displayText": "我想了解演員"
                                    }
                                }
                                ]
                            }
                            },
                            {
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
                                    "url": dicts[2]['photo']
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
                                            "text": dicts[2]['name'],
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
                                        "text": dicts[2]['country'],
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
                                    "data": "getplot2",
                                    "label": "劇情",
                                    "displayText": "我想了解劇情"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "label": "演員",
                                    "data": "getactor2",
                                    "displayText": "我想了解演員"
                                    }
                                }
                                ]
                            }
                            },
                            {
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
                                    "url":  dicts[3]['photo']
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
                                            "text": dicts[3]['name'],
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
                                        "text": dicts[3]['country'],
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
                                    "data": "getplot3",
                                    "label": "劇情",
                                    "displayText": "我想了解劇情"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "label": "演員",
                                    "data": "getactor3",
                                    "displayText": "我想了解演員"
                                    }
                                }
                                ]
                            }
                            },
                            {
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
                                    "url": dicts[4]['photo']
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
                                            "text": dicts[4]['name'],
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
                                        "text": dicts[4]['country'],
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
                                    "data": "getplot4",
                                    "label": "劇情",
                                    "displayText": "我想了解劇情"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "postback",
                                    "label": "演員",
                                    "data": "getactor4",
                                    "displayText": "我想了解演員"
                                    }
                                }
                                ]
                            }
                            }
                        ]
                        }
    return flex_content

# print(flex_func('med_us'))






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

# items_us=[
#                         QuickReplyButton(
#                             action=PostbackAction(label="醫療片", data="med_us",text="我想看醫療片")
#                         ),
#                         QuickReplyButton(
#                             action=PostbackAction(label="校園片", data="school_us",text="我想看校園片")
#                         ),
#                         QuickReplyButton(
#                             action=PostbackAction(label="愛情片", data="love_us",text="我想看愛情片")
#                         ),
#                         QuickReplyButton(
#                             action=PostbackAction(label="喜劇片", data="comedy_us",text="我想看喜劇片")
#                         ),
#                         QuickReplyButton(
#                             action=PostbackAction(label="法政片", data="law_us",text="我想看法政片")
#                         ),
                        
#                     ]






# def Carousel_Template():
#     message = TemplateSendMessage(
#             alt_text='test',
#             template=CarouselTemplate(
#                 columns=[
#                     CarouselColumn(
#                         thumbnail_image_url='https://img.freepik.com/free-photo/sky-clouds-cinematic-clouds-wallpaper-7_1562-744.jpg',
#                         title='Testing',
#                         text='website',
#                         actions=[
#                             URIAction(
#                                 label='GOOGLE',
#                                 uri='https://www.google.com'
#                             ),
#                             URIAction(
#                                 label='YOUTUBE',
#                                 uri='https://www.youtube.com'
#                             ),
#                             URIAction(
#                                 label='NETFLIX',
#                                 uri='https://www.netflix.com'
#                             ),                           
#                         ]
#                     ),
#                 ]
#             )
#         )
#     return message


def image_carousel_message():
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


# def buttons_message():
#     message = TemplateSendMessage(
#         alt_text='好消息來囉～',
#         template=ButtonsTemplate(
#             thumbnail_image_url="https://img.freepik.com/free-photo/sky-clouds-cinematic-clouds-wallpaper-7_1562-744.jpg",
#             title="test1",
#             text="test2",
#             actions=[
#                 DatetimePickerTemplateAction(
#                     label="請選擇生日",
#                     data="input_birthday",
#                     mode='date',
#                     initial='1990-01-01',
#                     max='2019-03-10',
#                     min='1930-01-01'
#                 ),
#                 MessageTemplateAction(
#                     label="HI",
#                     text="HELLO"
#                 ),
#                 URITemplateAction(
#                     label="網址",
#                     uri="https://www.google.com"
#                 )
#             ]
#         )
#     )
#     return message




print(flex_func('school_us'))

