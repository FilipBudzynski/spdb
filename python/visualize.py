import matplotlib.pyplot as plt


def plot_points_layers(
    layers, colors=None, sizes=None, labels=None, title=None, ax=None, legend=True
):
    """
    Plot multiple GeoDataFrame point layers on a single matplotlib axis.

    Args:
        layers (list): List of GeoDataFrames to plot (must be point geometries).
        colors (list): List of colors for each layer.
        sizes (list): List of marker sizes for each layer.
        labels (list): List of labels for each layer.
        title (str): Plot title.
        ax (matplotlib.axes.Axes): Existing axis to plot on (optional).
        legend (bool): Whether to show legend.
    Returns:
        matplotlib.axes.Axes: The axis with the plot.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 10))
    if colors is None:
        colors = ["blue", "green", "red", "orange", "purple"]
    if sizes is None:
        sizes = [20] * len(layers)
    if labels is None:
        labels = [f"Layer {i+1}" for i in range(len(layers))]
    for i, gdf in enumerate(layers):
        gdf.plot(
            ax=ax,
            color=colors[i % len(colors)],
            markersize=sizes[i % len(sizes)],
            label=labels[i],
        )
    if title:
        ax.set_title(title)
    ax.set_axis_off()
    if legend:
        ax.legend()
    return ax
