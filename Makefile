make:
	make test

push:
	git checkout source
	git add -A
	git commit
	git push origin source

test:
	make clean
	jekyll build --draft
	./_removeWhitespace.py

deploy:
	make push
	jekyll build --config _config_prod.yml
	./_removeWhitespace.py
	git checkout master
	git rm -qr .
	cp -r _site/. .
	make clean
	git add -A
	git commit -m "misc"
	git push origin master
	git checkout source

clean:
	rm -rf _site
