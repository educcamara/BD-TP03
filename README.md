

## Como começar 

**Linux:**

```shell
sudo psql -U postgres -d postgres
```

**MacOS:**

Caso ainda não esteja rodando o PostgreSQL, inicie o serviço com o comando:

```shell
brew services start postgresql
```

```shell
psql -U $(whoami) -d postgres
```

Criar o usuário para teste:

```sql
create user icomp with password 'icomp';
create database icomp owner icomp;
```

Você consegue verificar se o usuário e o banco de dados foram criados com sucesso utilizando os comandos:

```sql
\du
\l
````