import doctest

def test_suite():
    import enhatts
    def set_up(doc_test):
        # ensures lazy field definitions work:
        doc_test.globs = enhatts.__dict__
    return doctest.DocTestSuite(enhatts, setUp=set_up)
