from django.http import JsonResponse
from django.db.models import Q
from Blog.models import content


def extract_snippet(text, keyword, chars=10):
    index = text.lower().find(keyword.lower())
    if index != -1:
        start = max(index - chars, 0)
        end = min(index + len(keyword) + chars, len(text))
        return text[start:end]
    return ""

def search(request):
    query = request.GET.get('q', '')
    if query:
        results = content.objects.filter(
            #要搜尋的內容
            Q(postname__icontains=query) |
            Q(introduction__icontains=query) |
            Q(writer__icontains=query)
        ).distinct()[:10]  # 限制结果数量
        data = []
        for result in results:
            snippet = extract_snippet(result.introduction, query)
            print(snippet)
            data.append({
                #要傳送到前端顯示的內容
                'postname': result.postname,
                'snippet': snippet,
                'writer': result.writer,
                'post_date': result.post_date,
            })

        return JsonResponse(data, safe=False)
    return JsonResponse([])
