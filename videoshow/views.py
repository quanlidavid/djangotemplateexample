from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime
from django.http import HttpResponse


# Create your views here.
def index(request, tvno='0'):
    tv_list = [
        {'name': '卡卡', 'tvcode': 'XMzA3ODcyMTA4MA=='},
        {'name': '小罗', 'tvcode': 'XMTU5OTM2MTc1Mg=='},
        {'name': '梅西', 'tvcode': 'XNzQzMTY4NjA4'},
    ]
    template = get_template('index.html')
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    html = template.render(locals())
    return HttpResponse(html)
