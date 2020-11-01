from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from posts.models import Post


class PostView(TemplateView):
    template_name = "post.html"

    def get_object(self, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise ValueError("Have not this post")
        return post

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["post"] = self.get_object(id=kwargs.get("postID"))
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # {"action": ["like_post"]}
        return {"like_post": self._like_post, "dislike_post": self._dislike_post}.get(
            request.POST.get("action")
        )(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def _like_post(self, request, **kwargs):
        # TODO: обработать 2-й клик на лайк, т.е. убрать лайк
        post = Post.objects.get(id=id)
        post.likes.add(request.user)
        post.save()
        context = {"obj": post}
        return HttpResponse(
            render_to_string("components/post_like_row.html", context=context)
        )

    def _dislike_post(self, request, **kwargs):
        pass
