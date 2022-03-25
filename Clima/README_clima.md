# Sprint 3 - TMG

## Descrição
- O escopo deste projeto compreende a busca por bases de dados sobre clima e solo, o tratamento desses dados para que, posteriormente, possa ser util para a empresa realizar consultas de forma mais rápida e cruzar os recultados com a bases de dados da inteligência de negócios da TMG. Também foram feitas aplicações de algumas premissas geoestatísticas, testes de modelos de inteporlação como Krigagem e IDW e a execução dos mapas.
---

## Processamento e exploração dos dados sobre Clima 
### Organização dos diretórios

    ├── src/ (diretório para armazenar todos os arquivos de desenvolvimento e as pastas contendo os dados necessários para execução dos códigos);
    |   └── data/ (diretório de dados contendo pastas com os dados utilizados);
    |       └── dados_hist_clima_concatenados/ (diretório com todos os dados concatenados de todas as cidades com informações disponíveis no estado do Paraná (de 2006 até 2021) e também os dados tratados que serão utilizados em análises e nos scripts R);
    |   └── Arquivos_R/ (diretório contendo scripts R e modelos que foram exportados após sua execução)
    └──
---

### Arquivos Jupyter Notebooks desenvolvidos
- `01-Exploracao-inicial-Clima.ipynb`
    - Arquivo contendo exploração inicial e tratamento inicial sobre os dados de clima que foram retirados do site do INMET;
- `02-Unindo-Cidades-PR.ipynb`
    - Arquivo criado para filtrar os dados por cidade e período produtivo e criar um novo .csv contendo todos os dados das cidades concatenados e com suas respectivas informações de longitude e latitude;
- `03-Variogramas.ipynb`
    - Arquivo para plotar análises de distribuição de frequências e variogramas para verificar a qualidade dos dados;
- `04-UTM.ipynb`
    - Arquivo para converter longitude e latitude em novas colunas x e y contendo informações de UTM para que possam ser utilizadas no script R de krigagem;
- `05-Outra-Abordagem.ipynb`
    - Mesmo tipo de análise do item 02, porém contendo apenas médias gerais para cada cidade com apenas 25 linhas no final, possuindo 25 pontos de geolocalização únicos no intuito de testar a krigagem com melhor eficiência.
- `utils.py`
    - Script com as funções auxiliares caso necessário;
---

### Bibliotecas Utilziadas no Python
    - Numpy;
    - Pandas;
    - Seaborn;
    - Matplotlib;
    - Skgstat;
    - Geopy;
    - Scipy;
    - Pyproj.
### Bibliotecas Utilziadas no R
    - geobr;
    - ggplot2;
    - sf;
    - stars;
    - rnaturalearth;
    - rgeos;
    - gstat;
    - fields;
    - ggspatial;
    - rgdal;
---

## Processamento e exploração dos dados sobre Solo
### Organização dos diretórios


### Arquivos Jupyter Notebooks desenvolvidos


---
### Equipe
- [Igor Nieto](https://www.linkedin.com/in/igor-iraburo-nieto-6a5157119/)
- [Laryssa Stephanie](https://www.linkedin.com/in/laryssastephanie/)