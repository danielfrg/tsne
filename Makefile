PWD := $(shell pwd)


.PHONY: build
build:  ## Build package
	python setup.py sdist


.PHONY: upload
upload:  ## Upload package to pypi
	twine upload dist/*.tar.gz


.PHONY: env
env:  ## Create dev environment
	conda env create


.PHONY: docker
docker:  ## Docker image for testing
	docker build -t danielfrg/tsne .


.PHONY: docker-run
docker-run:  ## Run docker container
	docker run -it -v $(PWD):/workdir danielfrg/tsne


.PHONY: clean
clean:  ## Clean files
	rm -rf dist .eggs
	rm default.profraw
	rm -rf *.pyc *.so build/ bh_sne.cpp
	rm -rf tsne/*.pyc tsne/*.so tsne/build/ tsne/bh_sne.cpp


.PHONY: help
help:  ## Show this help menu
	@grep -E '^[0-9a-zA-Z_-]+:.*?##.*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?##"; OFS="\t\t"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, ($$2==""?"":$$2)}'
