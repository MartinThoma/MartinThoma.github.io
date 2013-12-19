push:
	git checkout source
	git add -A
	git commit
	git push origin source

test:
	rm -rf _site
	jekyll build
	./_removeWhitespace.py

deploy:
	make push
	jekyll build --config _config_prod.yml
	./_removeWhitespace.py
	git checkout master
	git rm -qr .
	cp -r _site/. .
	rm -r _site
	git add -A
	git commit -m "misc"
	git push origin master
	git checkout source
