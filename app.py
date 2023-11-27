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

from fn import *

from dotenv import load_dotenv
load_dotenv()

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

@handler.add(PostbackEvent)
def handle_message(event):
    recieved_msg = event.postback.data
    if 'med_kr' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)    
    elif 'school_kr' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'love_kr' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'law_kr' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'comedy_kr' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'med_us' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'school_us' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'love_us' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'comedy_us' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'law_us' in recieved_msg:
        message = TextSendMessage(text='嗨')
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent)
def handle_message(event):
    
    event_type = event.message.type
    if event_type == 'text':
        recieved_msg = event.message.text
        if '韓劇' in recieved_msg:
            message = TextSendMessage(text='那你想看哪種韓劇呢?',quick_reply=QuickReply(items_korea))
            line_bot_api.reply_message(event.reply_token,message)
        elif '美劇' in recieved_msg:
            message = TextSendMessage(text='那你想看哪種美劇呢?',quick_reply=QuickReply(items_us))
            line_bot_api.reply_message(event.reply_token,message)
        
    elif event_type == 'image':
        message = TextSendMessage(text='這是圖片')
        line_bot_api.reply_message(event.reply_token, message)

    
    
    
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
