from django import forms
from .models import ExpenseModel

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

class ExpenseForm(forms.ModelForm):
    Categories = forms.ChoiceField(choices=CATEGORIES)
    Status = forms.ChoiceField(choices=STATUS)
    

