import jieba
import csv
import json
from sys import stderr
from pathlib import Path
from typing import NamedTuple
from time import strptime, struct_time
from functools import reduce


class Comment(NamedTuple):
    time: struct_time
    words: list[str]


class Weibo(NamedTuple):
    id: int
    time: struct_time
    total_comment: int
    comments: list[Comment]


def load_csv(csv_path: Path) -> list[Comment]:
    comments = []
    with csv_path.open() as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 0:
                continue

            try:
                comment_time = strptime(row[0], "%Y-%m-%d %H:%M")
            except ValueError:
                comment_time = strptime('2020 '+row[0], '%Y %m月%d日 %H:%M')
            words = list(jieba.cut(row[1][row[1].find('：')+1:].strip()))
            if not len(words) == 0:
                comments.append(Comment(comment_time, words))

    return comments


def load_csvdata(dir_path: Path) -> list[Comment]:
    comments_file = map(lambda p: load_csv(p), dir_path.glob('*.csv'))
    return list(reduce(lambda x, y: x+y, comments_file))


def load_data(dir_path: Path) -> list[Weibo]:
    data = []

    files = dir_path.glob('*.json')
    ids = map(lambda p: p.name[:p.name.rfind('.')], files)
    for id in ids:
        json_path = dir_path/(id+'.json')
        csv_path = dir_path/(id+'.csv')

        if not json_path.exists() or not csv_path.exists():
            print("missing file for id %s" % id, file=stderr)
            continue

        weibo_time = None
        total_comment = 0
        with json_path.open() as jsonfile:
            obj = json.load(jsonfile)
            try:
                weibo_time = strptime(obj['date'], '%Y-%m-%d')
            except ValueError:
                print('wrong format in file %s' % json_path, file=stderr)
                exit(1)
            total_comment = obj['Comments']
            if not type(total_comment) == int:
                total_comment = int(total_comment)

        comments = load_csv(csv_path)
        data.append(Weibo(id, weibo_time, total_comment, comments))

    return sorted(data, key=lambda w: w.id)


def load_stopwords(path=Path('data/baidu_stopwords.txt')) -> set[str]:
    with open(path) as file:
        return set([line.strip() for line in file])
