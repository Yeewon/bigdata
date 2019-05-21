import re
import pprint as pp
from nltk import bigrams, word_tokenize
from nltk import ConditionalFreqDist
from nltk.probability import ConditionalProbDist,MLEProbDist,FreqDist
from nltk.util import ngrams
from operator import itemgetter

f = open('test.txt','r',encoding='UTF-8')
text = f.read()
text = re.sub('[-=#/?:$}",!\n\ufeff]', '', text) #불필요한 것들을 제거해준다.
text = text.replace("'","") #'는 re.sub에서 제거하기 힘들기 때문에 따로 제거해준다.


#unigram 어절 빈도를 계산하는 함수
def count(text):
    sp = text.split()
    word_dic = {}  # 어절과 빈도를 저장할 딕셔너리 생성

    for i in sp:    #각각은 str이다.
        if i in word_dic:   #해당 어절이 dic의 key값에 존재하는지 조사
            word_dic[i] = word_dic[i] + 1   #있는 값이면 value값을 +1
        else:
            word_dic[i] = 1     #없는 값이면 dic를 하나 추가해서 key값에 추가, value 1로 생성
    return word_dic


#trigram freq_tri에서 x 뒤에 오는 상위빈도 "y_z" 20개 출력하는 함수
def count_tri(x):
    # tri_find 라는 list형 변수에다 unigram의 상위 3개로 시작하는 것 모두 저장.
    tri_find = []
    tri_dic = {} #tigram과 빈도를 저장할 딕셔너리
    for tri in freq_tri:
        if tri[0] == x:
            tri_find.append(tri)
    for i in tri_find:
        if i in tri_dic: #해당 어절이 dic의 key값에 존재하는지 조사
            tri_dic[i] = tri_dic[i]+1 #있는 값이면 value값을 +1
        else:
            tri_dic[i] = 1
    tri_dic = sorted(tri_dic.items(),key=itemgetter(1),reverse=True)
    for i in tri_dic[:20]:
        print(i,end=' ')
    print()

#unigram 최상위 빈도 3개 출력
word_dic = count(text)

word_dic = sorted(word_dic.items(),key=itemgetter(1),reverse=True) # 내림차순으로 sorting. list형. 내부는 tuple자료형
print("Unigram 최상위 빈도 3개 : ",end='')

print(word_dic[0][0],end=' ')
print(word_dic[1][0],end=' ')
print(word_dic[3][0],end=' ')
print()


#bigram, trigram
sentences = text.split('.')
sentences = [x for x in sentences if x] #공백 string 자료 제거

freq_bi = [] #각각은 str로 이루어진 tuple
freq_tri = []
for sentence in sentences:
    sentence.strip() #양쪽 공백 제거
    tokens = word_tokenize(sentence)
    bigram = ngrams(tokens, 2, pad_left=True, pad_right=True, left_pad_symbol="SS", right_pad_symbol="SE")
    trigram = ngrams(tokens, 3, pad_left=True, pad_right=True, left_pad_symbol="SS", right_pad_symbol="SE")
    freq_bi += [t for t in bigram]
    freq_tri += [t for t in trigram]

cfd = ConditionalFreqDist(freq_bi)
cpd = ConditionalProbDist(cfd, MLEProbDist)

#bigram (x, y)에 대해 x 뒤에 오는 상위빈도 어절 y들 20개
print("<bigram (x, y)에 대해 x 뒤에 오는 상위빈도 어절 y들 20개>")
print("x = '그' 인경우 : ",end='')
print(cfd["그"].most_common(20))
print("x = '안' 인경우 : ",end='')
print(cfd["안"].most_common(20))
print("x = '있는' 인경우 : ",end='')
print(cfd["있는"].most_common(20))
print()


#trigram (x, y, z)에 대해 x 뒤에 오는 상위빈도 "y_z" 20개
print("<trigram (x, y)에 대해 x 뒤에 오는 상위빈도 어절 y들 20개>")
print("x = '그' 인경우 : ",end='')
count_tri('그')
print("x = '안' 인경우 : ",end='')
count_tri('안')
print("x = '있는' 인경우 : ",end='')
count_tri('있는')


