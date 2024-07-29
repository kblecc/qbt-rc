#!/usr/bin/python
# -*- coding: UTF-8 -*-
import telebot
import qbittorrentapi
import json
import sqlite3
import os
os.chdir(os.path.dirname(__file__))
with open('config.json', 'r', encoding='utf-8') as f:
    conf = json.loads(f.read())
    f.close()
QB_host=conf["QB_host"]
QB_port=conf["QB_port"]
QB_username=conf["QB_username"]
QB_password=conf["QB_password"]
Telegram_bot_api=conf["Telegram_bot_api"]
Telegram_user_id=conf["Telegram_user_id"]
Rule_list=conf["Rule"]
Download_dir=conf["Download_dir"]

if __name__ == '__main__':

    # Qbittorrent Config Check
    qbt_client = qbittorrentapi.Client(host=QB_host, port=QB_port, username=QB_username, password=QB_password)
    try:
        qbt_client.auth_log_in()
        print("Success: Qbittorrent Connected")
    except qbittorrentapi.LoginFailed as e:
        print(f"Error: Login Failed, {e}")
    except:
        print(f"Error: Config Error")


    if Telegram_bot_api !="":
        try:
            log="hello world"
            bot = telebot.TeleBot(Telegram_bot_api)
            bot.send_message(chat_id=Telegram_user_id,text=log,parse_mode='Markdown')
            print(f"Success: Telegram Bot Connected")
        except:
            print(f"Error: Telegram Bot Config")

