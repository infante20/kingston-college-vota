# Plan de imágenes en Canva — *Tiempo de Calidad*

> Documento de trabajo. Cuando la sesión corra en un entorno con **red abierta** (o allowlist con `*.canva.com`) y el **conector de Canva activado**, se ejecuta este plan: por cada ítem se genera el diseño en Canva, se exporta a PNG y se descarga al **archivo destino** indicado. El build (`scripts/build.py`) ya prioriza los `.png` sobre los `.svg`, así que las imágenes de Canva reemplazan automáticamente a las ilustraciones vectoriales actuales.

## Estado de ejecución (2026-06-03)

- ✅ **Portada + 4 separadores** generados, exportados y descargados (commit en `claude/exciting-fermi-bQzqV`). Se ven limpios, sin texto, fieles a la guía de estilo.
- ⏳ **48 ilustraciones de actividad: pendientes.** Bloqueadas por **cupo de Canva (Magic / AI generation) agotado** — reintentar cuando se reponga el cupo.

## Pipeline probado (orden de llamadas MCP)

1. `generate-design` → devuelve 4 *candidates* (tomar el 1.º).
2. `create-design-from-candidate` → `design_id`.
3. `export-design` con `{"type":"png"}` **sin width/height** (forzar dimensiones que no respetan el aspect del tipo da error «Not allowed to access»; exportar nativo y redimensionar luego con Pillow).
4. Descargar el PNG y redimensionar al tamaño destino.

## ⚠️ Decisiones de tipo de diseño (aprendido en la 1.ª corrida)

- **`design_type: poster`** → ilustración limpia, a sangre, **sin texto**. ✅ Usar para portada, separadores **y actividades**.
- **`design_type: facebook_cover`** → NO usar: genera una pieza de redes con **titulares de texto** y mete la ilustración dentro de un marco chico. Rompe la regla «sin texto».
- Como `poster` es **vertical**, las actividades pasan a ilustración **vertical/cuadrada** y la maquetación se ajusta (ver abajo). Decisión confirmada por el autor (2026-06-03).

## Ajuste de maquetación pendiente (para imágenes verticales de actividad)

Hoy `styles/print.css` usa `.act-img { width:100%; height:48mm; object-fit:cover }` (banda apaisada que recortaría una ilustración vertical). Al traer los posters verticales hay que cambiar a una **figura vertical/cuadrada** (p. ej. imagen flotada o bloque junto al texto, con `object-fit:contain` o caja con aspect adecuado) y verificar el build con 1-2 imágenes reales antes del lote completo.

## Especificaciones técnicas

| Recurso | Archivo destino | Tamaño sugerido | Orientación |
| --- | --- | --- | --- |
| Portada | `assets/images/portada.png` | 1700 × 2200 px | Vertical (8.5×11) ✅ |
| Separador 0 a 2 años | `assets/images/sep-0-2.png` | 1700 × 2200 px | Vertical (8.5×11) ✅ |
| Separador 3 a 5 años | `assets/images/sep-3-5.png` | 1700 × 2200 px | Vertical (8.5×11) ✅ |
| Separador 6 a 8 años | `assets/images/sep-6-8.png` | 1700 × 2200 px | Vertical (8.5×11) ✅ |
| Separador 9 a 12 años | `assets/images/sep-9-12.png` | 1700 × 2200 px | Vertical (8.5×11) ✅ |
| Ilustración de actividad (×48) | `assets/images/<id>.png` | ~1400 × 1400 px | **Vertical/cuadrada** (poster) ⏳ |

**Formato de exportación:** PNG. **Sin texto en la imagen** (los títulos los pone la maquetación). Mantener coherencia de estilo y paleta entre todas. Generar **todo con `design_type: poster`**.

## Guía de estilo visual (común a todo el libro)

- **Estilo:** ilustración plana (flat vector), tipo libro infantil; cálida, amigable y moderna.
- **Paleta:** verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D; fondo **crema #FBF7F0**; tinta suave para detalles.
- **Acento por tipo de actividad:**
  - Experimento: `#3E6E94`
  - Sensorial: `#7E57A6`
  - Recreativa / Motriz: `#E8744F`
  - Juego: `#2E7D5B`
  - Conexión emocional: `#D24D6E`
  - Arte y manualidades: `#F2A03D`
  - Naturaleza: `#5B9E4A`
