# functions.py => fn1~()부터 fn9()까지
from customer import Customer
def fn1_insert_customer_info():
    '''
    사용자로부터 name, phone, email, age, grade, etc를 입력받아 Customer형 객체 반환
    '''
    name = input('이름:')
    phone = input('번호:')
    email = input('매일:')
    while True:
        try:
            age = int(input('나이:'))
            if (age<0) or (age>130):
                raise Exception('나이 범위 이상')
            break
        except:
            print('올바른 나이를 입력하시오')
    try:
        grade = int(input('등급(1~5):'))
        if grade <1:
            grade = 1
        if grade >5:
            grade = 5
    except:
        print('유요하지 않는 등급 입력시 1등급으로 초기화')
    etc = input('기타 정보:')
    return Customer(name, phone, email, age, grade, etc)
def fn2_print_customers(customer_list):
    '''
    customer_list를 출력(pdf p.40)
    '''
    print('='*70)
    print('{:^70}'.format('고객정보'))
    print('='*70)
    print("{:>5}\t{:3}\t{:13}\t{:15}\t{:3}\t{}".format("grade", "이름", "전화",
                                                        "메일", "나이", "기타"))
    print('-'*70)
    for customer in customer_list:
          print(customer)
def fn3_delete_customer(customer_list):
    delete_name = input('삭제할 고객 이름은?')
    delete_idx = [] # 삭제할 인덱스를 저장하는 용도
    for idx, customer in enumerate(customer_list):
        if customer.name == delete_name:
            delete_idx.append(idx)
        if delete_idx:  # 뭔가 지울게 있다면 들어간다
            for idx in delete_idx[::-1]:# 반대로 삭제를 하는것 
                print(customer_list[idx], '지울겁니까?', end='')
                answer = input('(y/n)')
                if (answer == 'y') or (answer == 'Y'):
                # if answer.upper() == Y:
                    del customer_list[idx]
        else:
            print('{}님 데이터가 존재하지 않습니다'.format(delete_name))
def fn4_search_customer(customer_list):
    find_name=input('찾는이름:')
    find_idx=[]
    for idx, customer in enumerate(customer_list):
        if customer.name == find_name:
            find_idx.append(idx)
    if find_idx:     # 뭔가 지울게 있나? 라고 물어봄
        for idx in find_idx:
            #print('{}님 {}명 존재하였습니다'.format(find_name, len(find_idx))) 
            print(customer_list[idx])
    else:
        print('{}님 데이터가 존재하지 않습니다'.format(find_name))
def fn5_save_customer_csv(customer_list):
    '''
    매개변수로 받은 customer_list 를 딕셔너리 리스트로 변환
    '''
    import csv
    if customer_list:  # 커스터머가 들어있나? 라고 물어봄
        customer_dic_list = []
        for customer in customer_list:
            customer_dic_list.append(customer.as_dic())
        fieldnames = list(customer_dic_list[0].keys())
        filename = input('저장할 csv 파일명은?')
        with open('data/{}.csv'.format(filename), 'w', encoding='utf-8', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader()  # 헤더     
            dict_writer.writerows(customer_dic_list)
            print(f"data/{filename}.csv 내보내기 완료")
    else:
        print('입력된 데이터가 없습니다')
def fn9_save_customer_txt(customer_list):
    '''
    customer_list 를 list style 로 바꾼다
    to_list_style()을 이용해서 작업     ch09_customers.txt 로 백업
    '''
    customer_txt_list = []
    for customer in customer_list:
        customer_txt_list.append(customer.to_list_style() + '\n')
    with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f:
        f.writelines(customer_txt_list)
        