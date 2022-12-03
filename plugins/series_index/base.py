from systems.plugins.index import BasePlugin


class BaseProvider(BasePlugin('series_index')):

    @property
    def data(self):
        return self.command.facade(self.name, False)
