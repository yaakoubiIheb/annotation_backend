import json
from django.http import JsonResponse
from ..models import Document
from ..models import Annotation
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def annotation_view(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            document_text = json_data.get('document')
            annotations = json_data.get('annotations')

            
            document = Document.objects.create(text=document_text)

            
            for annotation_data in annotations:
                start = annotation_data.get('start')
                end = annotation_data.get('end')
                label = annotation_data.get('label')
                text = annotation_data.get('text')
                Annotation.objects.create(document_id=document.pk, start=start, end=end, label=label, text=text)

            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)