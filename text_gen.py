import pandas as pd;
from numpy.random import choice
with open('bee.txt') as file:
	words = file.read().split()

df = pd.DataFrame(columns = ['start' ,'after' ,'frequency'])
after = words[1:]
after.append('EndWord')
end_words = []
df['start'] = words
df['after'] = after
df['frequency']= df.groupby(by=['start','after'])['start','after'].transform('count')
df = df.drop_duplicates()

for word in words:
    if word[-1] in ['.','!','?'] and word != '.':
        end_words.append(word)
        
pivot_df = df.pivot(index = 'start', columns= 'after', values='frequency').fillna(0)
sum_words = pivot_df.sum(axis=1)

pivot_df = pivot_df.apply(lambda x: x/sum_words).fillna(0)

def make_a_sentence(start):
    word = start
    sentence = [word]
    while len(sentence) < 30:
        next_word = choice(a = list(pivot_df.columns), p = (pivot_df.iloc[pivot_df.index == word].fillna(0).values)[0])
        if next_word == 'EndWord':
                continue
        elif next_word in end_words:
            if len(sentence) > 2:    
                sentence.append(next_word)
                break
            else :
                continue
        else :
            sentence.append(next_word)
        word=next_word
    sentence = ' '.join(sentence)
    print(sentence)
    return sentence
sentence = make_a_sentence(input().strip())

