<img src="https://telegra.ph/file/198ae8fd6048244f918ab.jpg" align="right" width="200" height="200"/>

# Prime Music Bot <img src="https://img.shields.io/github/v/release/Toni880/PrimeMusic?color=black&logo=github&logoColor=black&style=social" alt="RELEASE">

[Prime Music Bot](https://github.com/Toni880/PrimeMusic) is a Powerful Telegram Music+Video Bot written in Python using Pyrogram and Py-Tgcalls by which you can stream songs, video and even live streams in your group calls via various sources.

* Youtube, Soundcloud, Apple Music, Spotify, Resso and Telegram Audios & Videos support.
* Written from scratch, making it stable and less crashes.
* Attractive thumbnails, fonts and images,  making experience more user-friendly and interactive.
* Loop, Seek, Shuffle, Specific Skip, Playlists etc support
* Global, Users, Chats Top 10 played tracks stats
* Multi-Language support


# 🔗 An Overview

Here's a brief high-level overview of the Yukki Music Bot:

This project is based on [Pyrogram](https://github.com/pyrogram) and [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls) . Pyrogram is a modern, elegant and asynchronous MTProto API framework.

* For database, Yukki uses the MongoDB to store data and keys. [MongoDB](https://www.mongodb.com/) is a document database with the scalability and flexibility that you want with the querying and indexing that you need.
* Project uses the bs4 web scrapping for getting many platform details. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library for pulling data out of HTML and XML files.
* The project uses the font [`Raleway`](../assets/font2.ttf) as its main font for the thumbnails.
* The projects uses attractive images and icons which you can get in [assets](../assets/) directory.

# ⚡️ Getting Started

### Before deploying Prime Music Bot , please have a look towards [all available config vars](../config/README.md) , also please check [all available commands](../strings/command.yml) of the project.

## 🖇 Generating Pyrogram String Session

- Generate a Pyrogram String Session via [Replit](https://replit.com/@Tonic990/StringSession)

- Generate a Pyrogram String Session via [Telegram String Generation Bot](https://t.me/PrimeStringBot)

# Deployment on Heroku or VPS

<details>
<summary><b> 🚀 Heroku Deployment</b></summary>
<br>

<h4>Click the button below to deploy Prime on Heroku!</h4>    
<a href="https://heroku.com/deploy?template=https://github.com/Toni880/PrimeMusic"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a>

<h4>Click the button below to deploy Prime on bot Telegram!</h4>
<a href="https://telegram.dog/XTZ_HerokuBot?start=VG9uaTg4MC9QcmltZU11c2ljIG1haW4"><img src="https://img.shields.io/badge/Deploy%20To%20Bot%20Telegram-blue?style=for-the-badge&logo=telegram" width="200""/></a>
</details>

<details>
<summary><b>🔗 Deploy on VPS</b></summary>
<br>
    
### Tutorial Deploy on VPS
```console
root@PrimeMusic~ $ sudo su
root@PrimeMusic~ $ apt-get update && apt-get upgrade -y
root@PrimeMusic~ $ screen -S PrimeMusic
root@PrimeMusic~ $ git clone https://github.com/Toni880/PrimeMusic
root@PrimeMusic~ $ cd PrimeMusic
root@PrimeMusic~ $ bash setup
```
> Setup will install each and every requirement, nodejs and pip packages automatically. After successfull installation of requirements , setup will ask you to input your vars.
> Please input your vars correctly.
```console
root@PrimeMusic~ $ bash start
```

</details>

## 🗂 License

This project is licensed under the **GNU General Public License v3**. All designs were created by [@Toni880](https://github.com/Toni880) .

See [LICENSE](../LICENSE) for more information.

Special thanks to these amazing projects/people which/who help power Prime Music Bot:

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls)
- [CallsMusic Team](https://github.com/Callsmusic)
- [TheHamkerCat](https://github.com/TheHamkerCat)
- [Charon Baglari](https://github.com/XCBv021)
- [TeamYukki](https://github.com/TeamYukki)
