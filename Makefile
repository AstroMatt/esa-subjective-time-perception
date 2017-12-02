help:
	@sphinx-build -M help "docs/" "_docs/"

backup:
	heroku run --app time-perception python manage.py dumpdata  --exclude=contenttypes --exclude=auth.permission --exclude=sessions --exclude=admin > _data/$(date +%F).json

restore:
	python manage.py loaddata _data/$(date +%F).json

clean:
	-rm -fr _docs/

docs:
	@sphinx-build -b singlehtml docs/ _docs/

graph:
	@python manage.py graph_models database

urls:
	@python manage.py show_urls
