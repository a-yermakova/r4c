from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from robots.models import Robot
from robots.service import generate_excel_report


@csrf_exempt
@require_GET
def get_report(request: HttpRequest) -> HttpResponse:
    """
    API endpoint for downloading a weekly report in Excel format.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: An HTTP response indicating success or failure.
    """
    try:
        # Получаем данные из БД
        data = Robot.get_weekly_summary()

        # Генерируем Excel-файл
        excel_file = generate_excel_report(data)

        # Формируем HTTP-ответ с файлом
        response = HttpResponse(
            excel_file,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="Weekly report.xlsx"'
        return response
    except Exception as e:
        return HttpResponse(f"Ошибка при создании отчета: {str(e)}", status=500)