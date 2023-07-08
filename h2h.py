
import pandas as pd
import streamlit as st
from tabulate import tabulate




urls = [
    "https://www.football-data.co.uk/mmz4281/2223/D1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/D1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/D1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/D1.csv",
    "https://www.football-data.co.uk/mmz4281/2223/D2.csv",
    "https://www.football-data.co.uk/mmz4281/2122/D2.csv",
    "https://www.football-data.co.uk/mmz4281/2021/D2.csv",
    "https://www.football-data.co.uk/mmz4281/1920/D2.csv",
    "https://www.football-data.co.uk/new/ARG.csv",
    "https://www.football-data.co.uk/new/AUT.csv",
    "https://www.football-data.co.uk/mmz4281/2223/B1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/B1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/B1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/B1.csv",
    "https://www.football-data.co.uk/new/BRA.csv",
    "https://www.football-data.co.uk/new/CHN.csv",
    "https://www.football-data.co.uk/new/DNK.csv",
    "https://www.football-data.co.uk/mmz4281/2223/SC0.csv",
    "https://www.football-data.co.uk/mmz4281/2122/SC0.csv",
    "https://www.football-data.co.uk/mmz4281/2021/SC0.csv",
    "https://www.football-data.co.uk/mmz4281/1920/SC0.csv",
    "https://www.football-data.co.uk/mmz4281/2223/SC1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/SC1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/SC1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/SC1.csv",
    "https://www.football-data.co.uk/mmz4281/2223/SC2.csv",
    "https://www.football-data.co.uk/mmz4281/2122/SC2.csv",
    "https://www.football-data.co.uk/mmz4281/2021/SC2.csv",
    "https://www.football-data.co.uk/mmz4281/1920/SC2.csv",
    "https://www.football-data.co.uk/mmz4281/2223/SP1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/SP1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/SP1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/SP1.csv",
    "https://www.football-data.co.uk/mmz4281/2223/SP2.csv",
    "https://www.football-data.co.uk/mmz4281/2122/SP2.csv",
    "https://www.football-data.co.uk/mmz4281/2021/SP2.csv",
    "https://www.football-data.co.uk/mmz4281/1920/SP2.csv",
    "https://www.football-data.co.uk/new/FIN.csv",
    "https://www.football-data.co.uk/mmz4281/2223/F1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/F1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/F1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/F1.csv",
    "https://www.football-data.co.uk/mmz4281/2223/F2.csv",
    "https://www.football-data.co.uk/mmz4281/2122/F2.csv",
    "https://www.football-data.co.uk/mmz4281/2021/F2.csv",
    "https://www.football-data.co.uk/mmz4281/1920/F2.csv",
    "https://www.football-data.co.uk/mmz4281/2223/G1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/G1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/G1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/G1.csv",
    "https://www.football-data.co.uk/mmz4281/2223/N1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/N1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/N1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/N1.csv",
    "https://www.football-data.co.uk/mmz4281/2223/E0.csv",
    "https://www.football-data.co.uk/mmz4281/2122/E0.csv",
    "https://www.football-data.co.uk/mmz4281/2021/E0.csv",
    "https://www.football-data.co.uk/mmz4281/1920/E0.csv",
    "https://www.football-data.co.uk/mmz4281/2223/E1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/E1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/E1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/E1.csv",
    "https://www.football-data.co.uk/new/IRL.csv",
    "https://www.football-data.co.uk/mmz4281/2223/I1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/I1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/I1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/I1.csv",
    "https://www.football-data.co.uk/mmz4281/2223/I2.csv",
    "https://www.football-data.co.uk/mmz4281/2122/I2.csv",
    "https://www.football-data.co.uk/mmz4281/2021/I2.csv",
    "https://www.football-data.co.uk/mmz4281/1920/I2.csv",
    "https://www.football-data.co.uk/new/JPN.csv",
    "https://www.football-data.co.uk/new/MEX.csv",
    "https://www.football-data.co.uk/new/NOR.csv",
    "https://www.football-data.co.uk/new/POL.csv",
    "https://www.football-data.co.uk/mmz4281/2223/P1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/P1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/P1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/P1.csv",
    "https://www.football-data.co.uk/new/ROU.csv",
    "https://www.football-data.co.uk/new/RUS.csv",
    "https://www.football-data.co.uk/new/SWE.csv",
    "https://www.football-data.co.uk/new/SWZ.csv",
    "https://www.football-data.co.uk/mmz4281/2223/T1.csv",
    "https://www.football-data.co.uk/mmz4281/2122/T1.csv",
    "https://www.football-data.co.uk/mmz4281/2021/T1.csv",
    "https://www.football-data.co.uk/mmz4281/1920/T1.csv",
    "https://www.football-data.co.uk/new/USA.csv"


]
# Criar uma lista para armazenar os dataframes
dfs = []

