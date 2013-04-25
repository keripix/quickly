from quickly.settings import Settings
import os


class Quickly:
    def __init__(self, path=None):
        self.setting = Settings(path)
        self.config = self.setting.getConfig()

    def add(self, key, path):
        if not os.path.exists(path):
            raise OSError("{path} does not exists".format(path=path))

        self.config['PATH'][key] = path

    def remove(self, key):
        self.config.remove_option('PATH', key)

    def edit(self, key, path):
        self.config['PATH'][key] = path

    def list(self):
        return self.config['PATH']

    def sync(self):
        self.setting.writeConfig(self.config)
