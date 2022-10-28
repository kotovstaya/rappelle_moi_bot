import logging
import pickle


def get_logger(name):
    logging.basicConfig(format=(
        f"%(asctime)s - %(name)s - "
        f"%(levelname)s - %(message)s"),
        level=logging.INFO)
    return logging.getLogger(name)


def load_pickle(path):
    return pickle.load(open(path, 'rb'))


def dump_pickle(obj, path):
    pickle.dump(obj, open(path, 'wb'))


def save_db_decorator(func):
    def deco(self, update, context):
        func(self, update, context)
        dump_pickle(self.DATABASE, self.database_filepath)
    return deco