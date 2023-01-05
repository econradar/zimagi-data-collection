from systems.models.index import Model


class SeriesIndex(Model('series_index')):

    def get_categories(self):
        categories = []

        def get_categories(category):
            if category is None:
                return []
            return [ category.name, *get_categories(category.parent) ]

        for category in self.series_categories.all():
            categories.extend(get_categories(category))

        return list(reversed(categories))
