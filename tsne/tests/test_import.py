def test_import():
    import tsne

    assert tsne.__version__ is not None
    assert tsne.__version__ != "0.0.0"
    assert len(tsne.__version__) > 0


def test_import_bh_tsne():
    from tsne import bh_sne  # noqa
