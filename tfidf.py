import math
from common import load_stopwords
from sys import stderr
from time import time


def idf(corpus: list[list[str]]) -> dict[str, float]:
    '''
    calculate idf value of all words in the corpus.
    '''
    print('idf() start', file=stderr)
    starttime = time()
    dicts = [set(doc) for doc in corpus]
    idf_cnt = {}
    for d in dicts:
        for w in d:
            idf_cnt[w] = idf_cnt.get(w, 0) + 1
    ret = {w: math.log(len(dicts)/cnt) for w, cnt in idf_cnt.items()}
    print('idf() end, time elapsed: %fs' % (time()-starttime), file=stderr)
    return ret


def tf(document: list[str], stopwords: set[str]) -> dict[str, float]:
    '''
    Calculate tf value for all words in a document,
    filtering stopwords
    '''
    print('tf() start', file=stderr)
    starttime = time()
    words = [word for word in document if word not in stopwords and len(
        word.strip()) >= 2]
    word_cnt = {}
    for w in words:
        word_cnt[w] = word_cnt.get(w, 0) + 1
    ret = {w: cnt/len(words) for w, cnt in word_cnt.items()}
    print('tf() end, time elapsed: %fs' % (time()-starttime), file=stderr)
    return ret


def tfidf(document: list[str], idf_val: dict[str, float],
          stopwords=load_stopwords(), topK=20, freq=False):
    '''
    Calculate tfidf for all words,
    return topK words that has biggest value.
    Every word needs to be in idf.
    '''
    print('tfidf() start', file=stderr)
    starttime = time()
    tf_val = tf(document, stopwords)
    tfidf_val = sorted([(tf_val[w]*idf_val[w], w)
                        for w in tf_val], reverse=True)
    if freq is True:
        ret = {w: v for v, w in tfidf_val[:topK]}
    else:
        ret = [w for v, w in tfidf_val[:topK]]
    print('tfidf() end, time elapsed: %fs' % (time()-starttime), file=stderr)
    return ret
