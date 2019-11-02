from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go


def reg_plot(x,y,predictions,names):
    trace0 = go.Scatter(
        x = x,
        y = y,
        mode = 'markers',
        name = 'Data'
    )
    reg_traces = []
    for i,prediction in enumerate(predictions): ##lastone excluded because of visualization
        reg_traces.append(go.Scatter(
                                x = prediction[0],
                                y = prediction[1],
                                mode = 'lines',
                                name = f'Regressor {names[i]}'
                                )
                         )

    layout = go.Layout(
        title = "Synthetic data",
    )

    data = [trace0] + reg_traces
    return iplot(go.Figure(data=data, layout=layout))

def grad_hist_plot(x,y,th):
    trace0 = go.Scatter(
        x = x,
        y = y,
        mode = 'markers',
        name = 'Data'
    )
    grad_traces = []
    for i,t in enumerate(th.tolist()): ##lastone excluded because of visualization
        grad_traces.append(go.Scatter(
                                x = x,
                                y = t[0]*x+t[1],
                                mode = 'lines',
                                )
                         )

    layout = go.Layout(
        title = "Gradients History",
    )

    data = [trace0] + grad_traces
    return iplot(go.Figure(data=data, layout=layout))
