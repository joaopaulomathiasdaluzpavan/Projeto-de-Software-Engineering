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



