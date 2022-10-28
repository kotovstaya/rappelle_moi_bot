import json

class User:
    def __init__(self, username):
        self.username = username
        self.DB = {}
        self.current_folder = None
        self.current_source = None
        self.current_password = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        repr = []
        for k, v in self.DB.items():
            s = f"folder: {k}:"
            if type(v) == dict:
                for kk, vv in v.items():
                    s += f"\n\t {kk} -> {vv}"
            repr.append(s)

        return "\n"+"\n".join(repr)

    # def to_json(self):
    #     return json.dumps(
    #         self.__str__(), default=lambda o: o.__dict__,
    #         sort_keys=True, indent=4)

    def list_folders(self):
        return list(self.DB.keys())

    def update_current_folder(self, folder: str):
        self.current_folder = folder

    def update_current_source(self, source: str):
        self.current_source = source

    def update_current_password(self, password: str):
        self.current_password = password

    def add_folder(self, folder: str):
        self.update_current_folder(folder)
        if folder not in self.DB:
            self.DB[folder] = {}

    def add_source(self, source: str):
        self.update_current_source(source)
        if source not in self.DB["self.current_folder"]:
            self.DB[self.current_folder][source] = None

    def add_password(self, password: str):
        self.update_current_password(password)
        self.DB[self.current_folder][self.current_source] = password

    def add_all_info(self, folder: str, source: str, password: str):
        self.add_folder(folder)
        self.add_source(source)
        self.add_password(password)

    def get_password(self, folder: str, source: str):
        return self.DB[folder][source]