from hlp import Hlp

test_nlp = Hlp("../../ltp_data_v3.4.0","../raw_data") #ltp模块的路径
test_list = test_nlp.process_ques("袭人和李纨是什么关系？"); #nh nh r n
print(test_list)
test_list = test_nlp.process_ques("袭人和李纨"); #nh nh
print(test_list)
test_list = test_nlp.process_ques("贾政是谁的爹？");#nh r n
print(test_list)
test_list = test_nlp.process_ques("谁的爸爸是贾政？");#r n nh
print(test_list)
test_list = test_nlp.process_ques("贾政的儿子是谁？");#nh n r
print(test_list)
test_list = test_nlp.process_ques("谁是贾政的儿子？");#r nh n
print(test_list)
test_list = test_nlp.process_ques("贾政的儿子");#nh n
print(test_list)