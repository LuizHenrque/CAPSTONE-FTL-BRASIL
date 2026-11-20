# Impactos do El Nino no Brasil

Projeto final para o Future Tech Leaders Brasil 2026, Space Tech Bootcamp.

## Grupo

- Luiz Henrique Araújo de Brito 
- Mariana Lebrão Murauskas
- Lucas Sousa Costa
- Laissa P.
- Gabrielle Vasconcelos de Mendonça Penha
- Laíne Reis de Moura
- Flávio Arthur Campos Figueira
- Douglas Rodrigues da Silva
- Danielle Mota Torres Nogueira
- Camila Yukari Kobayashi
- Ayronn Medina Zago Assen
- Alice Gomes Pereira

## Até agora mapeamos os seguintes impactos:

Escreva o impacto na sua região nesse lista! 

- Tornados na zona oeste de Santa Catarina. Chapecó.
- Seca extensiva no agreste de Pernambuco. Local encontrado para retratar a seca foi Panelas-PB
- Queimadas na zona de Manaus e no Pará.

## Coisas para fazer:

- Fazer uma foto de para a capa de entrada do storytelling. Alguma foto para a capa que apanhe essa ideia de El Nino e eventos extremos. Se usar a foto de alguem não esqueça de citar.  
- Elencar mais potenciais danos e eventos extremos que podem estar ligados ao el nino. (escrever na lista acima)
- Buscar fotos e reportagens dos eventos e adicionar na pasta `assets/fotos_reportagens`
- Breve estudo sobre as queimadas no Pará
- **Modificar o texto do storytelling. Até agora não há texto nenhum.**
- Adicionar os logos do FTL. 
- Sinta-se a vontade para fazer qualquer estudo relaciona a um evento extremo. Basta realiza-lo em um novo notebook na pasta `studies`
- Não tenha medo de contribuir e mexer aqui. Se você não souber como ajeitar o arquivo do storytelling, então só escreva o texto que você deseja num .md e depois complemente o README citando onde voce gostaria que o texto fosse alocado, alguém irá modificar e ajeitar para você.


## Como contribuir

De um fork nesse repositorio e clone em seu computador. Comece com um git checkout para trabalhar na sua branch. Deixe a main livre.

```bash
git checkout -b seu-nome
```

Depois, instalem os pacotes de uv para rodar o python,

aqui voce inicia o projeto
```bash
uv init 
```

aqui voce instala as bibliotecas
```bash
uv sync 
```

Depois, instalem as bibliotecas de javascript

```bash
npm install
```

Isso vai ler o arquivo `package.json`e instalar todas as dependências. Depois de instalado, você consegue ver a renderização do projeto direto no terminal de comando, rodando:

Aqui voce consegue visualizar como o storytelling esta ficando. 
```bash
npm run dev
```
Isso abre um local host na porta 5173. Só abrir esse link em qualquer navegador e você é capaz de ver o storytelling produzido. http://localhost:5173/

Perceba que o storytelling inteiro é escrito dentro de `elnino.md`! Todos os outros arquivos python são de estudos auxiliares para produzir as imagens que devam estar no storytelling. 

### Vocês podem trabalhar em 5 frentes aqui:

- Pesquisa: realizar a pesquisa dentro do `studies/`. Criem um notebook e tentem de alguma forma fazer o link entre o evento extremo observado e o El Nino. Por exemplo, se você quer demonstrar a seca acontecendo na Paraiba, então você poderia fazer um estudo climático e analisar o quanto essa seca se difere das outras numa série temporal. Ou demonstrar com algum índice e imagem de satélite que a região possui uma baixa umidade do solo, por exemplo. 
- Ajeitando o texto: Para ajeitar o texto basta modificar o arquivo `elnino.md`. Percebam que cada as # dao origem aos titulos e web components e o texto fica em paragrafo solto. 
- Ajeitando elementos: Sinta-se a vontade para ajeitar os elementos, adicionar images ou coisas do tipo. A documentação necessária voce encontra no próximo paragrafo.
- Buscando imagens para complementar os impactos. Uma vez com essas imagens voce pode inserir direto no storytelling ou voce pode adicionar na pasta `assets/fotos_reportagens` e deixar escrito abaixo para alguém adicionar para você. 
- Citando um possível impacto do evento extremo que você observou. Basta adicionar ao nosso README.md

- Todas as imagens que voce vê no storytelling estao armazenadas dentro da pasta `assets/`

### Documentação

- [Documentos do web componentes para storytelling](https://eox-a.github.io/EOxElements/?path=/story/elements-eox-storytelling--primary)
- [Outros Elementos](https://explorer.eopf.copernicus.eu/software-services/)
- [Video Aula de como começar com storytelling](https://github.com/emanuel-gf/FTL-Storytelling-I)
- [lindo exemplo de storytelilng](https://explorer.eopf.copernicus.eu/story/?id=ndci)
- A aula sobre como modificar esse storytelling está no grupo do Teams.

## HELP

Aqui vocês escrevam o que fizeram e qual a ajuda gostaria que alguem fizesse.
Ex:
- Busquei 2 imagens para complementar as queimadas da Amazônia. As imagens estão dentro da pasta `assets/fotos_reportagens` e possuem o nome da `nome_da_imagem.png` e `nome_da_imagem2.png`. Ficaria grato se alguém adicionasse-as no arquivo do storytelling pois não entendo muito bem como adicionar. Nome_De_Quem_Escreveu_Isso (FULANO. )