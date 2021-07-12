import re
import matplotlib.pyplot as plt
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from wordcloud.wordcloud import FONT_PATH
filepath = "J:\pleiades-4.7.3\workspace2\elearning\question5_2\maihime.txt"
out_filepath = "J:\pleiades-4.7.3\workspace2\elearning\question5_2\maihime_ルビ無し.txt"
try:
    with open(filepath, encoding='shift_jis') as f, open(out_filepath, 'w', encoding='shift_jis') as fo:
        txt=f.read()
        txt=re.split(r'-{50,}',txt)[2]
        txt=re.split(r'底本：',txt)[0]
        txt=re.sub(r'《.*?》|［＃.?］|｜','',txt)
        fo.write(txt)
except OSError as oe:
    print(oe.test_strerror)
t = Tokenizer()
token = t.tokenize(txt)
word_list = []
for line in token:
    tmp = re.split('\t', str(line))
    if '名詞' in tmp[1]:
        word_list.append(tmp[0])
words = " ".join(word_list)
print(words)
#wc = WordCloud(font_path=FONT_PATH, max_font_size=40).generate(words)
wc = WordCloud(background_color="white", font_path=r"C:\Windows\Fonts\msgothic.ttc")
wc.generate(words)
plt.imshow(wc)
plt.show()