- **Personajes:** niñas y niños diversos e inclusivos, expresiones alegres y serenas; en 0-2 aparece la figura del cuidador.
- **Reglas:** formas redondeadas, sombras suaves, composición centrada con márgenes; **nada de texto, palabras, letras, números ni logos**.

---

## Portada

- **Archivo:** `assets/images/portada.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (formato libro) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Escena de portada: una familia disfrutando tiempo juntos en casa sin pantallas — jugando, leyendo y creando. Ambiente hogareño cálido y luminoso, sensación de cercanía y alegría. Deja espacio libre y despejado en el centro/parte superior para sobreponer el título después. Predomina el verde de la paleta.
```

## Separadores de capítulo (uno por rango de edad)

### 0 a 2 años — «Descubrir el mundo con los sentidos»
- **Archivo:** `assets/images/sep-0-2.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (página completa) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. escena tierna y calmada: un bebé descubriendo el mundo con los sentidos, objetos blandos y formas suaves, ambiente acogedor de hogar. Composición de página completa, decorativa, con espacio inferior más despejado para sobreponer el título del capítulo.
```

### 3 a 5 años — «Jugar es aprender»
- **Archivo:** `assets/images/sep-3-5.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (página completa) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. escena alegre y juguetona: niños pequeños jugando e imaginando, cajas de cartón, pinturas y formas divertidas. Composición de página completa, decorativa, con espacio inferior más despejado para sobreponer el título del capítulo.
```

### 6 a 8 años — «Crear, construir y descubrir»
- **Archivo:** `assets/images/sep-6-8.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (página completa) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. escena de creación y descubrimiento: niños construyendo, experimentando y jugando con proyectos hechos a mano. Composición de página completa, decorativa, con espacio inferior más despejado para sobreponer el título del capítulo.
```

### 9 a 12 años — «Pensar en grande y trabajar en equipo»
- **Archivo:** `assets/images/sep-9-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (página completa) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. escena de trabajo en equipo y desafíos: preadolescentes colaborando, investigando y creando proyectos en conjunto. Composición de página completa, decorativa, con espacio inferior más despejado para sobreponer el título del capítulo.
```

## Ilustraciones de actividades (48)


### 0 a 2 años

#### `0a2-01` — Canasta de los tesoros  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-01.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Canasta de los tesoros». Una canasta llena de objetos cotidianos para que el bebé explore con todos los sentidos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-02` — Cazadores de pompas  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Cazadores de pompas». Pompas de jabón que flotan, brillan y desaparecen al tocarlas, pura magia para los ojos del bebé. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-03` — Botella de la calma  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Botella de la calma». Una botella con agua, brillos y objetos flotantes que hipnotiza y relaja al bebé. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-04` — Trasvases de agua  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Trasvases de agua». Recipientes, cucharas y agua para chapotear, llenar y vaciar una y otra vez. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-05` — Mantita de texturas  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Mantita de texturas». Una manta o panel con retazos de telas distintas para tocar, frotar y descubrir. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-06` — ¿Dónde está mamá? ¡Cucú-tras!  ·  *Conexión emocional*
- **Archivo:** `assets/images/0a2-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «¿Dónde está mamá? ¡Cucú-tras!». El clásico juego de esconderse y aparecer que enseña que lo que no se ve sigue ahí. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-07` — Caras en el espejo  ·  *Conexión emocional*
- **Archivo:** `assets/images/0a2-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Caras en el espejo». Frente al espejo, juntos, descubrimos sonrisas, muecas y el propio reflejo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-08` — Pequeña orquesta casera  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/0a2-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Pequeña orquesta casera». Ollas, cucharas y botes se convierten en tambores y maracas para hacer música juntos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-09` — Circuito de cojines  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/0a2-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Circuito de cojines». Una pista de almohadas y mantas para gatear, trepar y rodar sin peligro. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-10` — Torres que se caen  ·  *Juego*
- **Archivo:** `assets/images/0a2-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Torres que se caen». Apilar vasos o cajas para construir una torre y derribarla con un solo manotazo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-11` — Pintura de yogur  ·  *Arte y manualidades*
- **Archivo:** `assets/images/0a2-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Pintura de yogur». Pintar con los dedos usando yogur de colores, una obra de arte que se puede chupar sin peligro. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-12` — Meter y sacar  ·  *Juego*
- **Archivo:** `assets/images/0a2-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Meter y sacar». Una caja y varios objetos para llenar, vaciar y descubrir el placer de aparecer y desaparecer. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```


