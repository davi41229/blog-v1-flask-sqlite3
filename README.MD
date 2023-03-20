# projeto inicial- blog com crud.
# rota principal que mostra um loop com todos os posts
# postar,editar,deletar: titulo,autor,conteudo.
# estrutura flask: models,views,controllers

## Tecnologias

* python
* Flask
* Sqlite
* Html
* Css

## criação de ambiente virtual para instalar bibliotecas
## salvar relação das bibliotecas no arquivo requirements


´´´
python -m venv environment

pip install Flask==2.2.2
pip install Flask-SQLAlchemy==2.5.1
pip install sqlalchemy-connector==0.1.37
pip install SQLAlchemy==1.4.9

pip freeze > requirements.txt
pip install -r requirements.txt

´´´
## rodar==>

* python ./run.py