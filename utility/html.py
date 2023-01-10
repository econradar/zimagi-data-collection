from .data import ensure_list

import math


class HTML(object):

    def __init__(self):
        self.tags = []


    def add_html(self, name, content = None, **attributes):
        self.tags.append(self.tag(name, content, **attributes))
        return self


    def tag(self, name, content = None, id = None, classes = None, **attributes):
        id = '' if id is None else ' id="{}"'.format(id)
        classes = '' if classes is None else ' class="{}"'.format(' '.join(ensure_list(classes)))

        attributes = " ".join([ '{}="{}"'.format(key, value) for key, value in attributes.items() if value is not None ]).strip()
        if attributes:
            attributes = " {}".format(attributes)

        if content and isinstance(content, (list, tuple)):
            content = "\n".join(content)
        if not content:
            content = ''

        return "<{}{}{}{}>{}</{}>".format(name, id, classes, attributes, content, name)


    def text(self, text, **attributes):
        return self.tag('p', text, **attributes)

    def add_text(self, text, **attributes):
        return self.add_html('p', text, **attributes)

    def bold(self, text, **attributes):
        return self.tag('b', text, **attributes)

    def add_bold(self, text, **attributes):
        return self.add_html('b', text, **attributes)

    def italic(self, text, **attributes):
        return self.tag('i', text, **attributes)

    def add_italic(self, text, **attributes):
        return self.add_html('i', text, **attributes)

    def underline(self, text, **attributes):
        return self.tag('u', text, **attributes)

    def add_underline(self, text, **attributes):
        return self.add_html('u', text, **attributes)


    def h2(self, text, **attributes):
        return self.tag('h2', text, **attributes)

    def add_h2(self, text, **attributes):
        return self.add_html('h2', text, **attributes)

    def h3(self, text, **attributes):
        return self.tag('h3', text, **attributes)

    def add_h3(self, text, **attributes):
        return self.add_html('h3', text, **attributes)

    def h4(self, text, **attributes):
        return self.tag('h4', text, **attributes)

    def add_h4(self, text, **attributes):
        return self.add_html('h4', text, **attributes)


    def hr(self):
        return self.tag('hr')

    def add_hr(self):
        return self.add_html('hr')


    def div(self, content = None, **attributes):
        return self.tag('div', content, **attributes)

    def add_div(self, content = None, **attributes):
        return self.add_html('div', content, **attributes)

    def span(self, content = None, **attributes):
        return self.tag('span', content, **attributes)

    def add_span(self, content = None, **attributes):
        return self.add_html('span', content, **attributes)


    def link(self, url, text = None, **attributes):
        text = url if text is None else text
        return self.tag('a', text, href = url, **attributes)

    def add_link(self, url, text = None, **attributes):
        text = url if text is None else text
        return self.add_html('a', text, href = url, **attributes)


    def image(self, url, width = '100%', height = '100%', **attributes):
        return self.tag('img',
            src = url,
            width = width,
            height = height,
            **attributes
        )

    def add_image(self, url, **attributes):
        return self.add_div(self.image(url, **attributes),
            id = "{}-wrapper".format(attributes['id']) if attributes.get('id', None) else None,
            classes = 'image-wrapper'
        )


    def iframe(self, url, width = '100%', **attributes):
        return self.tag('iframe',
            src = url,
            width = width,
            frameborder = "0",
            scrolling = "no",
            **attributes
        )

    def add_iframe(self, url, **attributes):
        return self.add_div(self.iframe(url, **attributes),
            id = "{}-wrapper".format(attributes['id']) if attributes.get('id', None) else None,
            classes = 'iframe-wrapper'
        )


    def list(self, list_data, id = None, classes = None):
        items = []
        for index, item in enumerate(ensure_list(list_data)):
            items.append(self.tag('li', item,
                id = "{}-{}".format(id, index) if id else None,
                classes = [ 'unordered-list-item' ]
            ))
        return self.tag('ul', items,
            id = id,
            classes = [ 'unordered-list', *classes ] if classes else [ 'unordered-list' ]
        )

    def add_list(self, list_data, **attributes):
        return self.add_div(self.list(list_data, **attributes),
            id = "{}-wrapper".format(attributes['id']) if attributes.get('id', None) else None,
            classes = [ 'list-wrapper', 'unordered-list-wrapper' ]
        )


    def ordered_list(self, list_data, id = None, classes = None, start = None):
        items = []
        for index, item in enumerate(ensure_list(list_data)):
            items.append(self.tag('li', item,
                id = "{}-{}".format(id, index) if id else None,
                classes = [ 'ordered-list-item' ]
            ))
        return self.tag('ol', items,
            id = id,
            classes = [ 'ordered-list', *classes ] if classes else [ 'ordered-list' ],
            start = start
        )

    def add_ordered_list(self, list_data, **attributes):
        return self.add_div(self.ordered_list(list_data, **attributes),
            id = "{}-wrapper".format(attributes['id']) if attributes.get('id', None) else None,
            classes = [ 'list-wrapper', 'ordered-list-wrapper' ]
        )


    def table(self, table_data, header = True, row_header = True, id = None, classes = None, **attributes):
        rows = []
        for row_index, row_data in enumerate(table_data):
            columns = []

            for column_index, column_data in enumerate(row_data):
                if header and (row_header and not row_index or not row_header and not column_index):
                    column = self.tag('th', column_data,
                        id = "{}-{}-{}".format(id, row_index, column_index) if id else None,
                        classes = [
                            'table-header',
                            "table-header-{}".format(column_index if row_header else row_index),
                            'table-header-even' if (column_index % 2) == 0 else 'table-header-odd'
                        ]
                    )
                else:
                    column = self.tag('td', column_data,
                        id = "{}-{}-{}".format(id, row_index, column_index) if id else None,
                        classes = [
                            'table-column',
                            "table-column-{}".format(column_index if row_header else row_index),
                            'table-column-even' if (column_index % 2) == 0 else 'table-column-odd'
                        ]
                    )
                columns.append(column)

            rows.append(self.tag('tr', columns,
                id = "{}-{}".format(id, row_index) if id else None,
                classes = [
                    'table-row',
                    'table-row-even' if (row_index % 2) == 0 else 'table-row-odd'
                ]
            ))

        return self.tag('table', rows,
            id = id,
            classes = [ 'table', *classes ] if classes else [ 'table' ],
            **attributes
        )

    def add_table(self, table_data, **attributes):
        return self.add_div(self.table(table_data, **attributes),
            id = "{}-wrapper".format(attributes['id']) if attributes.get('id', None) else None,
            classes = 'table-wrapper'
        )


    def sections(self, sections, widths = None, shrink = 0.5, halign = 'center', valign = 'top', **attributes):
        if widths is None:
            widths = math.floor((1 / len(sections)) * 100)

        html_sections = []
        for index, section in enumerate(sections):
            html_sections.append(self.div(section,
                style = "width: {}%; display: inline-block; text-align: {}; vertical-align: {};".format(
                    ((widths[index] if isinstance(widths, (list, tuple)) else widths) - shrink),
                    halign, valign
                )
            ))
        return self.div(html_sections,
            style = "width: 100%; text-align: {};".format(halign),
            **attributes
        )

    def add_sections(self, sections, **attributes):
        return self.add_div(self.sections(sections, **attributes),
            id = "{}-wrapper".format(attributes['id']) if attributes.get('id', None) else None,
            classes = 'section-wrapper'
        )


    def format(self):
        return "\n".join(self.tags)
