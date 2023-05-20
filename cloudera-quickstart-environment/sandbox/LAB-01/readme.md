# Trabalhando com HDFS

Agora voltaremos ao terminal onde executaremos os comandos básicos do HDFS.
Temos que ter em mente duas coisas uma a máquina virtual/local onde você está e do cluster.

Para você executar os comandos na máquina virtual é mesmo que em uma máquina
convencional.

Dessa forma para executarmos comandos em linha de comando no cluster de Hadoop
devemos precedem os comandos com a sintaxe hadoop

1. Evidentemente podemos utilizar como exemplos os gerenciadores gráficos para exemplificar as diferenças entre o que está no cluster e o que está na sua máquina local/virtual. Acima temos dois comandos no terminal para listar arquivos. Para aqueles que não tem intimidade com o Linux o comando é ```ls-l```. No cluster o comando é mesmo porem deve ser sempre precedido por hdfs dfs, assim teremos hdfs dfs -ls /diretorio.

2. Já para os Gerenciadores de arquivos temos aqueles que você está habituado em seu computador, já para o HDFS temos o HUE, que além da função de gerenciamento de arquivos existem outras que utilizaremos em outros laboratórios

3. A primeira coisa que iremos fazer é copiar um arquivo que está “localmente” para nosso cluster, que logo você perceberá que este lugar será o nosso Data Lake.

4. Entre na pasta que você compartilhou no passo da primeira parte deste laboratório. Para copiar o que está na máquina local para o HDFS, utiliza o comando: ```hdfs dfs -copyFromLocal /local/arquivo /local no HDFS```