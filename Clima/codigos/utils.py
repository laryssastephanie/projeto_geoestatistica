import pandas as pd 
from pathlib import Path
from utils import *
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import math
import datetime
import base64

file_path = "data/dados_TMG/BD_BR_DP.xlsx"
new_file_path = "data/dados_TMG/base_dados.csv"
treated_file_path = "data/dados_TMG/base_dados_tratado.csv"
    
def load_data():
    """ 
    Realiza o carregamento de dados da planilha.
    Também transforma em arquivo .csv, que agiliza a leitura. 
    Caso o arquivo .csv já exista, apenas irá carregar os dados.
    """
    try:
        if(not Path(new_file_path).is_file()):
            data = pd.read_excel(file_path, sheet_name='BD', index_col=False)
            data.to_csv("data/dados_TMG/base_dados.csv", index=False, sep=';')
            print('BD carregado e arquivo .csv criado com sucesso!')
        else:
            print('BD carregado com sucesso!')
        df = pd.read_csv(new_file_path)
        return df
    except Exception as e:
        print(e)

def load_treated_data():
    """ 
    Realiza o carregamento de dados tratados.
    Contém algumas modificações em relação à planilha original
    """
    try:
        df = pd.read_csv(treated_file_path)
        print('Dados tratados carregados com sucesso!')
        return df
    except Exception as e:
        print(e)


def dados_faltantes(df):
    """
    Plotagem de um heatmap mostrando a porcentagem de dados faltantes das colunas do df.
    """
    colunas_dados_faltantes = df.columns[df.isna().any()]
    porcentagem_dados_faltantes = df[colunas_dados_faltantes].isna().sum().to_frame() / len(df) * 100
    plt.figure(figsize=(10,15))
    ax = sns.heatmap(porcentagem_dados_faltantes, annot=True, fmt='.2f', cmap='vlag')
    plt.title('Valores Faltantes (%)', fontweight='bold')
    plt.show()

def gerar_dados_clima (cidade_selecionada, id_em_selecionado):
    """
    Função responsável por carregar todos os dados dos anos de 2006 até 2021 disponíveis, de acordo com a 
    regiao, estado, cidade e id da estação meteorológica selecionada pelo usuário. Um arquivo .csv
    será gerado automaticamente e salvo na pasta conforme código abaixo. Aqui também é feito um tratamento inicial
    para renomear as colunas que mudaram de nome do ano de 2019 em diante e também para remover uma coluna irrelevante.
    Também é inserido o nome da cidade em questão em uma coluna para que possa tirar a latitude e longitude, que será 
    utilizada posteriormente.
    """

    df1 = pd.read_csv(f'data/2006/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2006_A_31-12-2006.CSV', encoding="latin-1", sep=';', skiprows=8)
    df2 = pd.read_csv(f'data/2007/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2007_A_31-12-2007.CSV', encoding="latin-1", sep=';', skiprows=8)
    df3 = pd.read_csv(f'data/2008/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2008_A_31-12-2008.CSV', encoding="latin-1", sep=';', skiprows=8)
    df4 = pd.read_csv(f'data/2009/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2009_A_31-12-2009.CSV', encoding="latin-1", sep=';', skiprows=8)
    df5 = pd.read_csv(f'data/2010/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2010_A_31-12-2010.CSV', encoding="latin-1", sep=';', skiprows=8)
    df6 = pd.read_csv(f'data/2011/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2011_A_31-12-2011.CSV', encoding="latin-1", sep=';', skiprows=8)
    df7 = pd.read_csv(f'data/2012/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2012_A_31-12-2012.CSV', encoding="latin-1", sep=';', skiprows=8)
    df8 = pd.read_csv(f'data/2013/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2013_A_31-12-2013.CSV', encoding="latin-1", sep=';', skiprows=8)
    df9 = pd.read_csv(f'data/2014/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2014_A_31-12-2014.CSV', encoding="latin-1", sep=';', skiprows=8)
    df10 = pd.read_csv(f'data/2015/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2015_A_31-12-2015.CSV', encoding="latin-1", sep=';', skiprows=8)
    df11 = pd.read_csv(f'data/2016/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-06-2016_A_31-12-2016.CSV', encoding="latin-1", sep=';', skiprows=8)
    df12 = pd.read_csv(f'data/2017/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2017_A_31-12-2017.CSV', encoding="latin-1", sep=';', skiprows=8)
    df13 = pd.read_csv(f'data/2018/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2018_A_31-12-2018.CSV', encoding="latin-1", sep=';', skiprows=8)
    df14 = pd.read_csv(f'data/2019/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2019_A_31-12-2019.CSV', encoding="latin-1", sep=';', skiprows=8)
    df15 = pd.read_csv(f'data/2020/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2020_A_31-12-2020.CSV', encoding="latin-1", sep=';', skiprows=8)
    df16 = pd.read_csv(f'data/2021/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2021_A_30-11-2021.CSV', encoding="latin-1", sep=';', skiprows=8)

    df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,
                                df14.rename(columns={'Data':'DATA (YYYY-MM-DD)', 'Hora UTC':'HORA (UTC)', 'RADIACAO GLOBAL (Kj/m²)':'RADIACAO GLOBAL (KJ/m²)'}), 
                                df15.rename(columns={'Data':'DATA (YYYY-MM-DD)', 'Hora UTC':'HORA (UTC)', 'RADIACAO GLOBAL (Kj/m²)':'RADIACAO GLOBAL (KJ/m²)'}), 
                                df16.rename(columns={'Data':'DATA (YYYY-MM-DD)', 'Hora UTC':'HORA (UTC)', 'RADIACAO GLOBAL (Kj/m²)':'RADIACAO GLOBAL (KJ/m²)'})])
    df.drop(['Unnamed: 19'], axis=1, inplace=True)
    df['DATA (YYYY-MM-DD)'] = pd.to_datetime(df['DATA (YYYY-MM-DD)'])
    df.set_index('DATA (YYYY-MM-DD)', inplace=True)
    df['CIDADE'] = f'{cidade_selecionada}'

    lat = pd.Series(df['CIDADE'].unique().tolist(), index=df['CIDADE'].unique().tolist()).apply(geocode).apply(lambda location: location.latitude)
    long = pd.Series(df['CIDADE'].unique().tolist(), index=df['CIDADE'].unique().tolist()).apply(geocode).apply(lambda location: location.longitude)
    lat.name = 'LATITUDE'
    long.name = 'LONGITUDE'
    df_lat = df.merge(lat, how='left', left_on='CIDADE', right_index=True)
    df_lat_long = df_lat.merge(long, how='left', left_on='CIDADE', right_index=True)

    df_lat_long.to_csv(f'data/dados_hist_clima_concatenados/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2006_A_30-11-2021.CSV')

    return df_lat_long

