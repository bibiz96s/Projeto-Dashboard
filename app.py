from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("EvasãoSérieHistórica2024.csv", encoding='latin1',delimiter=';')

opcoes = df.columns.tolist()
#Criando o Grafico
#fig = px.bar(df, x="Ano", y="Vinculados", title="Dados sobre os alunos da Engenharia de Computacao")


app.layout = html.Div(children=[
    html.H1(children='Dados sobre os alunos da Engenharia de Computação'),


    dcc.Dropdown(opcoes, value= ['Ingressantes'], id='color',multi=True),
    dcc.Dropdown(opcoes, value= 'Vinculados', id='y'),
    
    dcc.Graph(
        id='grafico-ecomp'
    )
])


@callback(
    Output('grafico-ecomp', 'figure'),
    Input('color', 'value'),
    Input('y', 'value')
)
def update_output(value_color,value_y):

    
    fig = px.bar()

    for coluna in value_color:
        print(coluna)
        fig.add_trace(px.bar(df, x="Ano", y=value_y,color=coluna, title=f"Dados sobre {coluna} e {value_y}").data[0],)

    return fig


if __name__ == '__main__':
    app.run(debug=True)
