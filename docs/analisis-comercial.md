# Análisis comercial — *Tiempo de Calidad*

> Auditoría honesta del proyecto como **producto a vender** (no como archivo). Qué estás
> haciendo mal, qué mejorar, qué quitar y qué incorporar para que tenga éxito en el mercado.
> Fecha: 2026-06. Basado en el estado actual del repo + datos de mercado KDP 2025-2026.

---

## Veredicto en 30 segundos

Tienes un **producto sólido y diferenciable** (español neutro/chileno + ciencia/STEM en casa +
sin pantallas + por edad). El contenido es bueno y abundante. Pero hay **3 cosas que pueden
hundirlo comercialmente** si no se corrigen antes de publicar:

1. **Economía de impresión:** 233 páginas a todo color en 8.5×11 es carísimo de imprimir →
   te obliga a un precio no competitivo, o a regalar tu margen.
2. **Cumplimiento KDP:** las imágenes son IA (hay que **declararlo** sí o sí) y el PDF no está
   bien preparado para imprenta (sangrado) → riesgo de **rechazo o suspensión de cuenta**.
3. **Posicionamiento:** título genérico, sin nicho/edad/keywords ni estrategia de serie →
   invisible entre ~50.000 "kids activity books".

Lo bueno: las tres son arreglables, y tu ángulo (ciencia en español por edad) es justo el tipo
de **nicho específico** que sí funciona hoy.

---

## 1. Lo que estás haciendo MAL (riesgos que matan ventas o causan rechazo)

### 1.1 — La economía de impresión (el problema #1)
Doblar el libro a **233 páginas a color** se sintió como "más valor", pero en KDP **el color
se paga por página** y te come el margen:

| Interior | Costo impresión aprox. (233 pág, 8.5×11) | Comentario |
|---|---|---|
| Blanco y negro | ~**US$3.65** ($0.85 + 233×$0.012) | Barato, pero pierdes las ilustraciones |
| **Standard color** (Amazon.com) | ~**US$6.94** ($1.00 + 233×$0.0255) | La opción color viable (72–600 pág) |
| Premium color | ~**US$17** ($0.85 + 233×$0.0700) | Inviable para este precio de nicho |

Referencia de mercado: *un libro de 200 páginas a color cuesta ~$13.85 de impresión vs ~$3.25
en B/N*. Con royalty del 60% (precio ≥ $9.99):

- Standard color a **$14.99** → 0.60×14.99 − 6.94 = **~$2.05** de ganancia/libro (apretado).
- Standard color a **$19.99** → 0.60×19.99 − 6.94 = **~$5.05** (mejor, pero **precio alto** para
  el nicho; baja la conversión).
- B/N a **$11.99** → 0.60×11.99 − 3.65 = **~$3.54** con precio competitivo.

**Conclusión:** tu versión actual (color, 233 pág) probablemente tendría que venderse a
$18-22 para ganar algo decente — caro para un libro de actividades. **Doblar las páginas, sin
querer, empeoró la economía.**

### 1.2 — Cumplimiento de IA en KDP (riesgo de baneo)
Las **109 ilustraciones son generadas por IA** (FLUX). Amazon **obliga a declarar** contenido
generado por IA (imágenes de portada e interior) al publicar o reeditar. **No declararlo puede
implicar retiro del libro o suspensión de la cuenta.** (La declaración no se muestra al
comprador ni afecta el ranking.) Además:
- Revisa **una por una** las 109 imágenes buscando artefactos típicos de IA (manos/dedos/caras
  raras, texto inventado). Los libros infantiles con IA reciben más escrutinio y reseñas duras.

### 1.3 — Preparación para imprenta (riesgo de rechazo)
Tu PDF es **8.5×11 exacto** y la **portada y los separadores van "a sangre"** (ocupan todo el
borde, `margin:0`). Para imprimir a sangre, KDP exige el interior a **8.625×11.25** (sangrado de
0.125" ancho / 0.25" alto). **Mezclar páginas con y sin sangrado es la causa #1 de rechazo.**
Hoy tienes imágenes que tocan el borde en un PDF sin sangrado → o se rechaza, o saldrán
**franjas blancas** si el corte se desvía 1-2 mm.
- Decisión: **(a)** todo con sangrado a 8.625×11.25, **o (b)** sin sangrado y meter las imágenes
  de portada/separadores **dentro de los márgenes** (con un marco). Hay que elegir una y ser
  consistente.

### 1.4 — Posicionamiento y SEO genéricos
- **Título "Tiempo de Calidad"**: bonito pero no dice **nicho, edad ni beneficio**, y no captura
  búsquedas. "kids activity book" arroja **~50.000 resultados** (océano rojo).
- Falta **subtítulo cargado de keywords**, elección de **2 categorías**, **7 keywords backend**,
  y definir **público** (edad, idioma, país/marketplace). Sin esto, no apareces en búsquedas.

### 1.5 — Sin autor/serie/marca
- `meta.autor` sigue como **"[Tu nombre]"** (no publiques así).
- Es **un solo mega-libro** en vez de aprovechar una **serie** (más listados = más superficie
  de búsqueda y compras repetidas).

### 1.6 — Falta lo legal y de seguridad
- No hay **página de copyright** ("Todos los derechos reservados", año, autor).
- No hay **descargo de responsabilidad (disclaimer)** — **crítico** porque hay experimentos con
  **fuego, imanes y riesgo de atragantamiento (0-2)**. Sin esto: riesgo legal y malas reseñas.

---

## 2. Lo que podrías hacer MEJOR

