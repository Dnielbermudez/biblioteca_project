from biblioteca.models import Autor, Libro, Resena
from datetime import date

# Crear más autores
a1 = Autor.objects.create(nombre="Lee Child", nacionalidad="Reino Unido")
a2 = Autor.objects.create(nombre="Clive Cussler", nacionalidad="Estados Unidos")
a3 = Autor.objects.create(nombre="Agatha Christie", nacionalidad="Reino Unido")
a4 = Autor.objects.create(nombre="Stephen King", nacionalidad="Estados Unidos")
a5 = Autor.objects.create(nombre="J.K. Rowling", nacionalidad="Reino Unido")
a6 = Autor.objects.create(nombre="Paulo Coelho", nacionalidad="Brasil")

# Crear más libros
l1 = Libro.objects.create(
    titulo="Zona Peligrosa",
    autor=a1,
    fecha_publicacion=date(1997, 6, 1),
    resumen="Un ex-militar se enfrenta a una conspiración peligrosa que amenaza su vida y la de muchos."
)

l2 = Libro.objects.create(
    titulo="El Imperio Perdido",
    autor=a2,
    fecha_publicacion=date(2006, 3, 15),
    resumen="Una expedición descubre secretos enterrados durante siglos, desatando una carrera por la supervivencia."
)

l3 = Libro.objects.create(
    titulo="Asesinato en el Expreso de Oriente",
    autor=a3,
    fecha_publicacion=date(1934, 1, 1),
    resumen="Un detective belga investiga un misterioso asesinato en un tren de lujo."
)

l4 = Libro.objects.create(
    titulo="El Resplandor",
    autor=a4,
    fecha_publicacion=date(1977, 5, 28),
    resumen="Una familia se aísla en un hotel embrujado durante el invierno, enfrentando horrores indescriptibles."
)

l5 = Libro.objects.create(
    titulo="Harry Potter y la Piedra Filosofal",
    autor=a5,
    fecha_publicacion=date(1997, 6, 26),
    resumen="Un joven mago descubre su verdadero origen y comienza su aventura en una escuela mágica."
)

l6 = Libro.objects.create(
    titulo="El Alquimista",
    autor=a6,
    fecha_publicacion=date(1988, 1, 1),
    resumen="Un viaje de autodescubrimiento a través del desierto en busca de un tesoro personal."
)

# Crear más reseñas
Resena.objects.create(libro=l1, texto="Muy buen ritmo y acción constante.", calificacion=5)
Resena.objects.create(libro=l1, texto="Algo predecible pero entretenido.", calificacion=4)
Resena.objects.create(libro=l1, texto="Excelente thriller, no puedo parar de leer.", calificacion=5)

Resena.objects.create(libro=l2, texto="Clive Cussler nunca decepciona.", calificacion=5)
Resena.objects.create(libro=l2, texto="Aventura emocionante de principio a fin.", calificacion=4)

Resena.objects.create(libro=l3, texto="Un clásico del misterio insuperable.", calificacion=5)
Resena.objects.create(libro=l3, texto="Brillante giro final, muy recomendado.", calificacion=5)
Resena.objects.create(libro=l3, texto="Algo lento en las primeras páginas.", calificacion=3)

Resena.objects.create(libro=l4, texto="Aterrador y cautivador, obra maestra.", calificacion=5)
Resena.objects.create(libro=l4, texto="Psicológicamente inquietante, excelente.", calificacion=5)

Resena.objects.create(libro=l5, texto="Perfecto para todas las edades, adictivo.", calificacion=5)
Resena.objects.create(libro=l5, texto="Inicio perfecto de una saga legendaria.", calificacion=5)
Resena.objects.create(libro=l5, texto="Imaginación sin límites.", calificacion=4)

Resena.objects.create(libro=l6, texto="Inspirador y reflexivo, vida cambiante.", calificacion=5)
Resena.objects.create(libro=l6, texto="Profundo mensaje sobre el destino.", calificacion=4)