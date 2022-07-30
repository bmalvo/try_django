from email import contentmanager
from socket import fromshare
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data  # dictionary
    #     print('cleaned_data', cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'ninja':
    #         raise forms.ValidationError('This title is taken.')
    #     print('title', title)
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'ninja':
            self.add_error('title', 'This title is taken')
            raise forms.ValidationError('This title is taken.')
        if 'ninja' in content or 'ninja' in title.lower():
            self.add_error('content', 'ninja can not be in content')
            raise forms.ValidationError('ninja is not allowed')
        return cleaned_data
