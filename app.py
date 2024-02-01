from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


import tempfile, os
import datetime
import time
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

from crud import *
from filter import *
from dotenv import load_dotenv
load_dotenv()
credentials = ServiceAccountCredentials.from_json_keyfile_name('sheet-api-412107-d39a802a3637.json', ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])


line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

gc = gspread.authorize(credentials)

spreadsheet = gc.open('series_db')
spreadsheet2 = gc.open('collect_db')


worksheet1 = spreadsheet.sheet1
worksheet2 = spreadsheet2.sheet1

data1 = worksheet1.get_all_values()
data2 = worksheet2.get_all_values()


col_df = pd.DataFrame(columns = data2[0],data=data2[1:])
df = pd.DataFrame(columns = data1[0],data=data1[1:])

dicts = [] #放篩後的
# print(df)


app = Flask(__name__)

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent)
def handle_message(event):
    global col_df
    global df
    event_type = event.message.type


    if event_type == 'text':
        recieved_msg = event.message.text

        # if '我的最愛' in recieved_msg:

        #1
        if '韓劇' in recieved_msg:
            country = 'kr'
            message = TextSendMessage(text='那你想看哪種韓劇呢?',quick_reply=item_func(country))
            line_bot_api.reply_message(event.reply_token,message)
        elif '美劇' in recieved_msg:
            country = 'us'
            message = TextSendMessage(text='那你想看哪種美劇呢?',quick_reply=item_func(country))
            line_bot_api.reply_message(event.reply_token,message)
        elif '嗨' in recieved_msg:
            message = TextSendMessage(text='嗨 要我推薦你影集的話可以按下方按鈕或輸入 韓劇 or 美劇 ')

            line_bot_api.reply_message(event.reply_token,message)
        elif '我的最愛' in recieved_msg:
            userid = str(event.source.user_id)
            data2 = worksheet2.get_all_values()
            col_df = pd.DataFrame(columns = data2[0],data=data2[1:])
            if col_df['userid'].isin([userid]).any():
                print('111++++')
                temp =col_df[col_df['userid'] == userid]['collect_id'].iloc[0]
                collect_list = eval(temp)
                print(collect_list,111)
                print(type(collect_list),222)
                if collect_list == []:
                    message = TextSendMessage(text='收藏已清空')
                    line_bot_api.reply_message(event.reply_token,message)
                else:
                    message = FlexSendMessage(alt_text='我的最愛',contents=col_flex_func(userid,'false'))
                    line_bot_api.reply_message(event.reply_token, message)
            else:
                message = TextSendMessage(text='暫無收藏')
                line_bot_api.reply_message(event.reply_token,message)
    elif event_type == 'image':
        message = TextSendMessage(text='這是圖片')
        line_bot_api.reply_message(event.reply_token, message)



