from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
import markdown
from .models import Post, Notice


class ZPaginator(Paginator):
    def __init__(self, current_page, object_list_all, perpage_post_num):
        self.current_page = current_page
        super(ZPaginator, self).__init__(object_list_all, perpage_post_num)
        self.object_list = Paginator.page(self, self.current_page)

    def previous_num(self):
        return self.object_list.previous_page_number() if self.object_list.has_previous() else self.current_page

    def next_num(self):
        return self.object_list.next_page_number() if self.object_list.has_next() else self.current_page

    def pagerange_disp(self):
        pagerange = [-1] * 9
        if 1 <= self.current_page <= 4:
            # 当前页面也1到4之间
            if self.num_pages <= self.current_page + 4:
                # 当前总页数小于等于self.current_page + 4页，显示所有页面索引
                for i in range(0, self.num_pages):
                    pagerange[i] = i + 1
            else:
                # 当前总页数超过self.current_page + 4页，显示部分页面索引
                for i in range(0, self.current_page + 4):
                    pagerange[i] = i + 1
                pagerange[self.current_page + 2] = 0
                pagerange[self.current_page + 3] = self.num_pages
        elif self.num_pages - 3 <= self.current_page <= self.num_pages:
            # 总页数超过5页，且当前页面在索引末尾
            pagerange_num = self.num_pages - self.current_page + 5
            for i in range(0, pagerange_num):
                pagerange[i] = self.num_pages - 4 + i
            pagerange[1] = 0
            pagerange[0] = 1
        else:
            # 不满足前两种情况
            for i in range(0, 9):
                pagerange[i] = self.current_page + i - 4
            pagerange[0], pagerange[1], pagerange[7], pagerange[8] = 1, 0, 0, self.num_pages

        while pagerange[-1] == -1:
            pagerange.pop()
        return pagerange


def index(request):
    return render(request, 'index.html', context={})


def gallery(request):
    post_list_all = Post.objects.all()
    current_page = request.GET.get('page', 1)
    # 每页展示六项内容
    paginator = ZPaginator(int(current_page), post_list_all, 6)

    return render(request, 'gallery.html', context={
        'paginator': paginator,
    })


def article(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.increase_views()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'article.html', context={'post': post})


def notice_page(request):
    notice_list_all = Notice.objects.all()
    current_page = request.GET.get('page', 1)
    # 每页展示六项内容
    paginator = ZPaginator(int(current_page), notice_list_all, 10)

    return render(request, 'notice.html', context={
        'paginator': paginator,
    })
