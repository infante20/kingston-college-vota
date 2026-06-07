# Tiempo de Calidad — ebook KDP de actividades sin pantallas

Guía/compendio de **+48 actividades lúdico-didácticas** para hacer con niños en casa,
pensada para **reducir el tiempo de pantallas** y generar tiempo de calidad en familia.
Las actividades están organizadas **por rango de edad** (0–2, 3–5, 6–8, 9–12) y, dentro de
cada edad, **por tipo** (experimentos, sensoriales, recreativas, juegos, conexión emocional,
arte y naturaleza). Cada actividad indica materiales del hogar, preparación, pasos,
**dificultad** (preparación y materiales), **duración** y una ilustración de guía.

El proyecto genera dos archivos listos para **Kindle Direct Publishing (KDP)**:

- `dist/Tiempo-de-Calidad.pdf` — PDF maquetado a 8.5×11 in (tapa blanda / interior).
- `dist/Tiempo-de-Calidad.epub` — EPUB3 reflujable para Kindle (válido con epubcheck).

## Cómo construir

```bash
pip install -r requirements.txt        # dependencias (jinja2, weasyprint, pandoc, …)
python scripts/gen_icons.py            # (una vez) iconos SVG de tipos y reloj
python scripts/build_images.py         # ilustraciones SVG (portada, separadores, 48 heroes)
python scripts/build.py                # -> dist/*.pdf y dist/*.epub
```

`python scripts/build.py --html` genera solo `dist/book.html` (rápido para iterar la maquetación).

## Estructura

```
data/
  book.yaml              # título, autor, trim, paleta, tipos, intros por edad, leyenda, textos
  activities/*.yaml      # una actividad por archivo (48). Ver el esquema más abajo.
templates/book.html.j2   # plantilla Jinja2 del libro completo
styles/print.css         # maquetación de impresión (PDF, paged media)
styles/epub.css          # estilos reflujables (EPUB)
assets/icons/*.svg       # iconos de tipo + reloj (generados)
assets/images/*.svg      # portada, separadores y heroes por actividad (generados)
assets/fonts/*.woff2     # Fraunces + Source Sans 3 (incrustadas en el PDF)
scripts/                 # gen_icons.py, build_images.py, build.py
dist/                    # SALIDAS: PDF y EPUB
```

## Editar el contenido

- **Título, autor, tamaño de página, textos e introducciones:** `data/book.yaml`
  (cambia `meta.autor` por tu nombre, `meta.titulo`, etc.).
- **Una actividad:** edita su archivo en `data/activities/`. Esquema:

  ```yaml
  id: "3a5-01"          # identificador único (también nombre de su imagen)
  orden: 1              # orden dentro del rango de edad
  edad: "3-5"           # 0-2 | 3-5 | 6-8 | 9-12
  tipo: experimento     # experimento|sensorial|recreativa|juego|emocional|arte|naturaleza
  titulo: "..."
  gancho: "..."         # frase de enganche
  duracion: "20-30 min"
  dif_prep: 2           # 1=baja, 2=media, 3=alta
  dif_materiales: 2     # 1=mínimos, 2=pocos, 3=varios
  materiales: ["...", "..."]
  preparacion: "..."
  pasos: ["...", "..."]
  aprendizaje: "..."
  variantes: "..."      # opcional
  seguridad: "..."      # opcional
  imagen: "3a5-01.png"  # = "<id>.png"
  ```

  Tras editar, vuelve a ejecutar `python scripts/build.py`.

## Imágenes

Las ilustraciones son **vectoriales (SVG)** generadas por código en `assets/images/`,
para que el libro sea reproducible sin depender de servicios externos. Son consistentes
con la paleta y el tipo de cada actividad.

Para **sustituir** cualquier ilustración por una propia (foto o arte), coloca un PNG/JPG con
el mismo nombre base en `assets/images/`:

- Actividad: `assets/images/<id>.png`  (p. ej. `3a5-01.png`)
- Portada:   `assets/images/portada.png`
- Separador: `assets/images/sep-3-5.png`

El build prefiere `.png`/`.jpg` sobre `.svg`, así que tu imagen tiene prioridad
automáticamente. Vuelve a ejecutar `python scripts/build.py`.

### Plan de imágenes en Canva

`docs/canva-plan.md` contiene la guía de estilo y un **prompt por cada actividad**,
portada y separadores, listo para generar las ilustraciones en Canva. Se regenera con
`python scripts/gen_canva_plan.py` (usa los títulos actuales). Para ejecutar el flujo
completo de Canva (generar → exportar → descargar a `assets/images/<id>.png`) se
necesita un entorno con **acceso de red Completo** o **Personalizado** incluyendo
`*.canva.com`; la política **Confiable** por defecto bloquea la CDN de Canva.

### Generar imágenes con Together AI (FLUX)

Alternativa 100% automatizable a Canva: `scripts/gen_images_together.py` genera
portada, separadores y las 48 ilustraciones llamando a la API de imágenes de
Together (modelos FLUX) y guardándolas en `assets/images/<id>.png`. Pide las
imágenes en base64 por `api.together.xyz`, sin depender de CDNs externas.

Requisitos: entorno con acceso de red a `api.together.xyz` (política **Completa**
o **Custom** con `api.together.xyz`) y la variable **`TOGETHER_API_KEY`**.

```bash
export TOGETHER_API_KEY=...          # tu clave de Together
python scripts/gen_images_together.py --build   # genera lo que falte y reconstruye
# opciones: --force (regenerar todo) · --only portada,0a2-01 · --limit 3 · --model <flux>
```

Los prompts viven en `scripts/prompts.py` (compartidos con el plan de Canva).

## Notas para KDP

- **Interior:** sube `dist/Tiempo-de-Calidad.pdf`. Tamaño 8.5×11 in. Ajusta los
  márgenes/sangrado en `styles/print.css` (`@page`) según el recuento de páginas que exija KDP.
- **Ebook Kindle:** sube `dist/Tiempo-de-Calidad.epub` (EPUB3 válido).
- **Portada de venta:** KDP pide una portada aparte; puedes exportar la portada de este
  proyecto o crear una propia y colocarla como `assets/images/portada.png`.
- Recuerda completar `meta.autor` (y, si aplica, `meta.isbn`) en `data/book.yaml`.
