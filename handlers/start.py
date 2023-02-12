from pyrogram import Client as bot
from pyrogram.types import *
from pyrogram import filters



import pyrogram
from pyrogram import filters

import time
import os
import threading

#bot_token = os.environ.get("TOKEN", "5880210499:AAFUP0kydgSnU3S8RUWylcIUgkyaXII_l4k") 
#api_hash = os.environ.get("HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e") 
#api_id = os.environ.get("ID", "6")
#bot = Client("mybot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)




@bot.on_message(filters.text)
def save(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):

    # joining chats
    if "https://t.me/+" in message.text or "https://t.me/joinchat/" in message.text:
        bot.send_message(message.chat.id,"**Private chats are not supported yet.**", reply_to_message_id=message.id)
  

    elif "https://t.me/" in message.text:
        datas = message.text.split("/")
        msgid = int(datas[-1])
        if "https://t.me/c/" in message.text:
            bot.send_message(message.chat.id,"**Sorry, private chat is not supported by bot.**", reply_to_message_id=message.id)

        # public
        else:
            username = datas[-2]
            msg  = bot.get_messages(username,msgid)
    
            if "Document" in str(msg):
                bot.send_document(message.chat.id, msg.document.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)

            elif "Video" in str(msg):
                bot.send_video(message.chat.id, msg.video.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)
            
            elif "Animation" in str(msg):
                bot.send_animation(message.chat.id, msg.animation.file_id, reply_to_message_id=message.id)

            elif "Sticker" in str(msg):
                bot.send_sticker(message.chat.id, msg.sticker.file_id, reply_to_message_id=message.id)

            elif "Voice" in str(msg):
                bot.send_voice(message.chat.id, msg.voice.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)    

            elif "Audio" in str(msg):
                bot.send_audio(message.chat.id, msg.audio.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)    

            elif "text" in str(msg):
                bot.send_message(message.chat.id, msg.text, entities=msg.entities, reply_to_message_id=message.id)

            elif "Photo" in str(msg):
                bot.send_photo(message.chat.id, msg.photo.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)


# infinty polling
bot.run()
