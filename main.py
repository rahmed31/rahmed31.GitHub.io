import numpy as np
import os, subprocess
import pickle
import random
from tornado.ioloop import IOLoop
import pandas as pd

# required libraries for plot
from plot_text import cite, notes, dataset_description, header, description, description2, description_search, description_slider, description_text_input
from call_backs import selected_code, input_callback
import bokeh
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper, CustomJS, Slider, TapTool, TextInput, RadioButtonGroup, Div, Paragraph, FileInput, DataTable, TableColumn
from bokeh.palettes import Category20
from bokeh.transform import linear_cmap, transform, factor_mark
from bokeh.plotting import figure, show
from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox, row, layout
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.server.server import Server

# def main():
i = 1

# doc = curdoc()

topic_path = 'topics.txt'
with open(topic_path) as f:
    topics = f.readlines()

X_embedded = np.load('X_embedded.npy')
y_pred = np.load('y_pred.npy')

df = pickle.load(open('df_processed.pickle', "rb" ))

df.info()

y_labels = y_pred

#data sources
source = ColumnDataSource(data=dict(
        x= X_embedded[:,0],
        y= X_embedded[:,1],
        x_backup = X_embedded[:,0],
        y_backup = X_embedded[:,1],
        desc= y_labels,
        titles= df['Title'],
        seam = df['SEAM'],
        category = df['Category'],
        abstracts = df['Preprocessed'],
        keywords = df['Keywords'],
        labels = ["C-" + str(x) for x in y_labels],
        authors = df['Author(s)']
        ))

#hover over information
hover = HoverTool(tooltips=[
        ("Title", "@titles{safe}"),
        # ("Abstract", "@abstracts{safe}"),
        ("Author(s)", "@authors{safe}"),
        ("Keywords", "@keywords"),
        # ("SEAM", "@seam"),
        # ("Category", "@category")
        ],

    point_policy="follow_mouse")

#map colors
initial_palette = Category20[20]
random.Random(42).shuffle(list(initial_palette))

mapper = linear_cmap(field_name='desc',
                     palette=Category20[20],
                     low=min(y_labels), high=max(y_labels))

#prepare the figure
plot = figure(plot_width=700, plot_height=350,
           tools=[hover, 'pan', 'wheel_zoom', 'box_zoom', 'reset', 'save', 'tap', 'crosshair'],
           title="Clustering of MHD Literature with t-SNE and K-Means",
           toolbar_location="above")

#plot settings
plot.scatter('x', 'y', size=11,
          source=source,
          fill_color=mapper,
          line_alpha=1,
          line_width=1.1,
          line_color="blue",
          legend = 'labels')

plot.legend.background_fill_alpha = 0.6

#Keywords
out_text = Paragraph(text= 'Keywords: Slide to specific cluster to see the keywords.', height=25)
input_callback_1 = input_callback(plot, source, out_text, topics)

# currently selected article
div_curr = Div(text="""Click on a point to view the metadata of the research paper.""",height=150)
callback_selected = CustomJS(args=dict(source=source, current_selection=div_curr), code=selected_code())
taptool = plot.select(type=TapTool)
taptool.callback = callback_selected

#WIDGETS
slider = Slider(start=0, end=22, value=22, step=1, title="Cluster #", callback = input_callback_1)
# slider.js_on_change('value', callback)
keyword = TextInput(title="Search:", callback = input_callback_1)
# keyword.js_on_change('value', callback)

#Edit function so that file outputs top recommendation as csv file in current working directory
def return_texts(attr, old, new):
    global i
    cwd = os.getcwd()
    output_path = os.path.join(cwd,'TextRecommendations' + str(i) + '.csv')

    cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

    df = pd.DataFrame(cars, columns= ['Brand', 'Price'])

    df.to_csv (output_path, index = False, header=True)

    i += 1
    # recommendations.to_csv(output_path)
    subprocess.run(['open', output_path], check=True)
    # print(cwd)

file_input = FileInput(accept=".txt,.pdf,")
file_input.on_change('value', return_texts)

#pass call back arguments
input_callback_1.args["text"] = keyword
input_callback_1.args["slider"] = slider
# column(,,widgetbox(keyword),,widgetbox(slider),, notes, cite, cite2, cite3), plot

#STYLE
header.sizing_mode = "stretch_width"
header.style={'color': '#2e484c', 'font-family': 'Julius Sans One, sans-serif;'}
header.margin=5

description.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
description.sizing_mode = "stretch_width"
description.margin = 5

description2.sizing_mode = "stretch_width"
description2.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
description2.margin=10

description_slider.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
description_slider.sizing_mode = "stretch_width"

description_search.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
description_search.sizing_mode = "stretch_width"
description_search.margin = 5

description_text_input.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
description_text_input.sizing_mode = "stretch_width"
description_text_input.margin = 5

# slider.sizing_mode = "scale_both"
slider.width = 590
slider.margin=15

# keyword.sizing_mode = "scale_both"
keyword.width = 615
keyword.margin=15

div_curr.style={'color': '#BF0A30', 'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
div_curr.sizing_mode = "scale_both"
div_curr.margin = 20

out_text.style={'color': '#0269A4', 'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
out_text.sizing_mode = "scale_both"
out_text.margin = 20

plot.sizing_mode = "scale_both"
plot.margin = 5

dataset_description.sizing_mode = "stretch_width"
dataset_description.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
dataset_description.margin=10

notes.sizing_mode = "stretch_width"
notes.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
notes.margin=10

cite.sizing_mode = "stretch_width"
cite.style ={'font-family': 'Helvetica Neue, Helvetica, Arial, sans-serif;', 'font-size': '1.1em'}
cite.margin=10

r = row(div_curr,out_text)
r.sizing_mode = "stretch_width"

#Page layout
l = layout([
        [header],
        [description],
        [description2],
        [description_slider, description_search, description_text_input],
        [slider, keyword, file_input],
        [out_text],
        [plot],
        [div_curr],
        [dataset_description, notes, cite]
        ])

l.sizing_mode = "scale_both"

curdoc().add_root(l)
# doc.title = "Display of Clusters"
# show(l)
# curdoc().add_root(l)
