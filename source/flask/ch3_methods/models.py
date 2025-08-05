class Member(BaseModel):
    name: str
    id: str
    pw: str
    addr: str 
  if __name__ == '__main__':
    member = Member('hong', 1, 'pw', '서울')
    print(member)