from quickly.settings import Settings
import os


class Quickly:
    def __init__(self, path=None):
        self.setting = Settings(path)
        self.config = self.setting.getConfig()

    def add(self, key, path):
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise OSError("{path} does not exists".format(path=path))

        self.config['PATH'][key] = path

    def remove(self, key):
        self.config.remove_option('PATH', key)

    def edit(self, key, path):
        self.config['PATH'][key] = path

    def list(self):
        return self.config['PATH']

    def listKeys(self):
        return list(self.config['PATH'].keys())

    def sync(self):
        self.setting.writeConfig(self.config)

    def cd(self, key):
        if key in self.config['PATH']:
            if (os.path.exists(self.config['PATH'][key])):
                print(self.config['PATH'][key])
            else:
                print("The path for {} which is {} cannot be found".format(key, self.config['PATH'][key]))
        else:
            print("{} has not been added. Cannot continue process".format(key))