@handler.add(PostbackEvent)
def handle_message(event):
    # global collect_list
    global dicts
    
    recieved_msg = event.postback.data
    #3
    if 'med_kr' in recieved_msg:
        key = 'med_kr'
        
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)    
    elif 'school_kr' in recieved_msg:
        key = 'school_kr'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'love_kr' in recieved_msg:
        key = 'love_kr'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'law_kr' in recieved_msg:
        key = 'law_kr'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'comedy_kr' in recieved_msg:
        key = 'comedy_kr'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'med_us' in recieved_msg:
        key = 'med_us'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'school_us' in recieved_msg:
        key = 'school_us'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token,message)
        return
    elif 'love_us' in recieved_msg:
        key = 'love_us'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'comedy_us' in recieved_msg:
        key = 'comedy_us'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'law_us' in recieved_msg:
        key = 'law_us'
        dicts = get_dicts(key)
        message = FlexSendMessage(alt_text='影集推薦',contents=flex_func(key))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'getplot' in recieved_msg:
        if recieved_msg == 'getplot0':
            message = TextSendMessage(text=dicts[0]['name'] + '的劇情介紹為:' + '\n'+dicts[0]['introduce'])
            line_bot_api.reply_message(event.reply_token, message)
            # print(dicts)
        elif recieved_msg == 'getplot1':
            message = TextSendMessage(text=dicts[1]['name'] + '的劇情介紹為:' + '\n'+dicts[1]['introduce'])
            line_bot_api.reply_message(event.reply_token, message)
        elif recieved_msg == 'getplot2':
            message = TextSendMessage(text=dicts[2]['name'] + '的劇情介紹為:' + '\n'+dicts[2]['introduce'])
            line_bot_api.reply_message(event.reply_token, message)
        elif recieved_msg == 'getplot3':
            message = TextSendMessage(text=dicts[3]['name'] + '的劇情介紹為:' + '\n'+dicts[3]['introduce'])
            line_bot_api.reply_message(event.reply_token, message)
        elif recieved_msg == 'getplot4':
            message = TextSendMessage(text=dicts[4]['name'] + '的劇情介紹為:' + '\n'+dicts[4]['introduce'])
            line_bot_api.reply_message(event.reply_token, message)
    elif 'getactor' in recieved_msg:


        if recieved_msg == 'getactor0':
            message = TextSendMessage(text=dicts[0]['name'] + '的演員為:\n'+dicts[0]['actor'] +'和'+dicts[0]['actress'])
            line_bot_api.reply_message(event.reply_token, message)
        elif recieved_msg == 'getactor1':
            message = TextSendMessage(text=dicts[1]['name'] + '的演員為:\n' +dicts[1]['actor'] +'和'+dicts[1]['actress'])
            line_bot_api.reply_message(event.reply_token, message)
        elif recieved_msg == 'getactor2':
            message = TextSendMessage(text=dicts[2]['name'] + '的演員為:\n' +dicts[2]['actor'] +'和'+dicts[2]['actress'])
            line_bot_api.reply_message(event.reply_token, message)
        elif recieved_msg == 'getactor3':
            message = TextSendMessage(text=dicts[3]['name'] + '的演員為:\n' +dicts[3]['actor'] +'和'+dicts[3]['actress'])
            line_bot_api.reply_message(event.reply_token, message)
        elif recieved_msg == 'getactor4':
            message = TextSendMessage(text=dicts[4]['name'] + '的演員為:\n' +dicts[4]['actor'] +'和'+dicts[4]['actress'])
            line_bot_api.reply_message(event.reply_token, message)
    elif 'col_plot' in recieved_msg:
        userid = str(event.source.user_id)
        love_dicts = col_flex_func(userid,'get_lovedict')
        num = recieved_msg.split('col_plot')[1]
        num = int(num)
        message = TextSendMessage(text=love_dicts[num]['name'] + '的劇情介紹為:' + '\n'+love_dicts[num]['introduce'])
        line_bot_api.reply_message(event.reply_token, message)
    elif 'col_actor' in recieved_msg:
        userid = str(event.source.user_id)

        love_dicts = col_flex_func(userid,'get_lovedict') 
        num = recieved_msg.split('col_actor')[1]
        num = int(num)
        message = TextSendMessage(text=love_dicts[num]['name'] + '的演員為:\n' +love_dicts[num]['actor'] +'和'+love_dicts[num]['actress'])
        line_bot_api.reply_message(event.reply_token, message)
    elif 'del' in recieved_msg:
            userid = str(event.source.user_id)
            love_dicts = col_flex_func(userid,'get_lovedict')
            num = recieved_msg.split('del')[1]
            num = int(num)
            love_dicts.pop(num)
            # col_flex_func(userid,'update',love_dicts)。
            update_list = [item['id'] for item in love_dicts]
            print("-------------------")
            print(love_dicts)
            print(update_list)
            update_col_df(userid,update_list)
            message = TextSendMessage(text='已完成刪除')
            line_bot_api.reply_message(event.reply_token, message)
            
    #6
    elif 'collect' in recieved_msg:
        data2 = worksheet2.get_all_values()
        col_df = pd.DataFrame(columns=data2[0], data=data2[1:])
        userid = str(event.source.user_id)

        try:
            
            temp =col_df[col_df['userid'] == userid]['collect_id'].iloc[0]
            collect_list = eval(temp)
            print(collect_list,111)
            print(type(collect_list),222)

            # if (type(temp) == str ):
            #     temp = temp.replace('[','')
            #     temp = temp.replace(']','')
            #     collect_list = temp.split(',')
            # else:
            #     collect_list = temp
            
        except Exception as e:
            print('ee-:',e)
            collect_list = []
        print(collect_list)
        num = recieved_msg.split('collect')[1]
        num = int(num)

        if str(dicts[num]['id']) in collect_list:
            message = TextSendMessage(text=dicts[num]['name']+'已在你的最愛')

        else:
            collect_list.append(dicts[num]['id'])
            message = TextSendMessage(text='已將 '+dicts[num]['name']+' 加入你的最愛')
            update_col_df(userid,collect_list)
        
        line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
