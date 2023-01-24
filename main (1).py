import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://edition.cnn.com/2023/01/20/asia/korean-war-fighter-pilot-soviet-shootdown-intl-hnk-ml/index.html'

article = Article(url)
article.download()
article.parse()
article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

root = tk.Tk()
root.title('News Summary')
root.geometry('1200x600')




root.mainloop()