from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters



import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, InviteHashExpired

import time
import os
import threading

@Client.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply("Hey! It's Just a Cloner Bot example source Code")


@Client.on_message(filters.text)
def save(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):

    # joining chats
    if "https://t.me/+" in message.text or "https://t.me/joinchat/" in message.text:
        message.reply("its pvt")
 
   # getting message
    elif "https://t.me/" in message.text:

        datas = message.text.split("/")
        msgid = int(datas[-1])

        # private
        if "https://t.me/c/" in message.text:
            #chatid = int("-100" + datas[-2])
            message.reply("private links not supported.")

        else:
            username = datas[-2]
            msg  = Client.get_messages(chat_id=username, msgid)
    
            if "Document" in str(msg):
                Client.send_document(message.chat.id, msg.document.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)

            elif "Video" in str(msg):
                Client.send_video(message.chat.id, msg.video.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)
            
            elif "Animation" in str(msg):
                Client.send_animation(message.chat.id, msg.animation.file_id, reply_to_message_id=message.id)

            elif "Sticker" in str(msg):
                Client.send_sticker(message.chat.id, msg.sticker.file_id, reply_to_message_id=message.id)

            elif "Voice" in str(msg):
                Client.send_voice(message.chat.id, msg.voice.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)    

            elif "Audio" in str(msg):
                Client.send_audio(message.chat.id, msg.audio.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id)    

            elif "text" in str(msg):
              #  message.reply(msg.text)
                Client.send_message(message.chat.id, msg.text.markdown)
            elif "Photo" in str(msg):
                Client.send_photo(message.chat.id, msg.photo.file_id, caption=msg.caption, caption_entities=msg.caption_entities, reply_to_message_ids=message.id)


# infinty polling
#Client.run()
