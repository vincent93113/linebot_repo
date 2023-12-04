from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from flask_ngrok import run_with_ngrok

import tempfile, os
import datetime
import time

from fn import *

from dotenv import load_dotenv
load_dotenv()
dicts = []

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))
# line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# handler = WebhookHandler(LINE_CHANNEL_SECRET)

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
dicts = [0]
@handler.add(PostbackEvent)
def handle_message(event):
    global dicts
    recieved_msg = event.postback.data
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



@handler.add(MessageEvent)
def handle_message(event):
    
    event_type = event.message.type
    if event_type == 'text':
        recieved_msg = event.message.text
        if '韓劇' in recieved_msg:
            country = 'kr'
            # print(item_func(country))
            message = TextSendMessage(text='那你想看哪種韓劇呢?',quick_reply=item_func(country))
            line_bot_api.reply_message(event.reply_token,message)
        elif '美劇' in recieved_msg:
            country = 'us'
            message = TextSendMessage(text='那你想看哪種美劇呢?',quick_reply=item_func(country))
            line_bot_api.reply_message(event.reply_token,message)
        elif '肚子餓' in recieved_msg:
            message = TextSendMessage(text='推薦給你兩款泡麵 ')
            message1 = image_carousel_message()
            message = [message,message1]
            line_bot_api.reply_message(event.reply_token,message)
        elif '嗨' in recieved_msg:
            message = TextSendMessage(text='嗨 要我推薦你影集的話可以按下方按鈕或輸入 韓劇 or 美劇 ')

            line_bot_api.reply_message(event.reply_token,message)
        # elif 'test' in recieved_msg:
        #     message = FlexSendMessage(alt_text='hello',contents=flex_content)
        #     line_bot_api.reply_message(event.reply_token,message)
    elif event_type == 'image':
        message = TextSendMessage(text='這是圖片')
        line_bot_api.reply_message(event.reply_token, message)
 
    
    
    
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
