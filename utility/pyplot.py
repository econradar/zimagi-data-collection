from matplotlib import pyplot
from matplotlib import transforms

import os
import pathlib


pyplot.rcParams.update({'figure.max_open_warning': 0})


class Chart(object):

    border_color = '#555'
    grid_color = '#999'
    background_color = '#eee'
    plot_colors = [
        '#1f77b4',
        '#ff7f0e',
        '#2ca02c',
        '#d62728',
        '#9467bd',
        '#8c564b',
        '#e377c2',
        '#7f7f7f',
        '#bcbd22',
        '#17becf'
    ]


    def __init__(self, xlabel = '', xdata = None, sharex = True, rows = 1, columns = 1, **pyplot_kwargs):
        pyplot_kwargs['squeeze'] = False

        fig, axes = pyplot.subplots(nrows = rows, ncols = columns, sharex = sharex, **pyplot_kwargs)
        self.fig = fig
        self.chart = axes
        self.rows = rows
        self.columns = columns

        self.xlabel = xlabel
        self.set_xdata(xdata)

        self.color_index = {}

        self._initialize_figure()

    def __del__(self):
        pyplot.close(self.fig)


    def _initialize_figure(self):
        self.fig.patch.set_alpha(0)


    def _initialize_chart(self, row, column, title, ylabel):
        self.chart[row][column].grid('on')
        self.chart[row][column].grid(True, linestyle = '--', color = self.grid_color)

        self.chart[row][column].patch.set_facecolor(self.background_color)
        self.chart[row][column].patch.set_alpha(0.9)

        for side in ['top', 'bottom', 'left', 'right']:
            self.chart[row][column].spines[side].set_color(self.border_color)
            self.chart[row][column].spines[side].set_linewidth(2)

        self.chart[row][column].set_title(title)
        title = self.chart[row][column].title
        title.set_weight('bold')

        if row == (self.rows - 1):
            self.chart[row][column].set_xlabel(self.xlabel)
            xlabel = self.chart[row][column].xaxis.get_label()
            xlabel.set_style('italic')
            xlabel.set_size(10)

        self.chart[row][column].set_ylabel(ylabel)
        ylabel = self.chart[row][column].yaxis.get_label()
        ylabel.set_style('italic')
        ylabel.set_size(10)


    def save(self, file_path, **attributes):
        pathlib.Path(os.path.dirname(file_path)).mkdir(parents = True, exist_ok = True)
        self.fig.savefig(
            file_path,
            facecolor = self.fig.get_facecolor(),
            edgecolor = 'none',
            **attributes
        )
        return file_path


    def set_xdata(self, data):
        self.xdata = data if data is not None else []

    def add(self, plot_type, ydata, ylabel = '', title = '', row = 0, column = 0, **attributes):
        chart_index = "{}:{}".format(row, column)
        color = self.plot_colors[self.color_index.get(chart_index, 0) % len(self.plot_colors)]
        if 'color' not in attributes:
            attributes['color'] = color

        if chart_index not in self.color_index:
            self.color_index[chart_index] = 0
            self._initialize_chart(row, column, title, ylabel)

        plot = getattr(self.chart[row][column], plot_type)
        plot(self.xdata, ydata, **attributes)
        self.color_index[chart_index] += 1
        return self


    def xfill(self, row = 0, column = 0, **attributes):
        y_min, y_max = self.chart[row][column].get_ylim()
        self.chart[row][column].fill_between(self.xdata, y_min, y_max,
            interpolate = False,
            **attributes
        )
        return self

    def yfill(self, data1, data2, interpolate = True, row = 0, column = 0, **attributes):
        self.chart[row][column].fill_between(self.xdata, data1, data2,
            interpolate = interpolate,
            **attributes
        )
        return self


    def add_legend(self, row = 0, column = 0, **attributes):
        self.chart[row][column].legend(**attributes)
        return self


class SeriesChart(Chart):

    def __init__(self, dates = None, **attributes):
        attributes['xdata'] = dates
        if 'xlabel' not in attributes:
            attributes['xlabel'] = 'Dates'

        super().__init__(**attributes)

    def _initialize_figure(self):
        super()._initialize_figure()
        self.fig.autofmt_xdate(rotation = 45)
