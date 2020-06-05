import pandas as pd
import argparse

words_df = pd.read_csv('~/Documents/fun/jp_wotd/jlpt3_vocab.csv')
words_df.dropna(inplace=True)

sentences_df = pd.read_csv('sentences_clean.csv')


def word(df):
	return dict(df.sample(1).iloc[0])

def show_word(df):
    a_word = word(df)
    print(a_word['word']+':\n\t'+a_word['hiragana']+'\n\t'+a_word['meaning'])

def show_sentence(df):
	print(df.sample(1).iloc[0]['sentence'])

parser = argparse.ArgumentParser(description='Improve your Japanese vocabulary.')

parser.add_argument('-w', '--word', help='Get a random Japanese word', action='store_const', const=True)
parser.add_argument('-s', '--sentence', help='Get a random Japanese sentence', action='store_const', const=True)


ns = parser.parse_args()
if ns.sentence:
	print('Sentence of the day: ')
	show_sentence(sentences_df)
if ns.word:	
	show_word(words_df)
