import math


def idf(corpus: list[list[str]]) -> dict[str, float]:
    '''
    calculate idf value of all words in the corpus.
    '''
    dicts = [set(doc) for doc in corpus]
    idf_cnt = {}
    for d in dicts:
        for w in d:
            idf_cnt[w] = idf_cnt.get(w, 0) + 1
    return {w: math.log(len(dicts)/cnt) for w, cnt in idf_cnt.items()}


def tf(document: list[str], stopwords=set()) -> dict[str, float]:
    '''
    Calculate tf value for all words in a document,
    filtering stopwords
    '''
    words = [word for word in document if word not in stopwords and len(
        word.strip()) >= 2]
    word_cnt = {}
    for w in words:
        word_cnt[w] = word_cnt.get(w, 0) + 1
    return {w: cnt/len(words) for w, cnt in word_cnt.items()}


def tfidf(document: list[str], idf_val: dict[str, float],
          stopwords=set(), topK=20) -> dict[str, float]:
    '''
    Calculate tfidf for all words,
    return topK words that has biggest value.
    Every word needs to be in idf.
    '''
    tf_val = tf(document, stopwords)
    tfidf_val = sorted([(tf_val[w]*idf_val[w], w)
                        for w in tf_val], reverse=True)
    return [w for v, w in tfidf_val[:topK]]
