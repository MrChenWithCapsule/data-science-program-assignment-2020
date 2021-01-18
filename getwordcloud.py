from pathlib import Path
import matplotlib.pyplot as plt
from tfidf import idf, tfidf
from wordcloud import WordCloud
from common import load_csvdata

comments = list([line.words for line in load_csvdata(Path('data/alldata'))])
idf_val = idf(comments)
all_comments = []
for c in comments:
    all_comments.extend(c)
tfidf_val = tfidf(all_comments, idf_val=idf_val, freq=True, topK=40)
wc = WordCloud(font_path='/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc',
               background_color='white', 
               height=600,
               width=1000)
wc.generate_from_frequencies(tfidf_val)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
