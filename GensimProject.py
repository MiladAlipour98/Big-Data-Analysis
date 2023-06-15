import numpy as np
import pandas as pd
import re
from gensim.models import Word2Vec
import csv
#from sklearn.metrics.pairwise import cosine_similarity

dataset_path = 'persica.csv'
isna_data_frame = pd.read_csv(dataset_path, sep=",\n", header=None, encoding='utf-8', engine='python')


def save_output_to_file(filename, output):
    text_file = open("%s.txt" % filename, "w", encoding="utf-8")
    text_file.write("%s" % output)
    text_file.close()


# a
def read_isna_content():
    news_content_index = [i for i in range(2, len(isna_data_frame), 7)]
    redun_list = [i for i in range(len(isna_data_frame)) if i not in news_content_index]
    isna_data_frame.drop(redun_list, axis=0, inplace=True)
    separator = ' '
    return separator.join(isna_data_frame[0].tolist())


isna_news_content = read_isna_content()
save_output_to_file('Part1', isna_news_content)
print('part1 done')


# b
def normalize_isna_content(news_content):
    news_content = re.sub(r"\s+", " ", news_content)
    return news_content.replace('إ', 'ا').replace('أ', 'ا').replace('ك', 'ک').replace('ؤ', 'و').replace('ة', 'ه'). \
        replace('ۀ', 'ه').replace('ئ', 'ی').replace('ي', 'ی')

normalized_file= normalize_isna_content(isna_news_content)
save_output_to_file('Part2', normalized_file)
print('part2 done')


# c
def segment_corpus_isna(corpus):
    return list(corpus.replace('؛', '.').replace(':', '.').replace('!', '.').replace('؟', '.').split('.'))


file_sentences = segment_corpus_isna(normalized_file)
save_output_to_file('Part3', file_sentences)
print('part3 done')


# d
def prepare_final_isna(sentences):
    return [sentence.split() for sentence in sentences]


file_words = prepare_final_isna(file_sentences)
save_output_to_file('Part4', file_words)
print('part4 done')


# e
def train_model():
    model = Word2Vec(file_words, window=5, min_count=2, negative=5, vector_size=100)
    model.save("model")
    return model



model = train_model()
print('part5 done')

# f
save_output_to_file('Part6', model.wv.most_similar('ایران')[:5])
print('Part6', model.wv.most_similar('ایران')[:5])
print('part6 done')

# g
print('Part7-1', model.wv.most_similar('فلسطین')[:5])
print('Part7-2', model.wv.most_similar('آمریکا')[:5])
print('Part7-3', model.wv.most_similar('ایران،')[:5])
print('Part7-4', model.wv.most_similar('کشورمان')[:5])
print('Part7-5', model.wv.most_similar('ایرانی')[:5])
save_output_to_file('Part7-1', model.wv.most_similar('فلسطین')[:5])
save_output_to_file('Part7-2', model.wv.most_similar('آمریکا')[:5])
save_output_to_file('Part7-3', model.wv.most_similar('ایران،')[:5])
save_output_to_file('Part7-4', model.wv.most_similar('کشورمان')[:5])
save_output_to_file('Part7-5', model.wv.most_similar('ایرانی')[:5])
print('part7 done')





