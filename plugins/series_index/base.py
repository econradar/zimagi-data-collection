from systems.plugins.index import BasePlugin


class BaseProvider(BasePlugin('series_index')):

    @property
    def data_name(self):
        return self.name

    @property
    def data(self):
        if not getattr(self, '_data_facade', None):
            self._data_facade = self.command.facade(self.data_name, False)
            self._data_facade.set_scope({
                'series_index_id': self.instance.get_id()
            })
        return self._data_facade
