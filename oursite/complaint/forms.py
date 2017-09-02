from django import forms

class ComplaintForm(forms.Form):
    title = forms.CharField(label="Complaint Title",max_length=140)
    DEPT_CHOICES = (
        (1,'ELECTRICAL'),
        (2, 'WATER'),
        (3, 'WASTE'),
    )
    LOC_CHOICES = (
        ('23','SECTOR 23'),
        ('22','SECTOR 22'),
        ('14','SECTOR 14'),
    )
    dept = forms.ChoiceField(label="Choose Department",required=True,choices=DEPT_CHOICES)
    location = forms.ChoiceField(label="Choose Location",choices=LOC_CHOICES)
    severity = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    solution = forms.CharField(widget=forms.Textarea)

