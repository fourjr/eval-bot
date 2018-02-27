# _eval
Stuff about  what this bot is is below. 

## Selfhosting
Firstly, let me get this clear. I will **not** provide support for selfhosting _eval

Clone the `raw` branch to your personal laptop
```bash
git clone https://github.com/fourjr/eval-bot@raw
```

If you use the `master ` branch, you would have the bot that I currently use, which includes the list of allowed people and requirements.

In the raw branch, there is a default set of requirements needed for the bot to function in `requirements.txt`. Do not remove any of them.

### Config
Head over to the config folder, fill up `config.json` as so:
```json
{
	"token":"discord bot token",
	"gittoken":"code recieved from git auth described below, but technically this is useless :/"
}
```
Fill up `access.json` with an array of user IDs that are allowed to use the bot. If you add the `"public" ` element to the array, anyone can use the bot.
```json
[
	"public"
]
```
Anyone can use the bot with the above config.

### What about Heroku?
The bot is already made to work with the Heroku platform.

The environmental variables should be set as follows
Key | Description 
token | discord bot token
gittoken | code recieved from git auth described below

`config/config.json` should stay unmodified and `config/access.json` should follow the same steps as normal config.

### Github Authentication
Go to [this website](soontm.com) and authorise your github account. This should redirect you to a page hosted by `herokuapp.com` with a JSON.

Copy the value in `code ` and insert that it into your `config.json`

## I still don't get it!
You aren't fit to host this bot yourself then. Learn python and learn how to use a pc first, unless you can find someone who bothers to help you.

## What are the commands that are in this bot?
Prefix is `_`, this can only be changed by editing source code.

`_eval ` - Evaluates python with preset variables such as `ctx`, `session` and `bot`.    
`_require <package name>` - This will edit `requirements.txt` and add the package name at the end of the list. This will **only work on Heroku hosting**    
`_restart` - This will add a line into `restart.txt ` to trigger a restart on the bot. This will **only work on Heroku hosting**, remind me to fix it

## So finally, what's this.. bot?
This bot is an eval bot. It is made in **Python 3.6** in discord.py

Anyone with access to the bot **has the potential** to run dangerous commands on it and thus it is highly discouraged to enable public eval mode.

The following are restrictions placed to hopefully protect the bot. The bot owner overwrites all restrictions:
- Bot cannot be used in DMs
- There are filtered words such as `os`, refer to source.

There is a public and private eval mode for this.

## One more question! What's that `/examples ` folder for?
That's for easy copying of a basic discord.py eval command in both a cog and in the main bot.

Take it if you want, but don't credit me because I didn't make it myself!

## Uh... I felt the need for this... How can I contribute?
I personally don't think there's anything that needs to be added but pull requests stay open! Ensure changes are tested. Bugs to be reported in github issues.