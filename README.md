# Reconhecimento-Facial
  Projeto idealizado e realizado como requisito da disciplina de Projetos III do curso de Sistemas de Informações em seu 6º Período do Centro de Ensino Superior de Juiz de Fora (CES/JF) sendo ele realizado em conjunto por Jonas Antonio Gomes Vicente, Juan Ferreira Carlos e Lucas Gomes da Silva sobre a supervisão e acompanhamento do Professor Romualdo Monteiro de Resende Costa.

## Escopo do Projeto
  Este projeto foi idealizado sobre a prerrogativa de se desenvolver um sistema de reconhecimento facial para que individuos que se encontram cadastrados neste determinado sistema, seja este sistema voltado para festas, atividades escolares e/ou de graduação e afins, possa então ser reconhecido e após isto ter a sua presença devidamente informada e efetuada para com os organizadores e também receba em seu e-mail cadastrado que sua presença foi efetuada com sucesso.

## Das Tecnologias
  Para realizarmos tal empreendimentos escolhemos nos utilizar da Linguagem de Programação Python em conjunto com o conjunto de bibliotecas OpenCV para visão computacional sendo ambas tecnologias Open Source.
  
### Python
   É uma linguagem de programação de alto nível do tipo interpretada, também contém nela a orientação a objetos. Para mais       informações acesse o link: 
  <a href="https://www.python.org/" title="Clique e acesse agora!">Python</a>
    
### OpenCV
   O OpenCV é um conjunto de bibliotecas voltadas para a visão computacional e aprendizado de máquina, criado para o avanço da pesquisa na aréa visual e gráfica. Para mais informações aacesse o link:
   <a href="https://opencv.org/" title="Clique e acesse agora!">OpenCV</a>
    
## Dos algoritmos de reconhecimento do OpenCV
* ### Local Binary Pattern Histogram (LBPH) 
   É um dos mais fáceis dos algoritmos de reconhecimento ele se utiliza das imagens em escala de cinza lendo suas texturas e assim realiza na preparação dos dados das imagens um arquivo contendo um Histograma em números binários com um Id atrelado a ele, quando os algoritmos do OpenCv comparam a imagem devidamente preparada com o individuo diante da câmera realiza a verificação e nos retorna o Id. Para maiores informações leia sobre LBPH no site Oficial da OpenCV ou  leia este <a href="https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b" title="Clique e acesse agora!">Artigo de Kelvin Salton do Prado na Towards Dara Science</a> que possui um texto bastante explicativo (Em Inglês).
   
* ### Eigenfaces
   Neste algoritimo não se captura a iluminação contida na imagem, apenas retira-se as informações mais relevantes da imagem para ser tratada na hora de preparar os dados para a comparação realizada pela biblioteca OpenCV, sendo as faces classificadas com base em padrões mais genéricos, sendo que tal informação é codificada de forma mais eficiente possivel. Para maiores informações leia sobre Eigenfaces no site Oficial da OpenCV ou  leia este <a href="http://www.scholarpedia.org/article/Eigenfaces" title="Clique e acesse agora!">Artigo na Scholarpedia</a> que possui um texto bastante explicativo (Em Inglês).

* ### Fisherfaces
  Neste algoritmo busca-se classificar e não representar e é justamente com esta proposta em mente que se deve utilizar este método de visão computacional, desta maneira ele procura mapear subespaços que representem que mapeiem os vetores das amostras preparadas para assim ser realizado a comparação em tempo real com o objeto ou face desejada pelo software criado. Para maiores informações leia sobre Fisherfaces no site Oficial da OpenCV ou leia este <a href="http://www.scholarpedia.org/article/Fisherfaces" title="Clique e acesse agora!">Artigo na Scholarpedia</a> que possui texto bem explicativo (Em Inglês).
 
