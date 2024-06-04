from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mountain
from .serializers import MountainSerializer
import random

@api_view(['GET'])
def mountain_quiz(request):
    mountains = list(Mountain.objects.exclude(image=''))
    correct_mountain = random.choice(mountains)
    other_mountains = random.sample([m for m in mountains if m != correct_mountain], 3)
    choices = other_mountains + [correct_mountain]
    random.shuffle(choices)

    data = {
        'image': correct_mountain.image.url,
        'correct_answer': correct_mountain.name,
        'options': [mountain.name for mountain in choices],
        'height': correct_mountain.height,
        'region': correct_mountain.region,
        'group': correct_mountain.group,
    }
    return Response(data)