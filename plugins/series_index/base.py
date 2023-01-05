from systems.plugins.index import BasePlugin


class BaseProvider(BasePlugin('series_index')):

    @property
    def data_name(self):
        return self.name


    @property
    def data_facade(self):
        return self.command.facade(self.data_name, False)

    @property
    def data(self):
        if not getattr(self, '_data_facade', None):
            self._data_facade = self.data_facade
            self._data_facade.set_scope({
                'series_index_id': self.instance.get_id()
            })
        return self._data_facade


    def get_system_fields(self):
        return [
            'series_index',
            'id',
            'created',
            'updated'
        ]

    def get_calculated_fields(self):
        return list(set(self.data.fields) - set(self.get_system_fields()))


    def format_table_info(self, doc):
        properties = self.get_properties(doc)
        table_info = []

        for key in sorted(properties.keys()):
            table_info.append([ key, properties[key] ])
        return table_info

    def get_properties(self, doc):
        instance = self.check_instance('get properties')
        return {
            'Source': doc.bold(instance.source.name),
            'Source ID': instance.external_id,
            'Popularity': "{}/100".format(doc.bold(instance.popularity)),
            'First Observation': doc.bold(self.time.to_date_string(instance.start)),
            'Last Observation': doc.bold(self.time.to_date_string(instance.end)),
            'Frequency': doc.bold(instance.frequency),
            'Seasonal Adjustment': instance.seasonal_adjustment,
            'Units': instance.units
        }
