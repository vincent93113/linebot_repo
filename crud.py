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
from filter import *

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



def col_flex_func(userid,target):

    data1 = worksheet1.get_all_values()
    data2 = worksheet2.get_all_values()
    col_df = pd.DataFrame(columns = data2[0],data=data2[1:])
    df = pd.DataFrame(columns = data1[0],data=data1[1:])
    df['id'] = df['id'].astype(int)
    col_df['collect_id'] = col_df['collect_id'].apply(eval)

    certain_row = col_df[col_df['userid'] == userid]
    print(certain_row,99999888)

    certain_collect = certain_row['collect_id'].values[0]
    print(type(certain_collect))
    print(certain_collect,99999)
    certain_collect = [int(item) for item in certain_collect]
    filtered_rows = df[df['id'].isin(certain_collect)]





    print(filtered_rows,8989898988)

    # filtered_rows = df[df['id'].isin([certain_collect])]
    if (target == 'update'):
        love_dicts = dicts
        return love_dicts
    elif (target == 'get_lovedict'):
        love_dicts = []
        for index, row in filtered_rows.iterrows():
            row_dict = row.to_dict()
            love_dicts.append(row_dict)
        return love_dicts
    else:
        love_dicts = []
        for index, row in filtered_rows.iterrows():
            row_dict = row.to_dict()


            love_dicts.append(row_dict)
        content_list = []
        i = 0
        for each in love_dicts:
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
                                        "url": love_dicts[i]['photo']
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
                                                "text": love_dicts[i]['name'],
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
                                            "text": love_dicts[i]['country'],
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
                                        "data": "col_plot"+str(i),
                                        "label": "劇情",
                                        "displayText": "我想了解劇情"
                                        }
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "postback",
                                        "label": "演員",
                                        "data": "col_actor"+str(i),
                                        "displayText": "我想了解演員"
                                        }
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "postback",
                                        "label": "刪除",
                                        "data": "del"+str(i),
                                        "displayText": "我要刪除此劇"
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
    

#7
# def update_col_df(id, collect_list):

#     data2 = worksheet2.get_all_values()
#     col_df = pd.DataFrame(columns = data2[0],data=data2[1:])
#     # 檢查 userid 是否已經存在
#     if col_df['userid'].isin([id]).any():
#         # 更新現有 userid 的 collect_id
#         # col_df.loc[col_df['userid'] == id, 'collect_id'] = collect_list
#         user_row = col_df.loc[col_df['userid'] == id]
#         if not user_row.empty:
#             col_df.loc[col_df['userid'] == id, 'collect_id'] = col_df.loc[col_df['userid'] == id, 'collect_id'].apply(lambda x: x + collect_list)

#         else:
#             new_row = pd.DataFrame({'userid': [id], 'collect_id': [collect_list]})
#             col_df = pd.concat([col_df, new_row], ignore_index=True)
#         collect_list = [int(item) for item in collect_list if str(item).isdigit()]
#     else:
#         # 新的 userid，創建新行
#         collect_list = [int(item) for item in collect_list if str(item).isdigit()]
#         new_row = pd.DataFrame({'userid': [id], 'collect_id': [collect_list]})
#         col_df = pd.concat([col_df, new_row], ignore_index=True, axis=0)

#     # 更新到 Google Sheets
#     col_values = [col_df.columns.tolist()] + col_df.astype(str).values.tolist()
#     worksheet2.update(values=col_values, range_name='A1')

#     print(col_df)
# id = 'U30414045a6d60e9b3b051d4f18c3ddf1'
# collect_list = [16,11]
# update_col_df()

def update_col_df(id, collect_list):
    data2 = worksheet2.get_all_values()
    col_df = pd.DataFrame(columns=data2[0], data=data2[1:])


    col_df['collect_id'] = col_df['collect_id'].apply(eval)


    collect_list = [item for item in collect_list if str(item).isdigit()]


    if col_df['userid'].isin([id]).any():
        # 删除已存在的 userid 行        
        col_df = col_df[col_df['userid'] != id]


    new_row = pd.DataFrame({'userid': [id], 'collect_id': [collect_list]})
    col_df = pd.concat([col_df, new_row], ignore_index=True, axis=0)


    col_df['collect_id'] = col_df['collect_id'].apply(lambda x: [int(item) for item in x])


    col_values = [col_df.columns.tolist()] + col_df.astype(str).values.tolist()
    worksheet2.update(values=col_values, range_name='A1')

    print(col_df)







