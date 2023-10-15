from person import Person
import pandas
from datetime import date
from policy import Policy


class Book(Person):

    def __init__(self, name, status):
        super().__init__(name, status)
        self.rented_book_dict = {}
        self.oldest_rented_date = date.today()
        self.policy = Policy(self.name, self.status)

    def rent_book(self, online):
        data = pandas.read_csv("library.csv") #csv 불러오기
        book_list = []
        return_list = []
        index = 0
        if online:
            user_response = input("\n대여할 책의 이름을 입력해주세요: ")
            year = date.today().year
            month = date.today().month
            day = date.today().day
        else:
            user_response = input("\n대여한 책의 이름을 입력해주세요: ")
            year = input("대여한 년도를 입력해주세요: ")
            month = input("대여한 월을 입력해주세요: ")
            day = input("대여한 일을 입력해주세요: ")
        for d in data["name"]:
            book_list.append(d)
        for d in data["returned"]:
            return_list.append(d)
        for i in range(0, len(book_list)):
            if book_list[i] == user_response:
                index = i
        if user_response in book_list and return_list[index] == "r":
            self.rented_book_dict[user_response] = [year, month, day]
            return user_response
        else:
            print("도서가 이미 대여중이거나 존재하지 않습니다.")
            return "over"
    def oldest_rental(self):
        lst = list(self.rented_book_dict.values())
        dat = []
        for i in range(0, len(self.rented_book_dict)):
            dat.append(lst[i])
        if len(dat) != 0:
            self.oldest_rented_date = min(dat)
            oldest_days = (date.today() - self.oldest_rented_date).days
            return oldest_days
        else:
            return 0

    def return_book(self):
        print("도서를 반납합니다.")
        user_response = input("반납할 도서의 이름을 입력하세요: ")
        returned_book = user_response
        if user_response in self.rented_book_dict.keys():
            if (date.today() - self.rented_book_dict[user_response]).days > self.policy.rental_period:
                print("반납 기한이 지나서 연체료가 발생합니다! (연체료는 15일에 한번씩 발생합니다)")
                multiplier = ((date.today() - self.rented_book_dict[user_response]).days - self.policy.rental_period) / 15
                total_fine = multiplier * self.policy.fine
                print("총 연체료 : ", total_fine, "원")
                user_response = input("지불 하시겠습니까? ('y'=예, 'n'=아니오)")
                if user_response == "y":
                    self.rented_book_dict.pop(returned_book)
                    print("반납되었습니다!")
                    return returned_book
                else:
                    print("반납 취소되었습니다!")
                    return "over"
            else:
                self.rented_book_dict.pop(returned_book)
                print("반납되었습니다!")
                return returned_book
        else:
            print("대여 목록에 존재하지 않는 도서입니다. 다시 시도해 주세요")
            return "over"

    def get_oldest_rental(self):
        return self.oldest_rental() - self.policy.rental_period

