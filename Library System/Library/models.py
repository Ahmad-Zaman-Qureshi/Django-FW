from django.db import models
class Book_Issue(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(default=get_returndate())
    remarks = models.CharField(max_length=100, default="Some Remarks")
    def _str_(self):
        return self.Students.std_name + " borrowed " + self.Book.book_title
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.IntegerField(max_length=1000)
    def _str_(self):
        return self.book_title
class Students(models.Model):
    std_rn = models.CharField(max_length=100)
    std_name = models.CharField(max_length=100)
    std_address = models.CharField(max_length=100)
    std_study_pro = models.CharField(max_length=100)
    def _str_(self):
        return self.std_name
    def _str_(self):
        return str(self.std_rn)