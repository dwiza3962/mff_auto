from lib.emulators.nox_player import NoxPlayer
from lib.functions import load_image
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import numpy as np
import json


def line_select_callback(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata

    print(f"Rect({x1 / img_width}, {y1 / img_height}, {x2 / img_width}, {y2 / img_height})")


nox = NoxPlayer("NoxPlayer")
screen = nox.get_screen_image()
#screen = load_image(r"C:\mff_auto\test.png")
img_height, img_width, _ = screen.shape

fig, ax = plt.subplots(1)

#plt.axis.Axis.zoom()
#plt.get_current_fig_manager().window.state('zoomed')
ax.imshow(screen)
rs = RectangleSelector(ax, line_select_callback, drawtype='box', useblit=False, button=[1], minspanx=5, minspany=5,
                       spancoords='pixels', interactive=True)


plt.show()