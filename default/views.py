from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

# Create your views here.
def poll_list(req):
    polls = Poll.objects.all()
    return render(req, "defult/list.html", {'poll_list':polls, 'msg': 'Hello!'})

class PollList(ListView):
    model = Poll
    #listView撈出一堆紀錄，產生清單頁面


class PollView(DetailView):
    model = Poll
     #default/Poll_detail.html
    #從PK取值處理

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['option_list'] = Option.objects.filter(poll_id=self.object.id)

        return ctx
    
class PollVote(RedirectView):
    def get_redirect_url(self, request, *args, **kwargs):
        option = Option.objects.get(id = self.kwargs['oid'])
        option.votes += 1  
        option.save()
        #return "/poll/{}/".format(option.poll_id) 
        #return f"/poll/{option.poll_id}"  
        #return reverse('poll_view', args=[option.poll_id])(直接一個一個填)
        return reverse('poll_view', kwargs={'pk': option.poll_id}) #(參數位置有可能調整但名稱不會動)
   
class PollCreate(CreateView):
    model = Poll
    fields = '__all__' #可以用方括號輸入想要顯示的
    success_url = reserve_lazy('poll_list')

class PollEdit(UpdateView):
    model = Poll
    fields = '__all__' #可以用方括號輸入想要顯示的

class OptionCreate(CreateView):
    model = Option
    fielss = ['title']

    def for_valid(self, form):
        form.instance.poll_id = self.kwargs['pid']
        return super (). form_valid(form)
        

    def getsucess_url(self):
        return reserve_lazy('poll_view', kwargs={'pk':self.object.id})
class OptionEdit
    model = Option
    fields = ['title']
    pk_url_kwargs = 'oid'

    def get_success_url(self):
        return reverse_lazy('poll_view'kwargs={'pk': self.object,poll.id})
