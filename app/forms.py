from django import forms

from app.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
