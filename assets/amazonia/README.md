# Mapa da Amazônia

[limite_bioma_amazonia_ibge.geojson](./limite_bioma_amazonia_ibge.geojson) contém o limite do **bioma Amazônia em território brasileiro**, da base de biomas do IBGE (2019), disponibilizada pelo Ibama. O contorno foi obtido em 27/11/2026 em GeoJSON, com coordenadas geográficas WGS 84 (EPSG:4326).

- [Metadados da camada no Ibama](https://pamgia.ibama.gov.br/server/rest/services/01_Publicacoes_Bases/biomas_ibge_250k_2019/FeatureServer/2).
- [Consulta usada para obter o arquivo](https://pamgia.ibama.gov.br/server/rest/services/01_Publicacoes_Bases/biomas_ibge_250k_2019/FeatureServer/2/query?where=bioma%3D%27Amaz%C3%B4nia%27&outFields=bioma,cd_bioma&outSR=4326&maxAllowableOffset=0.01&geometryPrecision=4&f=geojson).

O serviço generalizou a geometria com tolerância de 0,01 grau e quatro casas decimais para manter o arquivo leve na visualização regional. O contorno representa o bioma, não a Amazônia Legal nem a bacia hidrográfica.

O [storytelling](../../elnino.md) usa essa camada em três etapas: visão geral, Lábrea (AM) e Santarém (PA). Os marcadores são referências aproximadas das sedes municipais, nas coordenadas longitude/latitude `[-64.8, -7.26]` e `[-54.71, -2.44]`; não representam focos de calor ou a localização exata da fotografia. O mapa de fundo é do OpenStreetMap.