### 3 a 5 años

#### `3a5-01` — El volcán de bicarbonato  ·  *Experimento*
- **Archivo:** `assets/images/3a5-01.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El volcán de bicarbonato». Un volcán casero que entra en erupción con espuma de colores ante los ojos del peque. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-02` — Los colores que bailan  ·  *Experimento*
- **Archivo:** `assets/images/3a5-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Los colores que bailan». Gotas de colorante que se persiguen y se mezclan en un plato de leche, como por arte de magia. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-03` — Masa blandita casera  ·  *Sensorial*
- **Archivo:** `assets/images/3a5-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Masa blandita casera». Una masa suave para amasar, aplastar y modelar mil formas con las propias manos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-04` — La caja misteriosa  ·  *Sensorial*
- **Archivo:** `assets/images/3a5-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La caja misteriosa». Meter la mano sin mirar y adivinar qué objeto se esconde dentro solo con el tacto. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-05` — El circuito de cojines  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/3a5-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El circuito de cojines». Un recorrido de saltos, gateos y equilibrios armado con cojines y mantas del living. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-06` — Bolos con botellas  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/3a5-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Bolos con botellas». Una bolera casera con botellas para derribar lanzando una pelota de calcetines. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-07` — La tienda imaginaria  ·  *Juego*
- **Archivo:** `assets/images/3a5-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La tienda imaginaria». Montar una tiendita en casa para comprar y vender, con monedas de cartón y mucha imaginación. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-08` — Búsqueda de colores  ·  *Juego*
- **Archivo:** `assets/images/3a5-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Búsqueda de colores». Una carrera por la casa para encontrar objetos de cada color y llenar la canasta del arcoíris. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-09` — Las caras de las emociones  ·  *Conexión emocional*
- **Archivo:** `assets/images/3a5-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Las caras de las emociones». Dibujar y poner cara a la alegría, el enfado o el miedo para aprender a nombrar lo que se siente. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-10` — Sellos de papa y verduras  ·  *Arte y manualidades*
- **Archivo:** `assets/images/3a5-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Sellos de papa y verduras». Estampar figuras una y otra vez con sellos hechos de papas, corchos y verduras. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-11` — Collage de hojas y flores  ·  *Arte y manualidades*
- **Archivo:** `assets/images/3a5-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Collage de hojas y flores». Pegar hojas, pétalos y ramitas para crear un cuadro lleno de tesoros de la naturaleza. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-12` — Safari de bichos en el jardín  ·  *Naturaleza*
- **Archivo:** `assets/images/3a5-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Safari de bichos en el jardín». Salir de exploradores con una lupa de cartón a descubrir los bichitos que viven cerca de casa. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```


### 6 a 8 años

