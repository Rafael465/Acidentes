Acidentes de Trânsito no Brasil

Neste projeto foi realizada uma análise sobre os dados de acidentes de trânsito no Brasil. Os dados são de 2021 até 2024.

esse projeto foi desenvolvido através do jupyter notebook atraves do conda.

Pra rodar esse projeto deve baixar os arquivos em algum diretorio seu
Navegar ate a pasta Atividade final e iniciar a instancia com:
activate acidentes_env

e então rodar:
jupyter notebook

para rodar o streamlit basta rodar o seguinte comando com o ambiente ativo, dentro do diretorio App:
streamlit run app.py

## O que foi realizado

- Importação dos arquivos e a concatenação dos mesmos
- Limpeza de dados como valores nulos, duplicatas removidas e formatação
- Criação de colunas novas para análise como vitimas, ano, mes e novo periodo do dia
- Somatoria do numero de feridos leves e graves
- Número total de vitimas no periodo
- Histograma de relação entre quantidade de acidetes e o horário que ocorreram
- Boxplot de vitimas por fase do dia e vitimas por dia da semana
- Gráficos de barras com os 5 maiores causa de acidentes e tipos de acidentes
- Matriz de correlação entre os dados numéricos
- Mapa de Geolocalização com informações interativas
- Gráfico de disperção da correlação entre vitimas e condição climática
- Gráfico pizza com indice de acidentes com e sem mortes
- Streamlit com a tabela de dados na qual é possivel selecionar a tabela com base no ano.

Com base nos dados analisados, podemos ver que em relação ao horario dos acidentes existem dois picos, as 7 da manhã e as 6 da tarde. Esse indice pode ter relação com os horários que as pessão estão indo e voltando de seus trabalhos, pois costumeiramente são conhecidos como horário de pico onde há um volume maior de carro (e extresse) nas ruas. 

Outro dado interessante é que, ao analisar o boxplot, é possivel identificar um aglomeração maior de acidentes com mais vitimas aos sábados e aos domingos.

Ao avaliarmos os maiores causadores de acidentes, dois deles se destacam, que tem algo em comum entre si, a reação do condutor. E o tipo de acidente com maio incidencia é a colisão traseira.

Em um gráfico de pizza pode se observar que de todos os acidentes relatados no dataset, 7,2% deles possuem fatalidades.
