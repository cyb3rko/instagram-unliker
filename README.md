# instagram-unliker
Simple script for removing your Instagram likes.  
Inspired by and based on [jhnguyen521/InstaUnliker](https://github.com/jhnguyen521/InstaUnliker) 💛

## 🆚 Variations

### Base

This is the basic script without additions.

### Cronitor

Based on the base script this is a version with Cronitor support ([https://cronitor.io](https://cronitor.io)).  
Using that you can always see if the script works or not, even without direct access to your machine running the script.

## ⛔ Rate Limiting

To avoid possible blocking / banning of your account keep the number of posts to unlike at a low level.  
The [current default value](https://github.com/cyb3rko/instagram-unliker/blob/main/1%20-%20base/unliker.py#L8) worked fine for me while running this script every few hours.

## 🏃‍♂️ Usage

### Base

Open the <a href="1 - base/unliker.py">unliker.py file</a>, configure your options at the top and let it run. :)

### Cronitor

First create an account on [https://cronitor.io](https://cronitor.io).  
Then you have to create a job for your unliker. Either you do that via the web ui or you use the <a href="2 - cronitor/cronitor-setup.py">cronitor-setup.py script</a> to let it do that for you.  
The last step is the same as above: Open the <a href="2 - cronitor/unliker_cron.py">unliker_cron.py file</a>, configure your options at the top and let it run. :)