#### `6a8-01` — La torre de líquidos mágica  ·  *Experimento*
- **Archivo:** `assets/images/6a8-01.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «La torre de líquidos mágica». Apila miel, agua y aceite en un mismo vaso y descubre por qué nunca se mezclan. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-02` — Cohete de globo por un hilo  ·  *Experimento*
- **Archivo:** `assets/images/6a8-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Cohete de globo por un hilo». Construye una pista invisible y haz que un globo salga disparado como un cohete. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-03` — Mandala de sal de colores  ·  *Arte y manualidades*
- **Archivo:** `assets/images/6a8-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Mandala de sal de colores». Pinta la sal con tiza y crea un mosaico de colores que cabe en la palma de la mano. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-04` — La caja misteriosa al tacto  ·  *Sensorial*
- **Archivo:** `assets/images/6a8-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «La caja misteriosa al tacto». Mete la mano sin mirar y adivina qué objeto escondido estás tocando. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-05` — Circuito de obstáculos casero  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/6a8-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Circuito de obstáculos casero». Convierte el salón o el patio en una pista de saltos, túneles y equilibrio. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-06` — Bolos caseros con botellas  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/6a8-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Bolos caseros con botellas». Arma tu propia bolera con botellas y lanza para tumbarlas todas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-07` — Inventa tu juego de mesa  ·  *Juego*
- **Archivo:** `assets/images/6a8-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Inventa tu juego de mesa». Dibuja un tablero con tus propias reglas y rétate a llegar el primero a la meta. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-08` — Búsqueda del tesoro con pistas  ·  *Juego*
- **Archivo:** `assets/images/6a8-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Búsqueda del tesoro con pistas». Sigue un rastro de acertijos por la casa hasta encontrar el tesoro escondido. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-09` — El frasco de la calma  ·  *Conexión emocional*
- **Archivo:** `assets/images/6a8-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El frasco de la calma». Crea una galaxia de purpurina en un frasco para tranquilizarte cuando te enojas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-10` — Títeres de cartón con teatro  ·  *Arte y manualidades*
- **Archivo:** `assets/images/6a8-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Títeres de cartón con teatro». Da vida a unos personajes de cartón y monta tu propia función de marionetas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-11` — Diario de exploradores de la naturaleza  ·  *Naturaleza*
- **Archivo:** `assets/images/6a8-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Diario de exploradores de la naturaleza». Sal a la calle con lupa y cuaderno y conviértete en un explorador de la naturaleza. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-12` — El globo con electricidad mágica  ·  *Experimento*
- **Archivo:** `assets/images/6a8-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El globo con electricidad mágica». Frota un globo en tu pelo y haz que mueva cosas sin tocarlas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```


### 9 a 12 años

#### `9a12-01` — Cromatografía con plumones  ·  *Experimento*
- **Archivo:** `assets/images/9a12-01.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Cromatografía con plumones». Descubre que el negro de un plumón esconde muchos colores ocultos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-02` — Reloj de agua casero  ·  *Experimento*
- **Archivo:** `assets/images/9a12-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Reloj de agua casero». Mide el tiempo como en la antigüedad, solo con agua y gravedad. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-03` — Mensajes en código secreto  ·  *Juego*
- **Archivo:** `assets/images/9a12-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Mensajes en código secreto». Crea tu propio cifrado y envía mensajes que solo tu equipo podrá leer. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-04` — Escape room casero  ·  *Juego*
- **Archivo:** `assets/images/9a12-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Escape room casero». Diseña una sala de enigmas en casa y reta a tu familia a escapar. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-05` — Inventa tu juego de estrategia  ·  *Juego*
- **Archivo:** `assets/images/9a12-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Inventa tu juego de estrategia». Diseña desde cero un juego de mesa con tablero, reglas y fichas propias. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-06` — Circuito de retos y equilibrio  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/9a12-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Circuito de retos y equilibrio». Convierte el patio o el pasillo en una pista de obstáculos que pone a prueba tu cuerpo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-07` — Fabrica y aprende malabares  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/9a12-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Fabrica y aprende malabares». Hazte tus propias pelotas y domina el arte de los tres lanzamientos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-08` — Cápsula del tiempo  ·  *Conexión emocional*
- **Archivo:** `assets/images/9a12-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Cápsula del tiempo». Guarda un mensaje para tu yo del futuro y ábrelo dentro de un año. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-09` — Frasco de grandes conversaciones  ·  *Conexión emocional*
- **Archivo:** `assets/images/9a12-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Frasco de grandes conversaciones». Preguntas para hablar de verdad y descubrir lo que cada uno piensa y siente. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-10` — Crea tu propio cómic  ·  *Arte y manualidades*
- **Archivo:** `assets/images/9a12-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Crea tu propio cómic». Inventa una historia con viñetas, globos de diálogo y un héroe a tu medida. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-11` — Flipbook: animación sin pantalla  ·  *Arte y manualidades*
- **Archivo:** `assets/images/9a12-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Flipbook: animación sin pantalla». Da vida a tus dibujos creando una película de bolsillo que se mueve al pasar las hojas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-12` — Tu huerto en macetero  ·  *Naturaleza*
- **Archivo:** `assets/images/9a12-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición vertical (tarjeta), encuadre cuadrado o ligeramente vertical con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Tu huerto en macetero». Cultiva tus propias plantas aromáticas y observa cómo crecen día a día. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

