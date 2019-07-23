import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

# 通过txt生成词云

text_from_file_with_apath = open('python.txt',encoding='utf-8').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(background_color="white",width=1000,height=860, font_path="C:\\Windows\\Fonts\\STFANGSO.ttf").generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()