# instagram-unliker
Simple script for removing your Instagram likes.  
Inspired by [jhnguyen521/InstaUnliker](https://github.com/jhnguyen521/InstaUnliker) 💚  
Powered by [subzeroid/instagrapi](https://github.com/subzeroid/instagrapi) 💚

## 🚧 Rate Limiting

To avoid possible blocking / banning of your account keep the number of posts to unlike at a low level.  
The [current default value](https://github.com/cyb3rko/instagram-unliker/blob/main/unliker.py#L8) worked fine for me while running this script every few hours.

## 🚀 Usage

Open the [unliker.py](unliker.py) file, configure your options at the top and let it run. :)

### 🔒 2FA / MFA

If 2FA is configured for your account, you can still use this script by copying the TOTP secret into the [`mfa_secret`](https://github.com/cyb3rko/instagram-unliker/blob/main/unliker.py#L14) configuration.  
Using the secret the TOTP will be calculated on-the-fly when needed.
