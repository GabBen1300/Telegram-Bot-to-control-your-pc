# Telegram-Bot-to-control-your-pc

This project allows you to create a telegram bot that allows you to control your pc. It offers basic functions that are easily implemented by having access to the computer console

## Fist step

You need a bot TOKEN, go to [@BotFather](https://telegram.me/BotFather) to create a bot and get the token

## Installation

You need [Python](https://www.python.org/downloads/) install the latest version on the site, check that PIP is also installed. To check if it is installed, type in console

```bash
pip --version
```
Then you have to install what we are going to use,

```bash
pip install python-telegram-bot psutil
```

[tbstarter.vbs](https://github.com/GabBen1300/Telegram-Bot-to-control-your-pc/blob/d7ae7f357abd94f76d9c22c5423970bb4d53847b/setup.cmd) must go here: "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" if you want the bot server to start when the pc starts


[nircmdc.exe](https://github.com/GabBen1300/Telegram-Bot-to-control-your-pc/blob/d7ae7f357abd94f76d9c22c5423970bb4d53847b/nircmdc.exe) must be in "%USERPROFILE%\Pictures\Tbot"

[setup.cmd](https://github.com/GabBen1300/Telegram-Bot-to-control-your-pc/blob/d7ae7f357abd94f76d9c22c5423970bb4d53847b/setup.cmd) is only needed if you want to create a self-extracting executable for example with WinRAR that creates and extracts all the necessary files in the right positions

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
