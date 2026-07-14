import matplotlib.pyplot as plt
import seaborn as sns

class PlotBuilder:
    _plot_type = {
        'scatter': sns.relplot, 'line': sns.relplot,
        'hist': sns.displot,    'kde': sns.displot,    'ecdf': sns.displot,
        'strip': sns.catplot,   'swarm': sns.catplot,  'box': sns.catplot,
        'violin': sns.catplot,  'bar': sns.catplot,    'point': sns.catplot
    }
    def __init__(self, kind: str, data=None, **kwargs):
        if kind not in self._plot_type:
            raise ValueError(f"Kind '{kind}' must be one of {list(self._plot_type.keys())}")
    
        plot_func = self._plot_type[kind]
        self.fig = plot_func(data=data, kind=kind, **kwargs).fig
