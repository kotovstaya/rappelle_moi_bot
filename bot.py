from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from users import User
from utils import load_pickle, get_logger, save_db_decorator

logger = get_logger(__name__)


class RappelleMoiBot:
    def __init__(self,
                 token: str,
                 port: int,
                 database_filepath: str,
                 heroku_url: str):
        self.token = token
        self.port = port
        self.heroku_url = heroku_url
        self.database_filepath = database_filepath
        self.updater = self._init_updater()
        self.dp = self._init_dispatcher()
        self.DATABASE = self._init_db()

    def _init_db(self):
        try:
            return load_pickle(self.database_filepath)
        except FileNotFoundError as ex:
            return {}

    def echo(self, update, context):
        update.message.reply_text(update.message.text)

    def error(self, update, context):
        logger.warning('Update "%s" caused error "%s"', update, context.error)

    def _get_username(self, update):
        return update.message.chat.username


    @save_db_decorator
    def create_user(self, update, context):
        username = self._get_username(update)
        if username in self.DATABASE:
            update.message.reply_text(f"{username} is already in DATABASE")
        else:
            self.DATABASE[username] = User(username)
            logger.info(self.DATABASE[username].username)
            update.message.reply_text(self.DATABASE[username].username)

    @save_db_decorator
    def remove_user(self, update, context):
        username = self._get_username(update)
        self.DATABASE.pop(username)
        update.message.reply_text(f"{username} has been removed")

    @save_db_decorator
    def folder(self, update, context):
        _, folder_name = update.message.text.split(" ")
        username = self._get_username(update)
        self.DATABASE[username].add_folder(folder_name)

    @save_db_decorator
    def source(self, update, context):
        _, source = update.message.text.split(" ")
        username = self._get_username(update)
        self.DATABASE[username].add_source(source)

    @save_db_decorator
    def password(self, update, context):
        _, password = update.message.text.split(" ")
        username = self._get_username(update)
        self.DATABASE[username].add_password(password)

    def get_password(self, update, context):
        _, folder, source = update.message.text.split(" ")
        username = self._get_username(update)
        passw = self.DATABASE[username].get_password(folder, source)
        update.message.reply_text(f"password : {passw}")

    def show(self, update, context):
        username = self._get_username(update)
        print(self.DATABASE[username])
        update.message.reply_text(self.DATABASE[username])

    def start(self, update, context):
        update.message.reply_text('Hi!')

    def help(self, update, context):
        update.message.reply_text('Help!')

    def add_handler(self, name, func):
        self.dp.add_handler(CommandHandler(name, func))
        return self

    def add_message_handler(self, func):
        self.dp.add_handler(MessageHandler(Filters.text, func))
        return self

    def add_error_handler(self, func):
        self.dp.add_error_handler(func)
        return self

    def add_handlers(self):
        (
            self.add_handler("hehe", self.start)
            .add_handler("help", self.help)
            .add_handler("create", self.create_user)
            .add_handler("remove_user", self.remove_user)
            .add_handler("folder", self.folder)
            .add_handler("source", self.source)
            .add_handler("password", self.password)
            .add_handler("show", self.show)
            .add_handler("get_pass", self.get_password)
            .add_message_handler(self.echo)
            .add_error_handler(self.error)
        )

    def _init_updater(self):
        return Updater(self.token, use_context=True)

    def _init_dispatcher(self):
        return self.updater.dispatcher

    def start_bot(self):
        # self.updater.start_polling()
        self.updater.start_webhook(listen="0.0.0.0",
                                   port=self.port,
                                   url_path=self.token,
                                   webhook_url=f"{self.heroku_url}{self.token}")
        self.updater.idle()