FROM continuumio/miniconda3:4.8.2

RUN apt-get update \
    && apt-get install -y git build-essential libatlas-base-dev

RUN /opt/conda/bin/conda install -y ipython numpy cython scipy scikit-learn pytest

VOLUME /workdir
WORKDIR /workdir
