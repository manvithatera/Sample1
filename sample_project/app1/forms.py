from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    employee_name = forms.CharField(label='',
                                    widget=forms.TextInput(attrs={
                                        "placeholder": "your name",
                                    }))
    salary = forms.DecimalField(initial=10000.99)
    address = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={
                                  "placeholder": "your designation",
                                  "rows": 10,
                                  "cols": 40,
                              }))
    class Meta:
        model = Employee
        fields = [
            'employee_name',
            'designation',
            'salary',
        ]
    #validation
    # def clean_employee_name(self,*args, **kwargs):
    #     employee_name = self.cleaned_data.get("employee_name")
    #     if  not 'a'in employee_name:
    #         # return employee_name
    #     # else:
    #         raise forms.ValidationError('not valid')
    #     return employee_name




#pure django forms
class RawEMployeeForm(forms.Form):
    employee_name = forms.CharField(label='',
                                    widget=forms.TextInput(attrs={
                                        "placeholder":"your name",
                                    }))
    designation = forms.CharField()
    salary = forms.DecimalField(initial=10000.99)
    address = forms.CharField(required=False,
                              widget= forms.Textarea(attrs={
                                  "placeholder": "your designation",
                                  "rows":10,
                                  "cols":40,
                              }))







