from django import forms

class ComplaintForm(forms.Form):
    title = forms.CharField(label="Complaint Title",max_length=140)
    DEPT_CHOICES = (
        ('1','ELECTRICAL'),
        ('2', 'WATER'),
        ('3', 'WASTE'),
    )
    LOC_CHOICES = (
        ('23','SECTOR 23'),
        ('22','SECTOR 22'),
        ('14','SECTOR 14'),
    )
    dept = forms.CharField(label="Choose Department",required=True,widget=forms.Select(choices = DEPT_CHOICES))
    location = forms.CharField(label="Choose Location",widget=forms.Select(choices=LOC_CHOICES))
    severity = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    solution = forms.CharField(widget=forms.Textarea)