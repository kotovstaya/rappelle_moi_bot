import os

from dotenv import load_dotenv

from bot import RappelleMoiBot
from utils import get_logger

load_dotenv()

logger = get_logger(__name__)


def main():
    token = os.getenv("TOKEN")
    port = int(os.getenv('PORT'))
    db_path = os.getenv("DATABASE_PATH")
    heroku_url = os.getenv("HEROKU_URL")

    rmb = RappelleMoiBot(token, port, db_path, heroku_url)
    rmb.add_handlers()
    rmb.start_bot()


if __name__ == '__main__':
    main()
