def safe_index(list, item):
    """
    list 안에 item 요소가 있으면 item 요소의 index를 반환, 없으면 -1반환
    list : 나열가능한 데이터
    item : 찾을 데이터
    """
    if item in list:
        return list.index(item)     #여기서 return 
    else :
        return -1
    #  return list.index(item) if item in list else -1
