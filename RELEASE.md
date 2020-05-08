# How to release a new version

- Update `CHANGELOG.md`
- Update `README.md` and docs

```
export VERSION=1.0.0

git checkout -b release-${VERSION}
git commit -am "Release ${VERSION}.rc0" --allow-empty
git tag -a ${VERSION}.rc0 -m "${VERSION}.rc0"

make build
make upload test-pypi
```

```
git push origin ${VERSION}
git push
```

```

make upload-pypi

# Upload to test PyPI
make upload-test
```
