# instagram-unliker
Simple script for removing your Instagram likes.  
Inspired by [jhnguyen521/InstaUnliker](https://github.com/jhnguyen521/InstaUnliker) 💚  
Powered by [subzeroid/instagrapi](https://github.com/subzeroid/instagrapi) 💚

## ⚙️ Configuration

Open the [unliker.py](unliker.py) file and configure your options at the top. 

### 🔒 2FA / MFA

If 2FA is configured for your account, you can still use this script by copying the TOTP secret into the [`mfa_secret`](https://github.com/cyb3rko/instagram-unliker/blob/main/unliker.py#L14) configuration.  
Using the secret the TOTP will be calculated on-the-fly when needed.

## 🚀 Usage

### With uv

The "modern" way is to use [uv](https://docs.astral.sh/uv).

1. Install uv: https://docs.astral.sh/uv/getting-started/installation
2. Open a terminal and navigate to the project folder.
3. Run `uv run unliker.py`.

### With pip/python

The "classic" way is to use `pip` and `Python` itself.

1. Install Python and pip on your system.
2. Open a terminal and navigate to the project folder.
3. Run `python -m venv .venv`
4. Run `source .venv/bin/activate`
5. Run `pip install -r requirements.txt`
6. Run `python unliker.py`

## 🚧 Rate Limiting

To avoid possible blocking / banning of your account keep the number of posts to unlike at a low level.  
The [current default value](https://github.com/cyb3rko/instagram-unliker/blob/main/unliker.py#L9) worked fine for me while running this script every few hours.