- **Subtítulo SEO** (ejemplo): *"+100 actividades y experimentos de ciencia sin pantallas para
  niños de 0 a 12 años — juego, arte y naturaleza para hacer en casa"*. Mete edad + cantidad +
  "experimentos/ciencia" + "sin pantallas" + "en casa".
- **Portada de venta profesional** (distinta de la ilustración interior): título y **beneficio**
  grandes, **rango de edad visible**, legible como miniatura a 100 px ("thumbnail-first"). Para
  tapa blanda necesitas el **wrap completo** (contraportada con blurb + bullets + lomo).
- **Descripción** con bullets y formato (negritas, emojis moderados), **categorías** correctas en
  español (p. ej. *Libros para niños › Actividades, juegos y diversión*), y targeting de
  **Amazon.com.mx, Amazon.es y el público hispano de Amazon.com**.
- **"Look inside"**: que las primeras páginas vendan (índice atractivo, "cómo usar", una
  actividad estrella).
- **Reseñas de lanzamiento**: regala copias a familias/profes por reseña honesta; precio de
  lanzamiento + sube después.

---

## 3. Qué QUITAR

- **El relleno que infla páginas sin valor**: varias actividades dejan una 2.ª página casi vacía
  (solo notas). Reorganiza para no **pagar impresión por páginas semi-blancas**.
- **El color del interior impreso** (muévelo a B/N para la edición en papel; deja el color para
  el **ebook** y el **PDF/printable**). Es la palanca más grande de margen.
- **La idea de "un mega-libro"** si conviene más la **serie** (ver abajo).

---

## 4. Qué INCORPORAR

- **Serie por edad (4 SKUs) + bundle "Colección completa":**
  *0-2*, *3-5*, *6-8*, *9-12* (~26 actividades, ~55-60 pág c/u). Ventajas: impresión barata,
  **4 listados** (más SEO), compras repetidas, y un "tomo completo" para quien quiere todo.
- **Edición digital / printable** (Etsy, Gumroad o web propia): **margen ~90%**, sin costo de
  impresión, entrega instantánea. Ideal para actividades imprimibles. Estrategia **multi-canal**
  (KDP impreso + Kindle + printable en Etsy) maximiza ingresos del mismo contenido.
- **Páginas de valor** (que además justifican el grosor sin "relleno vacío"): índice por
  edad/tipo/**dificultad**, **página de seguridad**, **"bitácora del pequeño científico"**
  (registro de hipótesis/resultados → engagement), lista de materiales por actividad, y
  **códigos QR** a videos/recursos.
- **Marca + lead magnet**: nombre de serie/colección y un **PDF gratis de 5 actividades** a
  cambio del email (lista para futuros lanzamientos).
- **Obligatorio antes de publicar**: declaración de IA en KDP, página de **copyright** y
  **disclaimer** de seguridad.

---

## 5. Tu ángulo ganador (en qué doblar la apuesta)

**"Ciencia y juego sin pantallas, en español, por edad."** Es un **nicho específico** (lo que sí
funciona) dentro de una categoría enorme:
- El **mercado hispano** está **menos saturado** que el inglés (aunque Kindle Unlimited es más
  chico ahí; por eso conviene **venta directa**, no solo KU).
- **STEM/ciencia para niños** es de los sub-nichos con mejor demanda y diferenciación.
- **Long-tail**: apunta a "experimentos para niños de 3 a 5 años", "actividades sin pantallas",
  "ciencia en casa para niños" — no a "libro de actividades".

---

## 6. Plan de acción priorizado

**Fase 0 — Decisiones de negocio (antes de tocar nada más)**
1. ¿Serie por edad o libro único? (recomendado: **serie** + bundle).
2. ¿Interior impreso B/N o standard color? (recomendado: **B/N impreso + color en ebook/PDF**).
3. ¿Canales? (recomendado: **KDP impreso + Kindle + printable en Etsy/Gumroad**).

**Fase 1 — Cumplimiento y producción (bloqueantes de publicación)**
4. Configurar **sangrado** correcto (o meter imágenes dentro de márgenes), consistente.
5. **Página de copyright + disclaimer** de seguridad.
6. Plan para **declarar IA** en KDP y **QA visual** de las 109 imágenes.

**Fase 2 — Posicionamiento (lo que genera ventas)**
7. Título + **subtítulo SEO**, **7 keywords**, **2 categorías**, público/marketplaces.
8. **Portada de venta** profesional (wrap completo) + **descripción** con bullets.

**Fase 3 — Lanzamiento**
9. Precio de lanzamiento, **reseñas** iniciales, lead magnet, y réplica a **Etsy/Kindle**.

---

## Fuentes (mercado KDP)
- KDP — costos de impresión / regalías: <https://www.bookbloom.io/blog/kdp-print-cost-pricing-guide>, <https://kdp.amazon.com/en_US/help/topic/G201834340>
- KDP — política de divulgación de IA: <https://kdp.amazon.com/en_US/help/topic/G200672390>, <https://authorsguild.org/news/amazons-new-disclosure-policy-for-ai-generated-book-content-is-a-welcome-first-step/>
- Diferenciación / nichos infantiles: <https://bookbolt.io/what-are-kdp-activity-books-top-niches-best-sellers/>, <https://www.automateed.com/profitable-niches-for-low-content-books>
- Mercado en español: <https://marianaeguaras.com/porcentajes-de-amazon-kdp-regalias-para-libros-impresos-y-digitales/>
- Sangrado / formato 8.5×11: <https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6>, <https://www.kdpeasy.com/blog/puzzle-book-interior-formatting-kdp>
- KDP vs Etsy (printables): <https://www.etshop.ai/etsy-seller/kdp-vs-etsy-low-content-books-vs-printables-1167>
