## Configuração
Crie um ambiente virtual com o pyenv (https://github.com/pyenv/pyenv-installer)

### Adicione as seguintes linhas no arquivo .bashrc
```
`echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc \ 
echo 'eval "$(pyenv init -)"' >> ~/.bashrc \ 
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc \ 
source ~/.bashrc`
```

### Para criar o ambiente virtual:
```
# pyenv install 3.6.12
# pyenv virtualenv 3.6.12 my_env
```

### Para ativar o ambiente virtual:
```
# pyenv activate my_env
```

## Para iniciar o projeto
```
python manage.py runserver
python manage.py migrate
```

## Para criar migrates baseados nos modelos
```
python manage.py makemigrations blog
```

## Criando usuário admin
```
python manage.py createsuperuser
```
