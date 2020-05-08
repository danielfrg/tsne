# How to release a new version

- Update `CHANGELOG.md`
- Update `README.md` and docs

## Upload to test PyPI

```
export VERSION=1.0.0
git checkout -b release-${VERSION}

# Skip the rest for pushing to PyPI directly
git commit -am "Release ${VERSION}.rc0" --allow-empty
git tag -a ${VERSION}.rc0

make build
make upload-test

# Create venv and install rc version
pip install extra-index-url=https://test.pypi.org/simple tsne==0.3.0rc0

# Delete rc tag
git tag -d ${VERSION}.rc0
```

## Upload to PyPI

Merge branch created in the previous step.

```
export VERSION=1.0.0
git commit -am "Release ${VERSION}" --allow-empty
git tag -a ${VERSION}

make build
make upload-pypi
```
