
f = open('test.txt','r',encoding='UTF-8')   #파일을 읽기용으로 연다.

def count(f):   #unigram 어절 빈도를 계산하는 함수
    w = f.read()
    sp = w.split()
    word_dic = {}  # 어절과 빈도를 저장할 딕셔너리 생성

    for i in sp:    #각각은 str이다.
        if i in word_dic:   #해당 어절이 dic의 key값에 존재하는지 조사
            word_dic[i] = word_dic[i] + 1   #있는 값이면 value값을 +1
        else:
            word_dic[i] = 1     #없는 값이면 dic를 하나 추가해서 key값에 추가, value 1로 생성
    return word_dic

def probability(word_dic):  #각 어절들에 대한 어절출현 확률 계산하는 함수
    p_dic = {}  # 어절과 어절출현확률을 저장할 딕셔너리 생성
    total_cnt = 0 # 0으로 초기화
    for i in word_dic.values(): #value값만을 불러와 모든값을 더한다.
        total_cnt = total_cnt + i
    p_dic = word_dic
    for j in p_dic:
        p_dic[j] = p_dic[j] / total_cnt
    return p_dic

def total_prob(p_dic):
    sentence_prob = 1.0  # 문장생성 확률 1로 초기화
    for i in p_dic.values():
        sentence_prob = sentence_prob * i
    return sentence_prob

word_dic = count(f)
print(word_dic)
p_dic = probability(word_dic)
print(p_dic)
print(total_prob(p_dic))

f.close()   #파일을 닫는다.








