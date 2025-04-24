# customer.py = Customer클래스 to_customer(), load_customer()
class Customer:
    '고객 데이터와 as_dic(), to_list_style(txt백업시), __str()'
    def __init__(self, name, phone, email, age, grade, etc):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.grade = grade
        self.etc = etc
    def as_dic(self): # 고객데이터를 딕셔너리로
        return {'name' : self.name,
                'phone' : self.phone,
                'email' : self.email,
                'age' : int(self.age),
                'grade' : int(self.grade),
                'etc': self.etc}
    def to_list_style(self):
        return "{},{},{},{},{},{}".format(self.name, self.phone, self.email, int(self.age), int(self.grade), self.etc)
           # "유질동, 010-5432-2222,yu@hong.com,20,3, 열심히"
        # temp = [self.name, 
        #        self.phone, 
        #        self.email, 
        #        str(self.age), 
        #        str(self.grade), 
        #        self.etc]
        # return ', '.join(temp)
    def __str__(self):
        return "{:>5}\t{:3}\t{:13}\t{:15}\t{:3}\t{} ".format('★'*self.grade, self.name, self.phone, self.email, self.age, self.etc)
       # {}안에 띄어 쓰기랑 format 안에 self.name ~~ 식으로 가야 한다
def to_customer(row):
    '''
      row =  홍길동, 010-9999-9999, a@a.com, 30, 3, 까칠해 이 내용을 매개 변수 받아
      customer 객체로 return
    '''  
    data = row.split(',')
    name = data[0]
    phone = data[1].strip() # strip은 앞뒤 white space 제거
    email = data[2].strip()
    age = int(data[3].strip())
    grade = int(data[4].strip())
    etc = data[5].strip()
    return Customer(name, phone, email, age, grade, etc)
def load_customers():
    customer_list = []
    try:
        with open('data/ch09_customer.txt', 'r', encoding='utf-8') as f:
            # txt 데이터 한줄씩 customer 객체로 받아 customer_list.append
            lines = f.readlines() # 한꺼번에 읽는거Ff
            for line in lines:  #line = "홍길동, 010-9999-9999, a@a.com, 30, 3, 까칠해"
                customer = to_customer(line)
                customer_list.append(customer)
    except:
        with open('data/ch09_customer.txt', 'w', encoding='utf-8') as f:
            print('초기화 파일을 생성했습니다')
    return customer_list