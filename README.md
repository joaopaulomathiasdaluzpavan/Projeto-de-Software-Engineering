# Projeto-de-Software-Engineering
Temática do projeto: Sistema de Login e de Cadastro

O sistema de login e de Cadastro foi realizado com base em um vídeo do youtube, com o intuito da criação dessa aplicação para possíveis outros sistemas que envolvam login e cadastro. 

Tecnologias utilizadas: 
Customtkinter e o PIL (Image): ambos utilizados para a construção da interface gráfica e para carregar / inserir a imagem adicional para completar a aplicação;

tkinter (messagebox): esta biblioteca também é referente a parte de interface gráfica, mas ela está sendo utilizada para gerar os pop-ups de mensagens de erro e de se o cadastro ou login foram realizados com sucesso;

Sqlite3: esta biblioteca foi utilizada para fazer a conexão com o banco de dados, em que é possível fazer a conexão pelço próprio código python, referenciando o nome do banco de dados, criação de uma ponte / conexão para que ao ser atualizado ou criado algo seja expresso no bandco de dados. 

# Instruções para a execução do sistema: 

Primeiramente, caso a pessoa não tenha as bibliotecas instaladas, necessita de instalação: 
No VS code vá no menu superior e clique em ... > clique em Terminal > new Terminal > agora para as instalações, no prompt / terminal gerado digite pip install customtkinter e aguarde o processo de instalação > digite também pip install pillow e aguarde > já o tkinter e o sqlite3 já vêm instalados no python por padrão. 

Após isso, o usuário deverá clicar no botão de play para a execução da aplicação. Ao abrir a execução o usuário se depara com o campo de login, em que é pedido o nome de usuário e a senha do mesmo, abaixo há um botão para a visualização de senha, pois para mais segurança quando digita-se a senha no campo os caractéres são trocados por asteriscos. Abaixo tem-se os botões de FAZER LOGIN e se o usuário não tiver uma conta cadastrada o mesmo deverá cadastrar uma conta, clicando em FAZER CADASTRO.

Se o usuário colocar uma conta que não existe a aplicação irá retornar que OS DADOS NÃO FORAM ENCONTRADOS NO SISTEMA, que REVISE OS DADOS INSERIDOS ou CADASTRE-SE NA PLATAFORMA. 

Já na tela de fazer o cadastro, o usuário tem 4 campos: Nome de usuário, Email de usuário, Senha do usuário e Confirme a sua senha. Abaixo desses campos tem um botão de visualizar senha para que o usuário possa ver sua senha, pois os dígitos que são inseridos nos campos de senha são alterados para asterisco. 

Caso o usuário deixe algum dos campos sem preencher o programa vai retornar um erro de PREENCHA TODOS OS CAMPOS, caso o nome ou a senha seja menor de 4 caratéres o programa irá retornar um erro.Também dará erro de os campos de senha e de confirmar senha se ambos forem diferentes. Também há um botão de retorno para a página de login, em que o usuário poderá retornar e poder realizar o login e agora dar certo, caso coloque o nome de usuário e a senha respectiva de seu usuário.

# Ferramentas para o desenvolvimento do projeto e resoluções e apontamentos de alguns pontos 

Utilizar ferramnetas como o github actions auxilia na automação de testes repetitivos que o usuário perderia muito tempo para a execução de uma tarefa repetitiva. E que por meio destas implementações seria possível ver possíveis erros ao decorrer de cada etapa de repetição da automação. Assim, mostrando onde ocorreu o erro e por que dele ocorrer. Assegurando a confiabilidade e a identificação de erros para correções futuras. 

As principais mudanças que podem ser observadas por meio da alteração da metodologia utilizada decorrem de adaptação da entrega das sprints, em que na metodologia cascata só há um único fluxo de trabalho, que as retomadas ou as revisões sempre ocorrem ao término ou perto do término do projeto, dessa forma os custos para reparos podem ser grandes e a continuação pode vir a ser inviável, ou também se o projeto sofrer alguma alteração no meio do desenvolvimento para retornar para as etapas anteriores pode ser um pouco mais trabalhoso e custoso para a equipe. Já a metodologia ágil é diferente, ela trabalha com ciclo de sprints que ocorrem semanalmente ou a cada 2 semanas, em que há constantes reuniões para se saber o ponto que foi atingido, quais os problemas que o projeto está tendo, o por que dos mesmos estarem ocorrendo, apontamentos, sugestões para mitigar esses riscos durante a produção. Além de realizar um quadro de prioridades (utilizando o método MOSCOW - must have, shold have, could have e won't have). 

# A implementação da metodologia ágil para o desenvolvimento do projeto

Durante a execução do projeto (um pouco em cima da hora), o fluxo que estava seguindo de implementar o sistema de login com base no vídeo tutorial, eu fui fazendo ao mesmo tempo, dessa forma acaba por realizando a forma de metodologia por meio do método cascata. Mas, se fosse implementado a metodologia ágil seria mais vantajoso, mediante que poderia dividir o fluxo dos vídeos / funcionalidades por meio de sprints, podendo realizar uma por dia para que não ficasse muito sobrecarregado ou com dificuldades de acessar tais ferramentas e apontamentos para as implementações, além da ordem de prioridade mediante a outros projetos em paralelo que estavam sendo realizados ao longo do semestre. 

# Principais causas de falhas de projetos que envolvem métodos ágeis 

Os problemas que mais são vistos por meio da transição de um projeto que viava pela metodologia cascata para a ágil decorrem de priorizar tarefas que não possuem tanto impacto dentro da aplicação, dessa forma demorando ainda mais para fazer tarefas que realmente precisam ser feitas e focando apenas em tarefas secundárias, que causam a  lentidão e a demora para a entrega da sprint e do projeto também; confusão na entrega das sprints, que ao determinar um período X para uma parte da entrega as vezes as pessoas ficam perdidas sobre o que fazer ou também não cumprem com a entrega, assim gerando atrasos nas entregas e gerando gargalos para entregas futuras, acumulando mais funções; apresentação da temática com explicação que confunde as pessoas / equipe, que se a regra não for bem explicita pode acabar por gerar multiplas perspectivas acerca do projeto e sem uma linha de raciocínio apontando para uma direção acaba prejudicando o projeto (não que há apenas um caminho ou uma única maneira de seguir, mas que todos entrem em consonância na realização do projeto). Acabando por impactar a eficiência e a organização do projeto. 



