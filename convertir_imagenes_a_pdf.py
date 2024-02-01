from reportlab.pdfgen import canvas
from PIL import Image

def redimensionar_imagen(imagen, ancho_max, alto_max):
    # Escalar proporcionalmente la imagen para que encaje dentro de los límites dados
    ancho_original, alto_original = imagen.size
    proporcion = min(ancho_max / ancho_original, alto_max / alto_original)
    nuevo_ancho = int(ancho_original * proporcion)
    nuevo_alto = int(alto_original * proporcion)
    return imagen.resize((nuevo_ancho, nuevo_alto), 3)  # 3 corresponde a Image.ANTIALIAS

def convertir_imagenes_a_pdf(rutas_imagenes, ruta_pdf):
    # Crear un archivo PDF con tamaño A4
    pdf = canvas.Canvas(ruta_pdf, pagesize=(210, 297))

    for ruta_imagen in rutas_imagenes:
        # Abrir cada imagen
        imagen = Image.open(ruta_imagen)

        # Redimensionar la imagen para que encaje en la página A4
        imagen_redimensionada = redimensionar_imagen(imagen, 210, 297)

        # Obtener las coordenadas para centrar la imagen en la página
        x = (210 - imagen_redimensionada.width) / 2
        y = (297 - imagen_redimensionada.height) / 2

        # Añadir la imagen al PDF
        pdf.drawInlineImage(imagen_redimensionada, x, y)

        pdf.showPage()  # Cambiar a una nueva página para la siguiente imagen

    # Guardar el PDF
    pdf.save()

if __name__ == "__main__":
    # Lista de rutas de las imágenes
    rutas_imagenes = [
        r"C:\Users\usuario\Pictures\Saved Pictures\goku.jpg",
        r"C:\Users\usuario\Pictures\Saved Pictures\gato.jpeg",
        # Agrega más rutas según sea necesario
    ]

    # Ruta del PDF resultante
    ruta_pdf = r"C:\resultado\resultado_multiples_imagenes.pdf"

    # Llamar a la función para convertir las imágenes a PDF
    convertir_imagenes_a_pdf(rutas_imagenes, ruta_pdf)

    print(f"La conversión se ha completado. PDF creado en: {ruta_pdf}")
