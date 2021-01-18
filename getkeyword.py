import tfidf
from pathlib import Path
from pprint import pprint
from time import strftime
from functools import reduce
from common import load_data, Weibo, load_stopwords


def filter_toolate(data: list[Weibo]):
    filtered = []
    for w in data:
        comments = list(filter(lambda c: c.time.tm_yday <=
                               w.time.tm_yday+3, w.comments))
        filtered.append(Weibo(w.id, w.time, w.total_comment, comments))
    return filtered


def get_keyword(data: list[Weibo], stopwords=set()) -> list[list[str]]:
    comments_flat: list[list[str]] = map(
        lambda w: reduce(lambda x, y: x+y.words, w.comments, []), data)
    idf = tfidf.idf(comments_flat)
    weibo_keywd = []
    for id, time, total, comments in data:
        all_text = reduce(lambda x, y: x+y.words, comments, [])
        weibo_keywd.append(
            tfidf.tfidf(all_text, idf, stopwords=stopwords))

    return weibo_keywd


sw = load_stopwords()
data = load_data(Path('./data/FilterData'))
data = filter_toolate(data)
result = get_keyword(data, sw)
print('total weibo: %d' % len(result))
pprint([(id, strftime('%m%d', time), '(total: %d, crawled: %d)'
         % (total, len(c)), kw)
        for (id, time, total, c), kw in zip(data, result)], compact=True)
