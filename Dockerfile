FROM continuumio/miniconda

RUN apt-get update && apt-get install -y git build-essential libatlas-base-dev

RUN /opt/conda/bin/conda install ipython numpy cython scipy scikit-learn pytest -y

VOLUME /tsne
WORKDIR /tsne
