class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0
        
    def __str__(self):
        return f'{self.title} by {self.instructor}'

    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self):
        pass

    def show_details(self):
        print('Course Title : ', self.title)
        print('Intructor : ', self.instructor)
        print('Price : ', self.price)
        print('Number of Lectures : ', self.lectures)
        print('Users : ', self.users)
        print('Average rating : ', self.avg_rating)


class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, length_video):
        super().__init__(title, instructor, price, lectures)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print('Video Length : ', self.length_video)

class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print('pages : ', self.pages)


vc = VideoCourse('Learn C++', 'Jack', 30, 50, 10)
vc.new_user_enrolled('Allen')
vc.new_user_enrolled('Max')
vc.new_user_enrolled('Tom')
# vc.received_a_rating(3)
# vc.received_a_rating(5)
# vc.received_a_rating(4)
vc.show_details()

print()

pc = PdfCourse('Learn Java', 'Jim', 35, 50, 1000)
pc.new_user_enrolled('Allen')
pc.new_user_enrolled('Mary')
pc.new_user_enrolled('JIm')
# pc.received_a_rating(5)
# pc.received_a_rating(4)
# pc.received_a_rating(4.5)
pc.show_details()
