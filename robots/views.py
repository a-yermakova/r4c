from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpRequest
from .models import Robot
from .schemas import RobotInput
import json
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from .service import generate_excel_report


@csrf_exempt
@require_POST
def create_robot(request: HttpRequest) -> HttpResponse:
    """
    API endpoint for creating a new robot entry in the database.

    Args:
        request (HttpRequest): The HTTP request object containing the JSON payload.

    Returns:
        HttpResponse: A JSON response indicating success or failure.
    """
    try:
        data = json.loads(request.body)
        validated_data = RobotInput(**data)
        robot = Robot.create_robot(
            validated_data.model,
            validated_data.version,
            validated_data.created.isoformat()
        )
        return JsonResponse({
            'robot': {
                'serial': robot.serial,
                'model': robot.model,
                'version': robot.version,
                'created': robot.created,
            }
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
