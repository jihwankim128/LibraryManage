from person import Person

class Policy(Person):

    def __init__(self, name, status):
        super().__init__(name, status)

        self.rental_period = 0
        self.fine = 0
        self.set_rental_period()
        self.set_fine()

    def set_rental_period(self):
        if self.status == "professor":
            self.rental_period = 30

        elif self.status == "student":
            self.rental_period = 25

        elif self.status == "guest":
            self.rental_period = 15

    def set_fine(self):
        if self.status == "professor":
            self.fine = 1000

        elif self.status == "student":
            self.fine = 1500

        elif self.status == "guest":
            self.fine = 3500
