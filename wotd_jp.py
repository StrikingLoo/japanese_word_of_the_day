import pandas as pd

df = pd.read_csv('~/Documents/fun/jp_wotd/jlpt3_vocab.csv')
df.dropna(inplace=True)
def word(df):
	return dict(df.sample(1).iloc[0])

def show_word(df):
    a_word = word(df)
    print(a_word['word']+':\n\t'+a_word['hiragana']+'\n\t'+a_word['meaning'])

show_word(df)
