class Report:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def write_report(self, text):
        return "{} By: {} \n {}".format(self.title, self.author, text)
    
my_report = Report("I should of studied art", "Derrick")

print(my_report.write_report("This is OOP"))