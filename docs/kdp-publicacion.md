# Guía de publicación en KDP — *Tiempo de Calidad*

Datos listos para copiar y pegar al publicar en Amazon KDP. Ajusta a tu gusto.

---

## Metadatos del libro

**Título:** `Tiempo de Calidad`

**Subtítulo (elige uno; máx. 200 caracteres):**
1. `+100 actividades y experimentos sin pantallas para niños de 0 a 12 años: ciencia, juego, arte, sensorial y naturaleza para hacer en casa con materiales caseros`
2. `100 experimentos y actividades de ciencia sin pantallas para niños de 0 a 12 años: juego y aprendizaje en casa, paso a paso, con cosas que ya tienes`
3. `Actividades y experimentos sin pantallas para niños: +100 ideas de ciencia, juego y arte por edad (0-2, 3-5, 6-8 y 9-12 años) para hacer en familia`

**Autor:** *(completa tu nombre real o seudónimo — hoy figura "[Tu nombre]" en `data/book.yaml`)*

**Idioma:** Español

**Edad de lectura / público:** padres y cuidadores de niños de **0 a 12 años**
(en KDP, "Reading age": 0-12; o publica la **serie por edad**, ver abajo).

---

## Palabras clave (7 casillas de KDP) — long-tail en español

> Usa frases que un padre buscaría, no palabras sueltas. Valida que cada una tenga
> competencia razonable antes de fijarla.

1. `actividades para niños sin pantallas`
2. `experimentos de ciencia para niños en casa`
3. `actividades educativas niños 3 a 5 años`
4. `juegos sin pantallas para niños`
5. `manualidades y experimentos para niños`
6. `actividades para hacer en familia en casa`
7. `libro de actividades niños español`

---

## Categorías (elige 2 — rutas en español)

- **Libros para niños › Educación y referencia › Ciencia y naturaleza**
- **Libros para niños › Actividades, manualidades y juegos › Juegos y actividades**

*(Alternativas: "Crianza y familias › Actividades"; "Hogar y pasatiempos".)*
Tras publicar, puedes pedir a KDP categorías adicionales por correo.

---

## Descripción del producto (para la página de venta)

> Pégala en el campo "Descripción". Amazon permite formato básico (negritas, listas).

```
¿Tus hijos piden pantalla apenas se aburren? Este libro es la respuesta.

Tiempo de Calidad reúne MÁS DE 100 actividades y experimentos sin pantallas
para hacer en casa, con materiales que ya tienes. Están organizados POR EDAD
(0-2, 3-5, 6-8 y 9-12 años) para que siempre encuentres algo a la medida de tu
hijo o hija.

Dentro encontrarás:
• 43 experimentos de CIENCIA explicados paso a paso (volcanes, densidad, tinta
  invisible, ADN de frutilla, circuitos y mucho más).
• Juegos, arte, actividades sensoriales y de naturaleza para todos los días.
• Indicadores claros de dificultad, materiales y duración: eliges según el tiempo
  y la energía que tengas hoy.
• Ilustraciones a color en cada actividad y notas de seguridad cuando hacen falta.

Sin comprar nada caro. Sin pantallas. Solo tiempo de calidad en familia.

Ideal para padres, abuelos, cuidadores y profesores. ¡Empieza hoy la primera
actividad!
```

---

## Precio y formato (lo más importante para tu margen)

El interior a color es caro de imprimir. Recomendación de catálogo:

| Edición | Archivo | Costo impresión aprox. | Precio sugerido | Notas |
|---|---|---|---|---|
| **Tapa blanda B/N** | `dist/Tiempo-de-Calidad-BN.pdf` | ~US$3.65 | **$11.99–13.99** | Mejor margen; competitivo |
| Tapa blanda color (standard) | `dist/Tiempo-de-Calidad.pdf` | ~US$6.94 | $18.99–21.99 | Solo si quieres versión premium |
| **eBook Kindle** | `dist/Tiempo-de-Calidad.epub` | $0 | **$4.99–6.99** | Color sin costo de impresión |
| **PDF imprimible** (Etsy/Gumroad) | PDF a color | $0 | $6.99–9.99 | Margen ~90%, fuera de Amazon |

> Regalías KDP: 60% del precio − costo de impresión (precio ≥ $9.99). Sube el precio
> antes que sacrificar el margen; el mercado de actividades tolera $12-14 en tapa blanda B/N.

---

## ✅ Checklist antes de publicar

- [ ] **Declarar IA** en el formulario de KDP: las ilustraciones (portada e interior) son
      generadas por IA. **Obligatorio**; no declararlo puede causar el retiro del libro o el
      cierre de la cuenta. *(Ya hay una nota de transparencia en la página de créditos.)*
- [ ] **Revisar las 109 imágenes** una a una por artefactos de IA (manos/caras/texto raros).
- [x] **Sangrado del interior**: generado con `python scripts/build.py --kdp` →
      `dist/Tiempo-de-Calidad-KDP.pdf` (8.625×11.25 in). Sube ese archivo (o `-KDP-BN.pdf`),
      no el de 8.5×11.
- [x] Página de **copyright** y **descargo de responsabilidad** de seguridad — ya incluidas.
- [x] **Portada de venta** profesional (wrap completo con lomo + contraportada): genérala con
      `python scripts/build_cover.py` → `dist/Portada-KDP-tapa-blanda.pdf`. Edita el blurb en
      `scripts/build_cover.py` (dict `BACK`). El lomo se calcula según el nº de páginas.
- [ ] Completar **nombre de autor** en `data/book.yaml` (`meta.autor`).
- [ ] Subir a **Amazon.com, Amazon.com.mx y Amazon.es** (mercados hispanos).

---

## Estrategia de serie (recomendada)

En vez de un solo tomo de 233 páginas, considera **4 libros por edad** (~26 actividades,
~55-60 págs c/u) + un **"Tomo completo"**:

- *Tiempo de Calidad — 0 a 2 años* · *3 a 5 años* · *6 a 8 años* · *9 a 12 años*
- Ventajas: impresión barata por tomo, **4 listados** (más superficie de búsqueda),
  compras repetidas y un bundle para quien quiere todo.
- Cada tomo: su propio subtítulo con la edad ("...para niños de 3 a 5 años").

*(Se puede automatizar dividiendo el build por banda de edad — pídelo y lo implemento.)*
