from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.views import Response

from django.contrib.auth import get_user_model

from prestamos.models import Prestamos
from mantenedor.models import Producto

from django.core.urlresolvers import reverse_lazy
from reportlab.platypus import TableStyle, Table, Spacer, Paragraph, Image
from reportlab.lib import colors
from reportlab.lib.units import cm
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.views.generic import View
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from django.db.models import Avg, Max, Min, Sum, Count
from django.http import HttpResponse



# Create your views here.


User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'reportes/charts.html', {"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_clases = []

    def get(self, request, format=None):
        #qs_count1 =User.objects.all().count()
        #qs_count2 = Prestamos.objects.all().count()
        inner_qs = Prestamos.objects.filter(estado=1).values('id_producto_id')
        pro_dis = Producto.objects.exclude(id__in=inner_qs).filter(estado=1).count()
        pro_ocu = Producto.objects.filter(id__in=inner_qs, estado=1).count()
        # inner = Prestamos.objects.values('id_producto_id')
        # inner2 = Producto.objects.values('id')
        # inner3 = Producto.objects.values('codigo')
        # total = Producto.objects.values('codigo', inner).count()
        # variable = Producto.objects.values('codigo', inner).count().filter(inner=inner2).annotate(inner, inner3).order_by(total)[:1]

        # var1 = Prestamos.objects.values('id_producto_id__codigo')
        # inner = var1.Count('id_producto_id').latest()
        # #inner = v.latest('max')

        labels = ["Productos Disponibles", "Productos En Prestamos"]
        default_items = [pro_dis, pro_ocu]
        data = {
                "labels": labels,
                "default": default_items
        }
        return Response(data)


class Reporte(View):

    def cabecera(self, pdf):
        #imagen = settings.MEDIA_ROOT+'link de la imagen.jpg'
        #pdf.drawImage(imagen, 40, 520, 120, 90, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(300, 550, u"REPORTE DE PRESTAMO")
        pdf.setFont("Helvetica", 10)
        #pdf.drawString(200, 770, u"")

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition']='attachment; filename="%s"'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 420
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.setLineWidth(0.1)
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezados = ('Nombre del Docente', 'Nombre Equipo', 'Fecha Prestamo', 'Fecha Devolucion Prestamo', 'Detalle')

        detalles = [(Prestamos.id_usuario, Prestamos.id_producto, Prestamos.fecha_prestamo, Prestamos.fecha_devolucion, Prestamos.observaciones)
                    for Prestamos in Prestamos.objects.all()]
        detalle_orden = Table([encabezados] + detalles, colWidths=[3* cm, 2* cm, 5* cm, 5* cm, 10* cm])
        detalle_orden.setStyle(TableStyle(
            [
            ('ALIGN',(0,0),(1,0),'CENTER'),
            ('GRID', (0, 0), (8, -1), 0.5, colors.darkgrey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
        ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 40, -100)
        pdf.setPageSize(landscape(letter))

    template_name = 'reportes/reportes_prestamo.html'
    success_url = reverse_lazy('reportes:hom')


class ReporteActivo(View):

    def cabecera(self, pdf):
        #imagen = settings.MEDIA_ROOT+'link de la imagen.jpg'
        #pdf.drawImage(imagen, 40, 520, 120, 90, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(180, 550, u"REPORTE DE PRESTAMOS ACTIVOS")
        pdf.setFont("Helvetica", 10)
        #pdf.drawString(200, 770, u"")

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition']='attachment; filename="%s"'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.setLineWidth(0.1)
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezados = ('Nombre del Docente', 'Nombre Equipo', 'Fecha Prestamo', 'Fecha Devolucion Prestamo', 'Detalle')

        detalles = [(Prestamos.id_usuario, Prestamos.id_producto, Prestamos.fecha_prestamo, Prestamos.fecha_devolucion, Prestamos.observaciones)
                    for Prestamos in Prestamos.objects.filter(estado=1)]
        detalle_orden = Table([encabezados] + detalles, colWidths=[3* cm, 2* cm, 5* cm, 5* cm, 10* cm])
        detalle_orden.setStyle(TableStyle(
            [
            ('ALIGN',(0,0),(1,0),'CENTER'),
            ('GRID', (0, 0), (8, -1), 0.5, colors.darkgrey),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
        ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 40, 450)
        pdf.setPageSize(landscape(letter))

    template_name = 'reportes/prestamos_activos.html'
    success_url = reverse_lazy('reportes:hom')

# def report_pdf(request):
#     #create the httpresponse headers with pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=report.pdf'
#     #create the pdf object, using the ByteIO as its file
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer, pagesize=A4)
#
#     #header
#     c.setLineWidth(.3)
#     c.setFont('Helvetica', 22)
#     c.drawString(30, 750, 'Platzi')
#     c.setFont('Helvetica', 12)
#     c.drawString(30, 735, 'Report')
#
#     c.setFont('Helvetica-Bold', 12)
#     c.drawString(480, 750, '01/07/2018')
#     #start x, heigth end y, heigth
#     c.line(480, 747, 560, 747)
#
#     # Table header
#     styles = getSampleStyleSheet()
#     styleBH = styles["Normal"]
#     styleBH.aligment = TA_CENTER
#     styleBH.fontSize = 10
#
#     numero = Paragraph('''No.''', styleBH)
#     alumno = Paragraph('''Alumno''', styleBH)
#     b1 = Paragraph('''BIM1''', styleBH)
#     b2 = Paragraph('''BIM2''', styleBH)
#     b3 = Paragraph('''BIM3''', styleBH)
#     total = Paragraph('''TOTAL''', styleBH)
#     data = [(numero, alumno, b1, b2, b3, total)]
#
#     # Students table
#     students = [{'#': '1', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '2', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '3', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '4', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '5', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '6', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '7', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '8', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '9', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '10', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '2', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '3', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '4', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '5', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '6', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '7', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '8', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '9', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '10', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '2', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '3', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '4', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '5', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '6', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '7', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '8', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '9', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '10', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '2', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '3', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '4', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '5', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '6', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '7', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '8', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '9', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '10', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '2', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '3', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '4', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '5', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '6', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '7', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '8', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '9', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 {'#': '10', 'Name': 'Gonzalo', 'b1': '3.4', 'b2': '2.2', 'b3': '3.3', 'total': '3.19'},
#                 ]
#
#     styles = getSampleStyleSheet()
#     styleN = styles["BodyText"]
#     styleN.aligment = TA_CENTER
#     styleN.fontSize = 7
#
#     width, height = A4
#     high = 650
#     for student in students:
#         this_student = [student['#'], student['Name'], student['b1'], student['b2'], student['b3'], student['total']]
#         data.append(this_student)
#         high = high - 18
#
#     # Table size
#     table = Table(data, colWidths=[1.9 * cm, 9.5 * cm, 1.9 * cm, 1.9 * cm, 1.9 * cm, 1.9 * cm])
#     table.setStyle(TableStyle([
#         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#         ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))
#
#     # pdf size
#     table.wrapOn(c, width, height)
#     table.drawOn(c, 30, high)
#     c.showPage() #save page
#
#     #save pdf
#     c.save()
#     # get the value of BytesIO buffer and write response
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

# def reports(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=report.pdf'
#     buffer = BytesIO()
#     pdf = canvas.Canvas(buffer)
#     pdf.setFont("Helvetica", 16)
#     pdf.drawString(180, 780, u"SISTEMA DE PRESTAMOS")
#     pdf.setFont("Helvetica", 12)
#     pdf.drawString(250, 760, u"Reporte De Prestamos Activos")
#     #archivo_imagen = settings.MEDIA_ROOT + '/imagenes/espacioPDF.png'
#     #pdf.drawImage(archivo_imagen, 55, 735, 500, 10, preserveAspectRatio=False)
#     #archivo_imagen = settings.MEDIA_ROOT + '/imagenes/informe.png'
#     #pdf.drawImage(archivo_imagen, 20, 750, 120, 60, preserveAspectRatio=True)
#     pdf.translate(60, 520)
#     encabezados = ('Nombre Docente', 'Producto', 'Fecha Prestamo', 'Fecha Devolucion', 'Detalle')
#     detalles = [
#         (tramite.id_usuario, tramite.id_producto, tramite.fecha_prestamo, tramite.fecha_devolucion, tramite.observaciones)
#         for tramite in
#         Prestamos.objects.filter(estado=1)]
#     detalle_orden = Table([encabezados] + detalles, colWidths=[3 * cm, 2 * cm, 5 * cm, 5 * cm, 10 * cm])
#     detalle_orden.setStyle(TableStyle(
#         [
#             ('ALIGN', (0, 0), (0, 0), 'CENTER'),
#             ('GRID', (0, 0), (8, -1), 1, colors.gray),
#             ('FONTSIZE', (0, 0), (-1, -1), 8),
#             ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
#             ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
#             ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#         ]
#     ))
#     detalle_orden.wrapOn(pdf, 800, 600)
#     detalle_orden.drawOn(pdf, 0, 0)
#     pdf.showPage()
#     pdf.save()
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

