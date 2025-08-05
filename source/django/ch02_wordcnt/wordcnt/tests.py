from django.test import TestCase

# Create your tests here.
fulltxt = "홍길동 홍길동 아자"
strlength = len(fulltxt)
words = fulltxt.split()
wordcnt = len(words)
words_dic = dict()