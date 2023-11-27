from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

items_korea=[
                        QuickReplyButton(
                            action=PostbackAction(label="醫療片", data="med_kr",text="我想看醫療片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="校園片", data="school_kr",text="我想看校園片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="愛情片", data="love_kr",text="我想看愛情片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="喜劇片", data="comedy_kr",text="我想看喜劇片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="法政片", data="law_kr",text="我想看法政片")
                        ),
                        
                    ]

items_us=[
                        QuickReplyButton(
                            action=PostbackAction(label="醫療片", data="med_us",text="我想看醫療片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="校園片", data="school_us",text="我想看校園片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="愛情片", data="love_us",text="我想看愛情片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="喜劇片", data="comedy_us",text="我想看喜劇片")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="法政片", data="law_us",text="我想看法政片")
                        ),
                        
                    ]






def Carousel_Template():
    message = TemplateSendMessage(
            alt_text='test',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://img.freepik.com/free-photo/sky-clouds-cinematic-clouds-wallpaper-7_1562-744.jpg',
                        title='Testing',
                        text='website',
                        actions=[
                            URIAction(
                                label='GOOGLE',
                                uri='https://www.google.com'
                            ),
                            URIAction(
                                label='YOUTUBE',
                                uri='https://www.youtube.com'
                            ),
                            URIAction(
                                label='NETFLIX',
                                uri='https://www.netflix.com'
                            ),                           
                        ]
                    ),
                ]
            )
        )
    return message


def image_carousel_message():
    message = TemplateSendMessage(
        alt_text='即將上映',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://img.freepik.com/free-photo/sky-clouds-cinematic-clouds-wallpaper-7_1562-744.jpg',
                    action=URITemplateAction(
                        label="YOUTUBE",
                        uri='https://www.youtube.com'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://img.freepik.com/free-photo/sky-clouds-cinematic-clouds-wallpaper-7_1562-744.jpg',
                    action=URITemplateAction(
                        label='GOOGLE',
                        uri='https://www.google.com'
                    )
                ),
            ]
        )
    )
    return message


def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://img.freepik.com/free-photo/sky-clouds-cinematic-clouds-wallpaper-7_1562-744.jpg",
            title="test1",
            text="test2",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="HI",
                    text="HELLO"
                ),
                URITemplateAction(
                    label="網址",
                    uri="https://www.google.com"
                )
            ]
        )
    )
    return message



