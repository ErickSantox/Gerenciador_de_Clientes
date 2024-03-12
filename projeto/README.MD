Gerenciador de Clientes
    Este é um simples aplicativo de gerenciamento de clientes desenvolvido em Python usando a biblioteca Tkinter. O aplicativo permite cadastrar, buscar, alterar e excluir informações de clientes.

Como Usar
    Certifique-se de ter o Python instalado em seu sistema. Em seguida, execute o seguinte comando para instalar as dependências necessárias:

    Pip install customtkinter

Após a instalação, execute o script Python para iniciar o aplicativo:

    python projeto\Main.py

Funcionalidades

    Cadastro de Cliente

        Preencha todos os campos necessários.
        Clique no botão "Cadastrar Cliente".
        Os dados serão salvos no banco de dados.

    Busca por Endereço

        Insira o endereço do cliente no campo correspondente.
        Clique no botão "Buscar".
        Serão exibidos os dados do cliente encontrado.

    Alteração de Dados

        Busque o cliente pelo endereço.
        Modifique os campos necessários.
        Clique no botão "Alterar dados".
        As informações do cliente serão atualizadas.

    Limpar Campos

        Clique no botão "Limpar Campos" para resetar todos os campos.

    Exclusão de Cliente

        Insira o endereço do cliente no campo correspondente.
        Clique no botão "Deletar".
        O cliente será removido do banco de dados.



Personalização de Aparência

    Altere o tema do aplicativo no menu suspenso "Tema".
    Escolha entre os temas: System, Light e Dark.

Observação
    Este aplicativo utiliza a biblioteca customtkinter para aprimorar a interface gráfica. Certifique-se de ter essa biblioteca instalada para uma melhor experiência visual.


Observação sobre Configuração do Banco de Dados

    Este aplicativo foi desenvolvido para utilizar um banco de dados PostgreSQL. No entanto, a configuração do banco de dados não está integrada diretamente ao código-fonte. Fica a cargo do usuário configurar o banco de dados conforme necessário para o seu ambiente.

    Certifique-se de criar um banco de dados no PostgreSQL e configurar as credenciais no script ou em um arquivo de configuração apropriado. Se necessário, adapte o código para refletir as informações específicas do seu banco de dados, como nome do banco, usuário, senha, etc.

    Lembre-se de garantir que as bibliotecas necessárias estejam instaladas, incluindo o driver PostgreSQL para Python, que pode ser instalado com o seguinte comando:

    Pip install psycopg2

    Se surgirem dúvidas ou problemas durante a configuração do banco de dados, consulte a documentação do PostgreSQL ou entre em contato para obter assistência.


Desenvolvido por [Erick Santos] - [https://github.com/ErickSantox].