# Loop pelas URLs
for url in urls:
    # Baixar o arquivo CSV e ler como dataframe
    df = pd.read_csv(url)

    # Renomear as colunas
    df = df.rename(columns={
        "Home": "HomeTeam",
        "Away": "AwayTeam",
        "HG": "FTHG",
        "AG": "FTAG",
        "Res": "FTR",
        "PH": "PSH",
        "PD": "PSD",
        "PA": "PSA",
        "Country": "Div"
    })

    # Converter o conteúdo da coluna "Country"
    df["Div"] = df["Div"].replace("Argentina", "ARG")
    df["Div"] = df["Div"].replace("Austria", "AUT")
    df["Div"] = df["Div"].replace("Brazil", "BRA")
    df["Div"] = df["Div"].replace("China", "CHN")
    df["Div"] = df["Div"].replace("Denmark", "DNK")
    df["Div"] = df["Div"].replace("Finland", "FIN")
    df["Div"] = df["Div"].replace("Ireland", "IRL")
    df["Div"] = df["Div"].replace("Japan", "JPN")
    df["Div"] = df["Div"].replace("Mexico", "MEX")
    df["Div"] = df["Div"].replace("Norway", "NOR")
    df["Div"] = df["Div"].replace("Poland", "POL")
    df["Div"] = df["Div"].replace("Romania", "ROU")
    df["Div"] = df["Div"].replace("Russia", "RUS")
    df["Div"] = df["Div"].replace("Sweden", "SWE")
    df["Div"] = df["Div"].replace("Switzerland", "SWZ")
    df["Div"] = df["Div"].replace("USA", "USA")

    # Adicionar o dataframe à lista
    dfs.append(df)

# Concatenar os dataframes da lista em uma única tabela
merged_table = pd.concat(dfs)

# Excluir as colunas mencionadas
merged_table = merged_table.drop(columns=[
    "HTHG", "HTAG", "HTR", "HS", "AS", "HST", "AST", "HF", "AF", "HC",
    "AC", "HY", "AY", "HR", "AR", "B365H", "B365D", "B365A", "BWH", "BWD",
    "BWA", "IWH", "IWD", "IWA", "WHH", "WHD", "WHA",
    "VCH", "VCD", "VCA", "MaxH", "MaxD", "MaxA", "AvgH", "AvgD", "AvgA",
    "B365>2.5", "B365<2.5", "P>2.5", "P<2.5", "Max>2.5", "Max<2.5", "Avg>2.5",
    "Avg<2.5", "AHh", "B365AHH", "B365AHA", "PAHH", "PAHA", "MaxAHH", "MaxAHA",
    "AvgAHH", "AvgAHA", "B365CH", "B365CD", "B365CA", "BWCH", "BWCD", "BWCA",
    "IWCH", "IWCD", "IWCA", "PSCH", "PSCD", "PSCA", "WHCH", "WHCD", "WHCA",
    "VCCH", "VCCD", "VCCA", "MaxCH", "MaxCD", "MaxCA", "AvgCH", "AvgCD", "AvgCA",
    "B365C>2.5", "B365C<2.5", "PC>2.5", "PC<2.5", "MaxC>2.5", "MaxC<2.5", "AvgC>2.5",
    "AvgC<2.5", "AHCh", "B365CAHH", "B365CAHA", "PCAHH", "PCAHA", "MaxCAHH", "MaxCAHA",
    "AvgCAHH", "AvgCAHA", "League", "Season"
])
# Renaming the values in the "Div" column (as shown in the previous code)
merged_table["Div"] = merged_table["Div"].replace({
    # Renaming values
})

