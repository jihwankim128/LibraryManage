import pandas
import os
from person import Person
from book import Book
from policy import Policy
from datetime import date

dict_book = {}
person_list = []
bookobj_list = []
policyobj_list = []
genre = ""
name = ""
fined_person_list = []
data = pandas.read_csv("library.csv")
namel = []
genrel = []
returnedl = []
statusl = []
yearl = []
monthl = []
datel = []

def clear():
    os.system('cls')

def recover_memory():

    for d in data["name"]:
        namel.append(d)
    for d in data["genre"]:
        genrel.append(d)
    for d in data["returned"]:
        returnedl.append(d)
    for d in data["status"]:
        statusl.append(d)
    for d in data["year"]:
        yearl.append(d)
    for d in data["month"]:
        monthl.append(d)
    for d in data["date"]:
        datel.append(d)
    ind = []
    dict_book["name"] = namel
    dict_book["genre"] = genrel
    dict_book["returned"] = returnedl
    dict_book["status"] = statusl
    dict_book["year"] = yearl
    dict_book["month"] = monthl
    dict_book["date"] = datel

    for i in range(0, len(returnedl)):
        if not returnedl[i] == "r":
            ind.append(i)

    for i in ind:
        user_name = returnedl[i]
        user_status = statusl[i]
        user_book = namel[i]
        user_year = yearl[i]
        user_month = monthl[i]
        user_date = datel[i]
        p = Person(user_name, user_status)
        book = Book(p.name, p.status)
        policy = Policy(p.name, p.status)
        book.rented_book_dict[user_book] = date(int(user_year), int(user_month), int(user_date))
        person_list.append(p)
        bookobj_list.append(book)
        policyobj_list.append(policy)

def add_books_to_library():
    clear()
    print("현재 장르 목록입니다.")
    data = pandas.read_csv("library.csv")
    dgenre = [d for d in data["genre"]]
    print(list(set(dgenre)))
    genre = input("추가할 도서의 장르를 입력해 주세요: ")
    name = input("추가할 도서의 이름을 입력해 주세요: ")
    genrel.append(genre)
    namel.append(name)
    returnedl.append("r")
    statusl.append("")
    yearl.append("")
    monthl.append("")
    datel.append("")
    dict_book["name"] = namel
    dict_book["genre"] = genrel
    dict_book["returned"] = returnedl
    dict_book["status"] = statusl
    dict_book["year"] = yearl
    dict_book["month"] = monthl
    dict_book["date"] = datel
    library_status = pandas.DataFrame(dict_book)
    library_status.to_csv("library.csv")

def remove_books_to_library():
    clear()
    find_index = 0
    print("\n==도서제목==\n",namel)
    name = input("\n삭제할 도서의 이름을 입력해 주세요: ")
    if name in namel :
        nameIndex = [i for i in range(0,len(namel)) if name==namel[i]]
        for i in nameIndex :
            print("\n",name,"의 장르 : ",genrel[i])
            checking = input("\n해당 장르가 맞나요? (y,n) : ")
            if checking == 'y' or checking == 'Y' :
                find_index = i
                print("해당 도서가 삭제 되었습니다.")
                break
            else:
                print("삭제를 진행하지 않겠습니다.")
        del genrel[find_index]
        del namel[find_index]
        del returnedl[find_index]
        del statusl[find_index]
        del yearl[find_index]
        del monthl[find_index]
        del datel[find_index]
        dict_book["name"] = namel
        dict_book["genre"] = genrel
        dict_book["returned"] = returnedl
        dict_book["status"] = statusl
        dict_book["year"] = yearl
        dict_book["month"] = monthl
        dict_book["date"] = datel
        library_status = pandas.DataFrame(dict_book)
        library_status.to_csv("library.csv")
    else:
        print("없는 도서입니다.")


def view_library_status():
    clear()
    data = pandas.read_csv("library.csv")
    print("현재 도서관에 등록된 도서: \n")
    if len(data["name"]) == 0:
        print("도서가 없습니다")
    else:
        for d in range(0, len(data["name"])):
            print("도서명-",(data["name"])[d])
            print("장르-",(data["genre"])[d])
            print()
def view_library_staff():
    clear()
    data = pandas.read_csv("library.csv")
    if len(data["name"]) == 0:
        print("도서가 없습니다")
    else:
        print(data)
    if len(data["name"]) < 3:
        print("현재 존재하는 도서 수 : ", len(data["name"]))
        user_response = input(" 도서가 부족합니다, 도서를 추가해 주세요 ('y'=예, 'n'=아니오): ")
        if user_response == "y":
            add_books_to_library()

def get_books_by_genre():
    clear()
    data = pandas.read_csv("library.csv")
    dgenre = [d for d in data["genre"]]
    print("장르 목록입니다\n\n", list(set(dgenre)))
    user_response = input("\n찾고자 하는 장르를 입력하세요: ")
    print()
    if user_response in dgenre:
        genre_list = data[data.genre == user_response]
        print(genre_list.name)
    else :
        print("\nError: 장르 목록 내에서 선택해주세요")

def get_books_by_r():
    data = pandas.read_csv("library.csv")
    print("현재 대여 가능한 도서 목록입니다: ")
    unreturned = data[data.returned == "r"].name
    print(unreturned)

def get_rented_books():
    clear()
    data = pandas.read_csv("library.csv")
    print("미반납자를 조회한 목록입니다. \n")
    unreturned = data[data.returned != "r"]
    print(unreturned)

