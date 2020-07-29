from bokeh.models.callbacks import CustomJS
from bokeh.models import ColumnDataSource, CustomJS, Slider

# handle the currently selected article
def selected_code():
    code = """
            var titles = [];
            var authors = [];
            var seam = [];
            var category = [];
            cb_data.source.selected.indices.forEach(index => titles.push(source.data['titles'][index]));
            cb_data.source.selected.indices.forEach(index => authors.push(source.data['authors'][index]));
            cb_data.source.selected.indices.forEach(index => seam.push(source.data['seam'][index]));
            cb_data.source.selected.indices.forEach(index => category.push(source.data['category'][index]));

            title = "<h4>" + titles[0].toString().replace(/<br>/g, ' ') + "</h4>";
            authors = "<p1><b>Author(s):</b> " + authors[0].toString().replace(/<br>/g, ' ') + "<br>"
            seam = "<p1><b>Seam:</b> " + seam[0].toString().replace(/<br>/g, ' ') + "<br>"
            category = "<p1><b>Category:</b> " + category[0].toString().replace(/<br>/g, ' ') + "<br>"

            //abstract = "<br><b>Abstract Words: </b>" + abstracts[0].toString() + "<br>"

            current_selection.text = title + authors + seam + category
            current_selection.change.emit();
        """

    return code

# handle the keywords and search
def input_callback(plot, source, out_text, topics):

    # slider call back for cluster selection

    callback = CustomJS(args=dict(p=plot, source=source, out_text=out_text, topics=topics), code="""
                    				var key = text.value;
                    				key = key.toLowerCase();
                    				var cluster = slider.value;
                    var data = source.data;


                    x = data['x'];
                    y = data['y'];
                    x_backup = data['x_backup'];
                    y_backup = data['y_backup'];
                    labels = data['desc'];
                    abstract = data['abstracts'];
                    titles = data['titles'];
                    authors = data['authors'];
                    category = data['category'];

                    if (cluster == '22') {
                        out_text.text = 'Keywords: Slide to specific cluster to see the keywords.';
                        for (i = 0; i < x.length; i++) {
                            						if(abstract[i].includes(key) ||
                            						titles[i].includes(key) ||
                                                    category[i].includes(key) ||
                            						authors[i].includes(key)) {
                            							x[i] = x_backup[i];
                            							y[i] = y_backup[i];
                            						} else {
                            							x[i] = undefined;
                            							y[i] = undefined;
                            						}
                        }
                    }
                    else {
                        out_text.text = 'Keywords: ' + topics[Number(cluster)];
                        for (i = 0; i < x.length; i++) {
                            if(labels[i] == cluster) {
                                							if(abstract[i].includes(key) ||
                                							titles[i].includes(key) ||
                                                            category[i].includes(key) ||
                                							authors[i].includes(key)) {
                                								x[i] = x_backup[i];
                                								y[i] = y_backup[i];
                                							} else {
                                								x[i] = undefined;
                                								y[i] = undefined;
                                							}
                            } else {
                                x[i] = undefined;
                                y[i] = undefined;
                            }
                        }
                    }
                source.change.emit();
        """)
    return callback
