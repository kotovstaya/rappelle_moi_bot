# Rappelle moi bot

This bot helps you to save and manage your passwords.
For example, you don't want to remember some password of your email. 
You can create oneliner in this bot and then get the password at any time.

## How does it work?
```
@rappelle_moi_bot
1. /start - start the bot 
2. /help - info
3. /create - this command create your profile in some sort of database
4. /add_full <folder> <source> <password>
5. /get_password <folder> <source> - get password for email or whatever. 
6. /show - show all folders and sources for specific user.
7 /folder - create just a folder and that's all
8 /source - create just a source in specific folder
9. /password - create just a password in specific folder for specific source
10. /remove - remove user from the database  
```

### Examples
1. Сreate and remove user
```
/create
/remove
```

2. Сreate user and add some password
   1. ```
      /create
      /add_full email some_email@gmail.com fuzz
      /add_full email some_email2@yahoo.com qwerty
      /show
      /get_pass email some_email@gmail.com
      ```
   2. ```
      /create
      /folder email
      /source some_email@gmail.com
      /folder email
      /password fuzz
      /source some_email2@yahoo.com
      /password querty
      /show
      /get_pass email some_email@gmail.com
      ```
