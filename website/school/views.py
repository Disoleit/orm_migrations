from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.all().order_by(ordering)
    context = {'object_list': students}
    print("\n=== Список учеников с учителями ===")
    for student in students:
        print(f"\nУченик: {student.name} ({student.group})")
        print("Преподаватели:")
        for teacher in student.teachers.all():
            print(f"- {teacher.name} ({teacher.subject})")
        if not student.teachers.exists():
            print("- Нет преподавателей")

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    # prefetch_related('teachers')

    return render(request, template, context)