# Renomear o conteúdo da coluna "Div"
merged_table["Div"] = merged_table["Div"].replace({
    "ARG": "Argentina Liga Profesional",
    "AUT": "Austria Bundesliga",
    "BRA": "Brasil Serie A",
    "CHN": "China Super League",
    "DNK": "Dinamarca Super League",
    "D1":  "Alemanha Bundesliga",
    "D2":  "Alemanha Bundesliga 2",
    "CHN": "China Super League",
    "B1":  "Belgica Jupiler League",
    "SC2":  "Escócia Championship",
    "SC1": "Escócia League One",
    "SC0": "Escócia Premier League",
    "SP1": "Espanha La Liga",
    "SP2": "Espanha La Liga 2",
    "FIN": "Finlândia Veikkausliiga",
    "FINLAND": "Finlândia Veikkausliiga",
    "F1":  "França Ligue 1",
    "F2":  "França Ligue 2",
    "G1":  "Grécia Super Liga",
    "N1":  "Holanda Eredivisie",
    "E1":  "Inglaterra Championship",
    "E0":  "Inglaterra Premier League",
    "IRL":  "Irlanda Premier Division",
    "IRELAND":  "Irlanda Premier Division",
    "I1":  "Itália Serie A",
    "I2":  "Itália Serie B",
    "JPN":  "Japão J League",
    "MEX":  "México Liga MX",
    "NOR":  "Noruega Eliteserien",
    "POL":  "Polônia Ekstraklasa",
    "P1":  "Portugal Liga I",
    "T1":  "Turquia TFF 1. Lig",
    "ROU":  "Romênia Liga 1",
    "RUS":  "Russia Premier League",
    "SWE":  "Suêcia Allsvenskan",
    "SWEDEN":  "Suêcia Allsvenskan",
    "SWZ":  "Suiça Super League",
    "USA":  "USA MLS",


})

# Configurações do Streamlit
st.title("Análise h2h")
st.sidebar.title("Filtros")

# Solicitar ao usuário as datas inicial e final
data_inicial = st.sidebar.text_input("Informe a data inicial (formato: DD/MM/AAAA):")
data_final = st.sidebar.text_input("Informe a data final (formato: DD/MM/AAAA):")

# Converter as datas para formato de data
merged_table["Date"] = pd.to_datetime(merged_table["Date"], format="%d/%m/%Y")
data_inicial = pd.to_datetime(data_inicial, format="%d/%m/%Y")
data_final = pd.to_datetime(data_final, format="%d/%m/%Y")

# Filtrar o dataframe pelo intervalo de data
filtered_table = merged_table[(merged_table["Date"] >= data_inicial) & (merged_table["Date"] <= data_final)]

# Renomear as colunas de acordo com os nomes corretos
filtered_table = filtered_table.rename(columns={
    "Home": "HomeTeam",
    "Away": "AwayTeam",
    "HG": "FTHG",
    "AG": "FTAG",
    "Res": "FTR",
    "PH": "PSH",
    "PD": "PSD",
    "PA": "PSA",
    "Country": "Div"
})

# Obter a lista de valores únicos para HomeTeam e AwayTeam
home_teams = filtered_table["HomeTeam"].unique()
away_teams = filtered_table["AwayTeam"].unique()

# Opções de filtro para o Home Team e Away Team
home_team = st.sidebar.selectbox("Escolha o time da casa:", home_teams)
away_team = st.sidebar.selectbox("Escolha o time de fora:", away_teams)

# Filtrar o dataframe pelo Home Team e Away Team
filtered_table = filtered_table[
    (filtered_table["HomeTeam"] == home_team) &
    (filtered_table["AwayTeam"] == away_team)
]

# Solicitar ao usuário a opção de escolher casa ou visitante
opcao = st.sidebar.radio("Escolha a opção:", ("Casa", "Visitante"))

