#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: LatentDirichletAnalysis.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: LDA
# @Create: 2019-02-21 17:26:20
# @Last Modified: 2019-02-21 17:26:20
#

from collections import Counter
import random, pdb
documents = [
    ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
    ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
    ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
    ["R", "Python", "statistics", "regression", "probablility"],
    ["machine learning", "regression", "decision trees", "libsvm"],
    ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
    ["statistics", "probability", "mathmatics", "theory"],
    ["machine learning", "scikit-learn", "Mahout", "neural network"],
    ["neural networks", "deep learning", "Big Data", "artificial intelligence"],
    ["Hadoop", "Java", "MapReduce", "Big Data"], 
    ["statistics", "R", "statsmodels"],
    ["C++", "deep learning", "artificial intelligence", "probablility"],
    ["pandas", "R", "Python"],
    ["databases", "HBase", "Postgres","MySQL", "MongoDB"],
    ["libsum", "regression", "support vector machines"]
]

K = 4

document_topic_counts = [Counter() for _ in documents]
topic_word_counts = [Counter() for _ in range(K)]
topic_counts = [ 0 for _ in range(K)]
document_lengths = list(map(len, documents))
distinct_words = set([word for document in documents for word in document])
W = len(distinct_words)
D = len(documents)

def sample_from(weights):
    total = sum(weights)
    rnd = total * random.random()
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

# 文档中主题概率
def p_topic_given_document(topic, d, alpha=0.1):
    return ((document_topic_counts[d][topic] + alpha) / 
        (document_lengths[d] + K * alpha))

# 主题中单词概率
def p_word_given_topic(word, topic, beta=0.1):
    return ((topic_word_counts[topic][word] + beta) / 
        (topic_counts[topic] + W * beta))

# 更新主题权重
def topic_weight(d, word, k):
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)

def choose_new_topic(d, word):
    return sample_from([ topic_weight(d, word, k) 
            for k in range(K)])

random.seed(0)
document_topics = [ [random.randrange(K) for word in document] 
            for document in documents]


for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1

for iteror in range(1000):
    for d in range(D):
        for i, (word, topic) in enumerate(zip(documents[d], document_topics[d])):
            document_topic_counts[d][topic] -= 1
            topic_word_counts[topic][word] -= 1
            topic_counts[topic] -= 1
            document_lengths[d] -= 1

            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic

            document_topic_counts[d][new_topic] += 1
            topic_word_counts[new_topic][word] += 1
            topic_counts[new_topic] += 1
            document_lengths[d] += 1

topic_names = ["Big Data and programming languages",
                "Python and statistics",
                "databases",
                "machine learning"]

'''
for k, word_counts  in enumerate(topic_word_counts):
    for word, count in topic_counts.most_common():
        if count > 0:
            print(topik_names[topic], count)
'''

for document, topic_counts in zip(documents, document_topic_counts):
    print(document)
    for topic, count in topic_counts.most_common():
        if count> 0:
            print(topic_names[topic], count)
