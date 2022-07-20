# brazillian-presidential-elections

1 - OBJETIVO DO PROJETO 

 

Neste projeto vou usar dados reais coletados de um site de alta relevância, que é o twitter, onde pessoas famosas e com alta exposição fazem seus posts e mostrar suas opiniões.  

O período de eleições é bastante turbulento no Brasil, algumas pesquisas eleitorais não condizem com a realidade e há muitos boatos, que levam a uma falsa crença de um candidato ou outro. Um grande problema é saber realmente como o público avalia os candidatos. 

Essa avaliação é bastante útil para as equipes políticas, investidores e também para o público em geral, que pode ter uma ideia bem clara da opinião real da população.  

No ano de 2022 temos 2 candidatos bem polêmicos para a presidência da república no Brasil: Jair Bolsonaro e Luiz Inácio Lula da Silva. 

O principal objetivo desse projeto é fazer uma avaliação dos comentários do público para os 2 candidatos em suas páginas no twitter, classificando-as em positivas ou negativas para cada candidato. 

 
 
 

2 - SOLUÇÃO PROPOSTA 

 

Para realizar esse projeto foi construída uma solução completa de ciência de dados, que envolve armazenamento, gestão e automatização de fluxos de dados utilizando tecnologias como MySQL, AWS, API do twitter. A solução envolve também o processamento de dados com API de tradução Google Translator, TEXTBLOB, Pandas, Seaborn dentre outras tecnologias 

Primeiramente os dados são coletados via API do twitter, traduzidos para o inglês e armazenados no serviço RDS da AWS. Todo esse fluxo é repetido a cada 10 minutos por um trigger criado na própria AWS, que aciona a função Lambda que faz todo esse trabalho.  

Para usar a biblioteca TextBlob de avaliação de sentimentos preciso dos textos em inglês, então para resolver esse problema foi usado o Google translator. Mas, ao executar o tradutor para uma quantidade grande de informações o tempo era extremamente alto, sendo inviável essa abordagem. 

Para solucionar essa questão e também obter sempre tweets espaçados para ter uma maior variedade de opiniões, utilizei um trigger na AWS que aciona a função lambda responsável por esse fluxo de dados, que é executada a cada 10 minutos 

Resumindo: A cada 10 minutos a função Lambda coleta 50 tweets nas páginas dos candidatos, faz a tradução e os armazena no banco de dados MySQL na AWS. 

 

Depois dos dados estarem disponíveis, o próximo passo é fazer a limpeza desses dados, retirando tweets repetidos, pontuação, caracteres especiais.  

O pré-processamento vem em seguida, fazendo stemming e removendo stopwords, que deixará nossos dados prontos para a análise de sentimentos em si. 

Aplicando a biblioteca textblolb temos um resultado numérico que corresponde a polaridade de cada frase. Se a polaridade for menor que 0, tem um sentimento negativo, maior que 0 um sentimento positivo, e igual a 0 um sentimento neutro. 

No nosso caso retirei as avaliações neutras pois há muitas notícias publicadas na página desses candidatos, o que mudaria bastante a proporção das opiniões do público. 

Categorizando as classes de avaliação de sentimentos temos 2 distintas: positivo e negativo. Agora basta plotar essas 2 classes em gráficos utilizando o Seaborn para visualizar os resultados. 

 
 
 

3 - RESULTADOS 

Analisando os resultados podemos ver que os 2 candidatos têm uma opinião positiva maior do público, mas que o candidato Luiz Inácio Lula da Silva tem uma maior quantidade de opinião pública positiva. 

Como existem muitas controversas entre esses 2 candidatos pudemos ver como realmente o povo se expressa em relação a eles. Tirando a ideia de que um candidato está muito mal avaliado ou não. 

Podemos concluir que os 2 estão em uma disputa bem acirrada e que ambos têm muitas opiniões públicas positivas. 

É importante ter essa ideia das opiniões positivas, pois as questões mais divulgadas e comentadas dos 2 candidatos são opiniões negativas, levando a crer que “ninguém gosta dos 2 candidatos”. 

 

Para explicações mais detalhadas do projeto escrevi um artigo no Medium: 

 https://medium.com/@marcus.vicentini/an%C3%A1lise-de-sentimentos-do-twitter-de-candidatos-as-elei%C3%A7oes-brasileiras-de-2022-1a2d6555f0f5 

 

 