if opcao == "Casa":
    # Solicitar ao usuário os valores mínimos e máximos das odds para a opção casa
    odd_min = st.sidebar.number_input("Odd Inicial:")
    odd_max = st.sidebar.number_input("Odd Final:")

    # Filtrar o dataframe pelas faixas de odds para a opção casa
    filtered_table = filtered_table[(filtered_table["PSH"] >= odd_min) & (filtered_table["PSH"] <= odd_max)]
elif opcao == "Visitante":
    # Solicitar ao usuário os valores mínimos e máximos das odds para a opção visitante
    odd_min = st.sidebar.number_input("Odd Inicial:")
    odd_max = st.sidebar.number_input("Odd Final:")

    # Filtrar o dataframe pelas faixas de odds para a opção visitante
    filtered_table = filtered_table[(filtered_table["PSA"] >= odd_min) & (filtered_table["PSA"] <= odd_max)]

# Calculate the total number of matches
total_matches = len(filtered_table)

# Initialize the win, draw, and loss variables
wins = len(filtered_table[filtered_table["FTR"] == "H"])
draws = len(filtered_table[filtered_table["FTR"] == "D"])
losses = len(filtered_table[filtered_table["FTR"] == "A"])

# Create a head-to-head table
head_to_head_table = pd.DataFrame({
    "": ["Win", "Draw", "Loss"],
    "Count": [wins, draws, losses]
})

# Display the head-to-head table using tabulate
head_to_head_table_formatted = tabulate(head_to_head_table, headers="keys", tablefmt="fancy_grid")
st.write("**Head-to-Head Statistics**")
st.code(head_to_head_table_formatted)

# Filter the dataframe by Home Team and Away Team
filtered_matches = filtered_table[
    (filtered_table["HomeTeam"] == home_team) &
    (filtered_table["AwayTeam"] == away_team)
]

# Selecionar as colunas desejadas
selected_columns = ["Div", "Date", "Time", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "PSH", "PSD", "PSA"]

# Filtrar o dataframe pelas colunas selecionadas
filtered_matches = filtered_matches[selected_columns]

# Arredondar as colunas relevantes para duas casas decimais
filtered_matches["FTHG"] = filtered_matches["FTHG"].round(2)
filtered_matches["FTAG"] = filtered_matches["FTAG"].round(2)
filtered_matches["PSH"] = filtered_matches["PSH"].round(2)
filtered_matches["PSD"] = filtered_matches["PSD"].round(2)
filtered_matches["PSA"] = filtered_matches["PSA"].round(2)

# Display the filtered matches using tabulate
filtered_matches_formatted = tabulate(filtered_matches, headers="keys", tablefmt="fancy_grid")
st.write("**Filtered Matches**")
st.code(filtered_matches_formatted)

# Filtrar o dataframe pelo Home Team e Away Team
filtered_matches = filtered_table[
    (filtered_table["HomeTeam"] == home_team) &
    (filtered_table["AwayTeam"] == away_team)
]

# Calcular a média de gols feitos e tomados
mean_goals_scored = filtered_matches["FTHG"].mean()
mean_goals_conceded = filtered_matches["FTAG"].mean()

# Calcular o coeficiente de variação
cv_goals_scored = filtered_matches["FTHG"].std() / mean_goals_scored * 100
cv_goals_conceded = filtered_matches["FTAG"].std() / mean_goals_conceded * 100

# Arredondar os valores para duas casas decimais
mean_goals_scored = round(mean_goals_scored, 2)
mean_goals_conceded = round(mean_goals_conceded, 2)
cv_goals_scored = round(cv_goals_scored, 2)
cv_goals_conceded = round(cv_goals_conceded, 2)

# Criar uma lista de listas com os dados da tabela
statistics_data = [
    ["Média de Gols Marcados", mean_goals_scored],
    ["Média de Gols Sofridos", mean_goals_conceded],
    ["Coeficiente de Variação de Gols Marcados", cv_goals_scored],
    ["Coeficiente de Variação de Gols Sofridos", cv_goals_conceded]
]

# Exibir a tabela formatada utilizando o método tabulate
statistics_table_formatted = tabulate(statistics_data, headers=["Estatística", "Valor"], tablefmt="fancy_grid")
st.write("**Statistics**")
st.code(statistics_table_formatted)
