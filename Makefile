push:
	git checkout source
	git add -A
	git commit
	git push origin source

deploy:
	jekyll
	git checkout master
	git rm -qr .
	cp -r _site/. .
	rm -r _site
	git add -A
	git commit
	git push origin master
