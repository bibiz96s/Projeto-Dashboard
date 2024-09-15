from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_csv("EvasãoSérieHistórica2024.csv", encoding='latin1',delimiter=';')

opcoes = df.columns.tolist()


app.layout = html.Div(children=[
    html.H1(children='Dados sobre os alunos da Engenharia de Computação'),


    dcc.Dropdown(opcoes, value= ['Ingressantes'], id='color',multi=True),
    dcc.Dropdown(opcoes, value= 'Vinculados', id='y'),
    
    dcc.Graph(
        id='grafico-barras'
    ),
    
    dcc.Graph(
        id='grafico-linhas'
    )

])


@callback(
    Output('grafico-barras', 'figure'),
    Input('color', 'value'),
    Input('y', 'value')
)
def update_bar(value_color,value_y):

    
    fig_bar = px.bar()

    for coluna in value_color:
        
        fig_bar.add_trace(px.bar(df, x="Ano", y=value_y,color=coluna, title=f"Dados sobre {coluna} e {value_y}").data[0],)

    return fig_bar

@callback(
    Output('grafico-linhas', 'figure'),
    Input('color', 'value'),
    Input('y', 'value')
)
def update_lines(value_color,value_y):

    
    fig_lines = px.bar()

    for coluna in value_color:
        
        fig_lines.add_trace(px.line(df, x="Ano", y=value_y,color=coluna, title=f"Dados sobre {coluna} e {value_y}").data[0],)

    return fig_lines


if __name__ == '__main__':
    app.run(debug=True)
