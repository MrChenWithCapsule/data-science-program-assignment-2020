import matplotlib.pyplot as plt
from matplotlib import rcParams
from common import load_csvdata, Weibo, Comment
from functools import reduce
from pathlib import Path
from time import struct_time, strptime

group_show = {'对牺牲者的哀悼', '批评红十字会', '批评政府掩盖事实,防控不力'}


def load_kwgroup(path: Path) -> dict[str, set[str]]:
    groups = {}
    with open(path) as file:
        for line in file:
            if line.isspace():
                continue
            split = line.split(':')
            if split[0] not in group_show:
                continue
            groups[split[0]] = set(split[1].strip().split(','))
    return groups


def filter_toolate(comments):
    return filter(lambda c: c.time.tm_year == 2020 and c.time.tm_mon == 2,
                  comments)


def group_by_date(
        comments: list[Comment]) -> list[tuple[struct_time, list[list[str]]]]:
    comments = sorted(comments, key=lambda c: c.time)
    comments.append((strptime('2021 01 01', '%Y %m %d'), []))
    result = []
    current_date = comments[0].time
    current_comments = []
    for (time, words) in comments:
        if time.tm_yday == current_date.tm_yday:
            current_comments.append(words)
        else:
            result.append((current_date, current_comments))
            current_date = time
            current_comments = []

    return result


def get_groupfreq_by_date(
        comments: list[Comment],
        groups: dict[str,
                     set[str]]) -> list[tuple[struct_time, dict[str, int]]]:
    comments_date = group_by_date(comments)
    result = []
    for (time, comments) in comments_date:
        wordset = list(map(lambda c: set(c), comments))
        group_freq = {}
        for (key, words) in groups.items():
            count = reduce(
                lambda prev, comment_words: prev
                if comment_words.isdisjoint(words) else prev + 1, wordset, 0)
            group_freq[key] = count / max(len(comments), 1)
        result.append((time, group_freq))
    return result


data = load_csvdata(Path('data/alldata'))
groups = load_kwgroup(Path('data/dict.md'))
groupcount = list(get_groupfreq_by_date(filter_toolate(data), groups))

rcParams['font.family'] = 'Noto Sans CJK JP'
fig, ax = plt.subplots()
for (key, _) in groups.items():
    ax.plot(list(map(lambda gc: gc[0].tm_yday, groupcount)),
            list(map(lambda gc: gc[1][key], groupcount)),
            label=key)
ax.legend()
plt.show()
