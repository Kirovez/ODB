
import telebot
from telebot import apihelper

bot = telebot.TeleBot("TOKEN HERE")
apihelper.proxy = {
  'https': 'socks5://telegram:telegram@wmwdt.tgvpnproxy.me:1080'
}



def recursivePolling():
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(10)
        recursivePolling()

if __name__ == "__main__":
    recursivePolling()
