make:
	make test

push:
	git checkout source
	git add -A
	git commit
	git push origin source

test:
	make clean
	# add folder to save not-preprocessed posts
	mkdir -p _postStorage
	cp _posts/* _postStorage/
	# do preprocessing
	./_preprocess.py
	# draft build
	jekyll build --draft
	# postprocessing
	./_postprocess.py
	-@[ -e "search.db" ] && mv -f search.db _site/search/search.db
	# restore pre-preprocessing state
	cp _postStorage/* _posts/
	# remove temporary files
	rm -rf _postStorage

deploy:
	make push
	# add folder to save not-preprocessed posts
	mkdir -p _postStorage
	cp _posts/* _postStorage/
	# do preprocessing
	./_preprocess.py
	# normal build
	jekyll build --config _config_prod.yml
	# postprocessing
	./_postprocess.py
	-@[ -e "search.db" ] && mv -f search.db _site/search/search.db
	# restore pre-preprocessing state
	cp _postStorage/* _posts/
	# remove temporary files
	rm -rf _postStorage
	# upload files to github
	git checkout master
	git rm -qr .
	cp -r _site/. .
	make clean
	git add -A
	git commit -m "misc"
	git push origin master
	git checkout source

martinde:
	make clean
	jekyll build --config _config_martinde.yml
	./_postprocess.py
	-@[ -e "search.db" ] && mv -f search.db _site/search/search.db

martincom:
	make clean
	# add folder to save not-preprocessed posts
	mkdir -p _postStorage
	cp _posts/* _postStorage/
	# do preprocessing
	./_preprocess.py
    #build
	jekyll build --config _config_martincom.yml
	./_postprocess.py
	-@[ -e "search.db" ] && mv -f search.db _site/search/search.db

clean:
	rm -rf _site
