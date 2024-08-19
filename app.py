from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("EvasãoSérieHistórica2024.xlsx")

#Criando o Grafico
fig = px.bar(df, x="Ano", y="Vinculados", title="Dados sobre os alunos da Engenharia de Computacao")
opcoes = [
    "Ano",
    "Vinculados",
    "Formados",
    "Ingressantes",
    "Continuaram Vinculados no Proximo Ano",
    "Evadidos p/Metodo",
    "Evadidos Real",
    "Taxa Evolução Vinculados",
    "Porcentagem de Formados",
    "Porcentagem de Ingressantes",
    "Porcentagem Continuaram Vinculados",
    "Porcentagem Evadidos",
    "Porcentagem Evasao"
]


app.layout = html.Div(children=[
    html.H1(children='Dados sobre os alunos da Engenharia de Computação'),


    dcc.Dropdown(opcoes, value= 'Ano', id='x'),
    dcc.Dropdown(opcoes, value= 'Vinculados', id='y'),
    
    dcc.Graph(
        id='grafico-ecomp',
        figure=fig
    )
])


@callback(
    Output('grafico-ecomp', 'figure'),
    Input('x', 'value'),
    Input('y', 'value')
)
def update_output(value_x,value_y):

    fig = px.bar(df, x=value_x, y=value_y, title="Dados sobre os alunos da Engenharia de Computacao")
    return fig
    


if __name__ == '__main__':
    app.run(debug=True)
