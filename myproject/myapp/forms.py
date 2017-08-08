# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a image',
        help_text='上传图片后请不要刷新页面/F5。。。。=_=|||',
    )