def ler_dados_concatenados(cidade_selecionada, id_em_selecionado):
    """
    Função para realizar a leitura dos dados concatenados gerados na função acima, de acordo com os inputs feitos pelo usuário.
    Também é realizado um tratamento para transformar a coluna de data para seu devido formato. A coluna de horário é removida.
    Todos os dados são transformados em tipo float para poder trabalhar com estatísticas posteriormente.
    Os NA's foram substituídos pela média das colunas, o que não alterou o resultado final (na média) do dataframe.
    """
    df_tratado = pd.read_csv(f'data/dados_hist_clima_concatenados/INMET_S_PR_{id_em_selecionado}_{cidade_selecionada}_01-01-2006_A_30-11-2021.CSV', index_col=False, decimal=',')
    df_tratado['DATA (YYYY-MM-DD)'] = pd.to_datetime(df_tratado['DATA (YYYY-MM-DD)'])
    df_tratado.set_index('DATA (YYYY-MM-DD)', inplace=True)
    df_tratado.drop(['HORA (UTC)'], axis=1, inplace=True)
    df_tratado.iloc[:, 11:15] = df_tratado.iloc[:, 11:15].astype(float) # Os dados precisam ser do tipo float para poder trabalhar com estatísticas
    df_tratado.iloc[:, :17] = df_tratado[df_tratado.iloc[:, :17] > -5] # Pegando apenas medições de números acima de -5 (A temperatura poderia chegar a ser negativa, por isso o limite)
    df_tratado = df_tratado.iloc[:, :17].fillna(df_tratado.iloc[:, :17].mean())
    return df_tratado

def historico_por_periodo(df, periodo):
    """
    Gera um dataframe agrupando de acordo com o período que o usuário escolher no streamlit.
    Todas as colunas serão agrupadas com as suas respectivas médias, com exceção da precipitação,
    que será feito a soma dos milímetros.
    """
    df_periodo = df.resample(f'{periodo}').mean().round(2)
    # Para dados de chuva, utiliza-se a soma diária dos mm de precipitação, não a média
    df_precip = df.resample(f'{periodo}').sum()
    df_periodo['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'] = df_precip['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']
    df_periodo = df_periodo[df_periodo['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'] >= 0] # Utilizando os dados apenas maiores ou iguais a 0
    return df_periodo

def plotar_grafico(df, colunas_selecionadas, k):
    """
    Plotagem de gráficos de linhas de acordo com o dataframe do período selecionado.
    Apenas será plotado as colunas selecionadas pelo usuário.
    As médias móveis também serão plotadas nos gráficos de acordo com o 'k' (número de medições) escolhido
    """
    # cols = df.columns.tolist()

    fig = go.Figure()
    for c in colunas_selecionadas:
        fig.add_trace(go.Scatter(x=df.index, y=df[c], mode='lines+markers', name=f'{c}'))
        fig.add_trace(go.Scatter(x=df.index, y=df[c].rolling(k).mean(), name=f'MÉDIA MÓVEL DA {c} ({k} medições)'))
    fig.update_layout(title='Variáveis meteorológicas',
                    xaxis_title='Data',
                    title_x=0.3,
                    title_y=0.9,
                    xaxis_tickformat = '%B<br>%Y',
                    autosize=True,
                    height=600)
    return fig

def plotar_histograma(df, colunas_selecionadas, g):
    """
    Plotagem de hitograma de acordo com o dataframe do período selecionado.
    Apenas será plotado as colunas selecionadas pelo usuário.
    As médias móveis também serão plotadas nos gráficos de acordo com o 'g' (Intervalo (gap) das medidas) escolhido.
    """
    fig = go.Figure()
    for c in colunas_selecionadas:
        fig.add_trace(go.Histogram(x=df[c], name=f'{c}',
                xbins=dict(size=g),
                opacity=0.75
            ))
        fig.update_layout(
            title_text=f'Histograma das Variváveis meteorológicas de {df.index[0]} até {df.index[-1]}',
            xaxis_title_text='Valor',
            yaxis_title_text='Quantidade',
            bargap=0.2,
            bargroupgap=0.1,
            title_x=0.25,
            title_y=0.9,
            autosize=True,
            height=600
        )
    return fig
    
def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False, sep=';')

        # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

