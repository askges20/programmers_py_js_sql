def solution(phone_book):
    phone_book.sort()
    for a in range(len(phone_book)-1):
        if phone_book[a+1].startswith(phone_book[a]):
            return False
    return True
