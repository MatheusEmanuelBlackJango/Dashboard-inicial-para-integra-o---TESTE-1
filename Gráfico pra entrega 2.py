import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as x
import pandas




df = pandas.read_csv('https://raw.githubusercontent.com/MatheusEmanuelBlackJango/Gr-fico-pra-entrega2/main/planilha%20gr%C3%A1ficos%20pra%20entrega%202.csv')



fig = make_subplots(
                    vertical_spacing=0.15,
                    horizontal_spacing=0.05,
                    #subplot_titles=('TENSÃO', 'CORRENTE', 'CARGA ESPECÍFICA', 'CARGA DO BANCO'),
                    rows=2, cols=3

)

fig.add_trace(x.Bar(
                    name='Tensão',
                    x= df['tempo1'],
                    y= df['tensão']),
                    row=1, col=2
)


fig.add_trace(x.Bar(
                    name='Corrente',
                    x= df['tempo1'],
                    y= df['corrente']),
                    row=1, col=3
)


# fig.add_trace(x.Bar(
#                   name='carga específica',
#                   x= df['celulas'],
#                   y= df['carga específica']),
#                   row=2, col=2
# )

fig.add_trace(x.Scatter(
                  name='CE1',
                  x= df['tempo2'],
                  y= df['CE1'],
                  hovertemplate='célula1 - %{x} horas - %{y}% de carga'),
                  row=2, col=2
)

fig.add_trace(x.Scatter(
                  name='CE2',
                  x= df['tempo2'],
                  y= df['CE2'],
                  hovertemplate='célula2 - %{x} horas - %{y}% de carga'),
                  row=2, col=2
)

# noinspection PyTypeChecker
fig.add_trace(x.Scatter(
                  name='CE3',
                  x= df['tempo2'],
                  y= df['CE3'],
                  marker_color='rgba(203, 254, 0, 0.8)',
                  hovertemplate='célula3 - %{x} horas - %{y}% de carga'),
                  row=2, col=2
)


fig.add_trace(x.Scatter(
                       name='CB',
                       x= df['tempo2'],
                       y= df['carga do banco']),
                       row=2, col=3
)


fig.add_trace(x.Indicator(
    mode = "gauge+number",
    value = 40,
    title = {'text': "temperatura(C°)"},
    domain = {'x': [0, 0.2], 'y': [0.4, 1]}
))

fig.update_layout(
                   # template= 'plotly_dark', #modelo
                   width=900,  # dimencionamento horizontal da área de plotagem (paper)
                   height=465,    # dimensionamento vertical do paper
                   title_xanchor='left', # posição do título
                   title = 'Monitoramento de Baterias',
                   titlefont = {'family':  "Arial", 'size': 40, 'color': 'white'}, # dados do título
                   legend_orientation="v", legend=dict(x=1, y=1), # orientação, posição da legenda (séries)
                   plot_bgcolor='powderblue', # cor da área do gráfico
                   paper_bgcolor='green',
                   modebar_orientation= 'v', modebar_bgcolor='steelblue', # orientação  e cor da modbarra
)

#expressura e cor da borda dos gráficos:

fig.data[0].marker.line.width=3
fig.data[0].marker.line.color='white'

fig.data[1].marker.line.width=3
fig.data[1].marker.line.color='white'

fig.data[2].marker.line.width=3
fig.data[2].marker.line.color='white'

fig.data[3].marker.line.width=3
fig.data[3].marker.line.color='white'

fig.data[4].marker.line.width=3
fig.data[4].marker.line.color='white'

fig.data[5].marker.line.width=3
fig.data[5].marker.line.color='white'

fig.show()