def offline_renting():
    clear()
    data = pandas.read_csv("library.csv")
    print("==== 대여 ====")
    user_name = input("대여자의 성함을 입력해주세요 : ")
    print("1. student, 2. professor, 3. guest")
    user_status = input("대여자의 직업을 입력해주세요 : ")
    user = Person(user_name, user_status)
    print("\n ====대여가능한 도서목록==== \n")
    get_books_by_r()
    book = Book(user.name, user.status)
    rented_book = book.rent_book(False)
    if rented_book != "over":
        index = dict_book["name"].index(rented_book)
        (dict_book["returned"])[index] = user_name
        (dict_book["status"])[index] = user_status
        (dict_book["year"])[index] = (book.rented_book_dict[rented_book])[0]
        (dict_book["month"])[index] = (book.rented_book_dict[rented_book])[1]
        (dict_book["date"])[index] = (book.rented_book_dict[rented_book])[2]
        person_list.append(user)
        bookobj_list.append(book)
        library_status = pandas.DataFrame(dict_book)
        library_status.to_csv("library.csv")

def renting(type):
    clear()
    data = pandas.read_csv("library.csv")
    print("==== 대여 ====")
    user_name = input("성함을 입력해주세요 : ")
    user = Person(user_name, type)
    clear()
    print("\n\n★환영합니다.", user.name, "님★\n\n ====대여가능한 도서목록==== \n")
    get_books_by_r()
    book = Book(user.name, user.status)
    rented_book = book.rent_book(True)
    if rented_book != "over":
        index = dict_book["name"].index(rented_book)
        (dict_book["returned"])[index] = user_name
        (dict_book["status"])[index] = type
        (dict_book["year"])[index] = (book.rented_book_dict[rented_book])[0]
        (dict_book["month"])[index] = (book.rented_book_dict[rented_book])[1]
        (dict_book["date"])[index] = (book.rented_book_dict[rented_book])[2]
        person_list.append(user)
        bookobj_list.append(book)
        library_status = pandas.DataFrame(dict_book)
        library_status.to_csv("library.csv")

def returning():
    clear()
    data = pandas.read_csv("library.csv")
    user_name = input("반납하는 사람의 성함을 입력해주세요: ")
    match = False
    p_list = []
    for person in person_list:
        p_list.append(person.name)
        if user_name == person.name:
            match = True
    if match:
        i = p_list.index(user_name)
        print(bookobj_list[i].rented_book_dict)
        value = bookobj_list[i].return_book()
        if value != "over":
            index = dict_book["name"].index(value)
            (dict_book["returned"])[index] = "r"
            (dict_book["status"])[index] = ""
            (dict_book["year"])[index] = ""
            (dict_book["month"])[index] = ""
            (dict_book["date"])[index] = ""
            if len(bookobj_list[i].rented_book_dict) == 0:
                person_list.remove(person_list[i])
        library_status = pandas.DataFrame(dict_book)
        library_status.to_csv("library.csv")
    else :
        print("대여기록이 없는 사용자입니다.")

def is_fine():
    clear()
    for b in bookobj_list:
        b.oldest_rental()
        if b.get_oldest_rental() > Policy(b.name, b.status).rental_period:
            fined_person_list.append(b)

recover_memory()
def UserSelect():
    clear()
    print("반갑습니다. 사용자를 선택해주세요\n")
    print("1: 학부생")
    print("2: 교수진")
    print("3: 외부인")
    print("4: 관리자")
    print("0: 종  료")
    return input("\n입력하세요 ◀:")
def Load():
    clear()
    print("===도서 처리 프로그램 입니다===")
    input("이용 하시려면 엔터키를 누르세요")


def check(type):
    clear()
    if type == "student":
        print("==== 학  생 ====")
    elif type == "professor":
        print("==== 교  수 ====")
    else :
        print("==== 외부인 ====")
def staff_Menu():
    clear()
    print("==== 관리자 ====")
    print("1: 도서 추가하기")
    print("2: 도서 제거하기")
    print("3: 도서 미반납자 조회")
    print("4: 연체자 목록 조회")
    print("5: 도서 현황 조회")
    print("6: 오프라인 대여자 등록")
    print("0: 처음으로")
    key = input("\n입력하세요 ◀:")
    if key == "0":
        Run(True)
    elif key == "1":
        add_books_to_library()
    elif key == "2":
        remove_books_to_library()
    elif key == "3":
        get_rented_books()
    elif key == "4":
        is_fine()
        for f in fined_person_list:
            print(f.name, "최대 ", f.get_oldest_rental(),"일 미반납")
    elif key == "5":
        view_library_staff()
    elif key == "6":
        offline_renting()
    else:
        print("잘못입력했습니다.")
    input("\n\n엔터키를 눌러주세요")
    staff_Menu()

def MenuSelect(type):
    check(type)
    print("1: 도서목록 보기")
    print("2: 장르별 도서 보기")
    print("3: 도서 대여하기")
    print("4: 도서 반납하기")
    print("0: 처음으로")
    key = input("\n입력하세요 ◀:")
    if key == "0":
        Run(True)
    elif key == "1":
        view_library_status()
    elif key == "2":
        get_books_by_genre()
    elif key == "3":
        renting(type)
    elif key == "4":
        returning()
    else:
        print("잘못입력했습니다.")
    input("\n\n엔터키를 눌러주세요")
    MenuSelect(type)

def Run(start):
    while start:
        user_type = ""
        user_response = UserSelect()
        if user_response == "0":
            clear()
            print("이용해주셔서 감사합니다.\n")
            print("프로그램을 종료하겠습니다.")
            exit()
        elif user_response == "1":
            user_type = "student"
            MenuSelect(user_type)
        elif user_response == "2":
            user_type = "professor"
            MenuSelect(user_type)
        elif user_response == "4":
            user_type = "staff"
            staff_Menu()
        elif user_response == "3":
            user_type = "guest"
            MenuSelect(user_type)
        else:
            input("다시 선택해주세요.")
Load()
Run(True)

