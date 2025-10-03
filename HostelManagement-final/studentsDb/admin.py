from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Complaint
from django.forms import PasswordInput

# Custom form for Student model
class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'password': PasswordInput(render_value=True),  # show password on edit
        }

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm  # use the custom form

    list_display = ('username', 'room_no', 'fee_status', 'student_actions')
    list_filter = ('fee_status', 'room_no')
    search_fields = ('username', 'first_name')

    fieldsets = (
        ('Personal Info', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'father_name', 'age', 'email', 'address', 'image',)
        }),
        ('Hostel Details', {
            'fields': ('room_no', 'fee_status', 'fee')
        }),
    )

    def student_actions(self, obj):
        return format_html(
            '<a class="button" href="/admin/studentsDb/student/{}/change/">Edit</a>', 
            obj.id
        )
    student_actions.short_description = "Actions"




@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('Full_Name', 'Room_Number', 'Complaint_Type', 'resolved')
    list_filter = ('resolved', 'Complaint_Type')
    search_fields = ('Full_Name', 'Room_Number', 'Complaint_Details')