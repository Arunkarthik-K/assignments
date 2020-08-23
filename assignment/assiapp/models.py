from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User,Group
from datetime import datetime, timedelta
    

CATEGORIES = (
    ('TRA', 'Travel'),
    ('MISC', 'Misc'),
    ('FOOD', 'Food'),
    ('ACCO', 'Accommodation'),
    ('TRAI', 'Training'),
    ('CERT', 'Certificate'),
    ('SP', 'Software Purchase'),
)        

STATUS = (
    ('PEND', 'Pending'),
    ('APPR', 'Approved'),
    ('REJ', 'Rejected'),
)

class ExpenseModel(models.Model):
    Title = models.CharField(max_length=64)        
    Description = models.CharField(max_length=255)
    Amount = models.FloatField(validators=[validators.MaxValueValidator(10000)])
    Categories = models.CharField(max_length=5,choices=CATEGORIES)
    Trans_Date = models.DateField()
    Image = models.ImageField(max_length=100)
    Status = models.CharField(max_length=5, choices=STATUS, default="Pending")
    Emp = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_of_Sub = models.DateField(default=datetime.now())

    def clean(self):
        if self.Categories == "TRA":
            if self.Amount > 7500:
                raise ValidationError("Amount should be less or equal to 7500 "+ self.Categories) 
                if self.Trans_Date > self.Date_of_Sub:
                    raise ValidationError("Trans_Date should not be future")
                elif self.Trans_Date < (self.Date_of_Sub - timedelta(days=90)):
                    raise ValidationError("Trans_Date should not be older than 3 months")
            elif self.Trans_Date > self.Date_of_Sub:
                raise ValidationError("Trans_Date should not be future")   
            elif self.Trans_Date < (self.Date_of_Sub - timedelta(days=90)):
                raise ValidationError("Trans_Date should not be older than 3 months")            
        elif self.Categories == "MISC":
            if self.Amount > 1500:
                raise ValidationError("Amount should be less or equal to 1500 "+ self.Categories)
                if self.Trans_Date > self.Date_of_Sub:
                    raise ValidationError("Trans_Date should not be future")
                elif self.Trans_Date < (self.Date_of_Sub - timedelta(days=90)):
                    raise ValidationError("Trans_Date should not be older than 3 months")
            elif self.Trans_Date > self.Date_of_Sub:
                raise ValidationError("Trans_Date should not be future")   
            elif self.Trans_Date < (self.Date_of_Sub - timedelta(days=90)):
                raise ValidationError("Trans_Date should not be older than 3 months")
        elif self.Trans_Date > self.Date_of_Sub:
            raise ValidationError("Trans_Date should not be future")   
        elif self.Trans_Date < (self.Date_of_Sub - timedelta(days=90)):
            raise ValidationError("Trans_Date should not be older than 3 months")

    class Meta:
        db_table="expense"   
      


