# Plan de imágenes en Canva — *Tiempo de Calidad*

> Documento de trabajo. Cuando la sesión corra en un entorno con **red abierta** (o allowlist con `*.canva.com`) y el **conector de Canva activado**, se ejecuta este plan: por cada ítem se genera el diseño en Canva, se exporta a PNG y se descarga al **archivo destino** indicado. El build (`scripts/build.py`) ya prioriza los `.png` sobre los `.svg`, así que las imágenes de Canva reemplazan automáticamente a las ilustraciones vectoriales actuales.

## Especificaciones técnicas

| Recurso | Archivo destino | Tamaño sugerido | Orientación |
| --- | --- | --- | --- |
| Portada | `assets/images/portada.png` | 1700 × 2200 px | Vertical (8.5×11) |
| Separador 0 a 2 años | `assets/images/sep-0-2.png` | 1700 × 2200 px | Vertical (8.5×11) |
| Separador 3 a 5 años | `assets/images/sep-3-5.png` | 1700 × 2200 px | Vertical (8.5×11) |
| Separador 6 a 8 años | `assets/images/sep-6-8.png` | 1700 × 2200 px | Vertical (8.5×11) |
| Separador 9 a 12 años | `assets/images/sep-9-12.png` | 1700 × 2200 px | Vertical (8.5×11) |
| Ilustración de actividad (×48) | `assets/images/<id>.png` | 1200 × 460 px | Horizontal (banner) |

**Formato de exportación:** PNG. **Sin texto en la imagen** (los títulos los pone la maquetación). Mantener coherencia de estilo y paleta entre todas.

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
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Canasta de los tesoros». Una canasta llena de objetos cotidianos para que el bebé explore con todos los sentidos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-02` — Cazadores de pompas  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Cazadores de pompas». Pompas de jabón que flotan, brillan y desaparecen al tocarlas, pura magia para los ojos del bebé. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-03` — Botella de la calma  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Botella de la calma». Una botella con agua, brillos y objetos flotantes que hipnotiza y relaja al bebé. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-04` — Trasvases de agua  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Trasvases de agua». Recipientes, cucharas y agua para chapotear, llenar y vaciar una y otra vez. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-05` — Mantita de texturas  ·  *Sensorial*
- **Archivo:** `assets/images/0a2-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Mantita de texturas». Una manta o panel con retazos de telas distintas para tocar, frotar y descubrir. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-06` — ¿Dónde está mamá? ¡Cucú-tras!  ·  *Conexión emocional*
- **Archivo:** `assets/images/0a2-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «¿Dónde está mamá? ¡Cucú-tras!». El clásico juego de esconderse y aparecer que enseña que lo que no se ve sigue ahí. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-07` — Caras en el espejo  ·  *Conexión emocional*
- **Archivo:** `assets/images/0a2-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Caras en el espejo». Frente al espejo, juntos, descubrimos sonrisas, muecas y el propio reflejo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-08` — Pequeña orquesta casera  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/0a2-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Pequeña orquesta casera». Ollas, cucharas y botes se convierten en tambores y maracas para hacer música juntos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-09` — Circuito de cojines  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/0a2-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Circuito de cojines». Una pista de almohadas y mantas para gatear, trepar y rodar sin peligro. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-10` — Torres que se caen  ·  *Juego*
- **Archivo:** `assets/images/0a2-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Torres que se caen». Apilar vasos o cajas para construir una torre y derribarla con un solo manotazo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-11` — Pintura de yogur  ·  *Arte y manualidades*
- **Archivo:** `assets/images/0a2-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Pintura de yogur». Pintar con los dedos usando yogur de colores, una obra de arte que se puede chupar sin peligro. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-12` — Meter y sacar  ·  *Juego*
- **Archivo:** `assets/images/0a2-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Meter y sacar». Una caja y varios objetos para llenar, vaciar y descubrir el placer de aparecer y desaparecer. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-13` — ¿Flota o se hunde?  ·  *Experimento*
- **Archivo:** `assets/images/0a2-13.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «¿Flota o se hunde?». Un balde con agua y objetos del hogar para descubrir cuáles se quedan arriba y cuáles caen al fondo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-14` — Sombras mágicas  ·  *Experimento*
- **Archivo:** `assets/images/0a2-14.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Sombras mágicas». Con una linterna y una pared, las manos y los juguetes cobran vida en sombras que aparecen y crecen. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-15` — Hielo que desaparece  ·  *Experimento*
- **Archivo:** `assets/images/0a2-15.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Hielo que desaparece». Un cubo de hielo grande que se vuelve agua entre las manos tibias del bebé, frío que se escapa. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-16` — Rampa de pelotas  ·  *Experimento*
- **Archivo:** `assets/images/0a2-16.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Rampa de pelotas». Una tabla inclinada y pelotas que ruedan solas hacia abajo: la gravedad jugando ante los ojos del bebé. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-17` — Cazar la luz  ·  *Experimento*
- **Archivo:** `assets/images/0a2-17.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Cazar la luz». Un espejito refleja el sol y crea un punto de luz que baila por la pared para que el bebé lo persiga. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-18` — Papel que cae  ·  *Experimento*
- **Archivo:** `assets/images/0a2-18.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Papel que cae». Un papel baja flotando despacio y una pelota cae de golpe: dos formas distintas de caer que sorprenden al bebé. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-19` — Tesoros del jardín  ·  *Naturaleza*
- **Archivo:** `assets/images/0a2-19.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Tesoros del jardín». Un paseo lento por el pasto para tocar hojas, sentir la brisa y descubrir el mundo natural con todos los sentidos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-20` — Sembrar una semilla  ·  *Naturaleza*
- **Archivo:** `assets/images/0a2-20.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Sembrar una semilla». Llenar un macetero con tierra y poner una semilla para esperar juntos a que la planta despierte. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-21` — Sellos de esponja  ·  *Arte y manualidades*
- **Archivo:** `assets/images/0a2-21.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Sellos de esponja». Esponjas mojadas en pintura que dejan huellas de colores en el papel con solo apretar. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-22` — Pelota de ida y vuelta  ·  *Juego*
- **Archivo:** `assets/images/0a2-22.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Pelota de ida y vuelta». Una pelota que rueda de tus manos a las del bebé y de vuelta, el primer juego de turnos y de compartir. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-23` — Masaje con canción  ·  *Conexión emocional*
- **Archivo:** `assets/images/0a2-23.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Masaje con canción». Caricias suaves al ritmo de una canción para que el bebé se relaje y sienta tu cariño en la piel. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-24` — Baile con pañuelos  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/0a2-24.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Baile con pañuelos». Pañuelos livianos que flotan y giran en el aire mientras bailan juntos al ritmo de la música. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-25` — Botella de burbujas  ·  *Experimento*
- **Archivo:** `assets/images/0a2-25.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Botella de burbujas». Una botella con agua y un poco de aire que, al moverla, se llena de burbujas que suben solas hacia arriba. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `0a2-26` — Rueda en cada piso  ·  *Experimento*
- **Archivo:** `assets/images/0a2-26.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un bebé o niño pequeño (0-2 años) acompañado por su madre o padre realizando la actividad «Rueda en cada piso». La misma pelota empujada igual, pero en una toalla apenas avanza y en el piso liso se va lejos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```


### 3 a 5 años

#### `3a5-01` — El volcán de bicarbonato  ·  *Experimento*
- **Archivo:** `assets/images/3a5-01.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El volcán de bicarbonato». Un volcán casero que entra en erupción con espuma de colores ante los ojos del peque. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-02` — Los colores que bailan  ·  *Experimento*
- **Archivo:** `assets/images/3a5-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Los colores que bailan». Gotas de colorante que se persiguen y se mezclan en un plato de leche, como por arte de magia. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-03` — Masa blandita casera  ·  *Sensorial*
- **Archivo:** `assets/images/3a5-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Masa blandita casera». Una masa suave para amasar, aplastar y modelar mil formas con las propias manos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-04` — La caja misteriosa  ·  *Sensorial*
- **Archivo:** `assets/images/3a5-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La caja misteriosa». Meter la mano sin mirar y adivinar qué objeto se esconde dentro solo con el tacto. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-05` — El circuito de cojines  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/3a5-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El circuito de cojines». Un recorrido de saltos, gateos y equilibrios armado con cojines y mantas del living. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-06` — Bolos con botellas  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/3a5-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Bolos con botellas». Una bolera casera con botellas para derribar lanzando una pelota de calcetines. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-07` — La tienda imaginaria  ·  *Juego*
- **Archivo:** `assets/images/3a5-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La tienda imaginaria». Montar una tiendita en casa para comprar y vender, con monedas de cartón y mucha imaginación. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-08` — Búsqueda de colores  ·  *Juego*
- **Archivo:** `assets/images/3a5-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Búsqueda de colores». Una carrera por la casa para encontrar objetos de cada color y llenar la canasta del arcoíris. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-09` — Las caras de las emociones  ·  *Conexión emocional*
- **Archivo:** `assets/images/3a5-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Las caras de las emociones». Dibujar y poner cara a la alegría, el enfado o el miedo para aprender a nombrar lo que se siente. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-10` — Sellos de papa y verduras  ·  *Arte y manualidades*
- **Archivo:** `assets/images/3a5-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Sellos de papa y verduras». Estampar figuras una y otra vez con sellos hechos de papas, corchos y verduras. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-11` — Collage de hojas y flores  ·  *Arte y manualidades*
- **Archivo:** `assets/images/3a5-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Collage de hojas y flores». Pegar hojas, pétalos y ramitas para crear un cuadro lleno de tesoros de la naturaleza. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-12` — Safari de bichos en el jardín  ·  *Naturaleza*
- **Archivo:** `assets/images/3a5-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Safari de bichos en el jardín». Salir de exploradores con una lupa de cartón a descubrir los bichitos que viven cerca de casa. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-13` — El aceite y el agua que no se mezclan  ·  *Experimento*
- **Archivo:** `assets/images/3a5-13.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El aceite y el agua que no se mezclan». Dos líquidos que se niegan a juntarse y forman burbujas mágicas dentro del vaso. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-14` — Flores blancas que cambian de color  ·  *Experimento*
- **Archivo:** `assets/images/3a5-14.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Flores blancas que cambian de color». Una flor blanca que amanece pintada de colores como por arte de magia. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-15` — La vela que se apaga bajo el vaso  ·  *Experimento*
- **Archivo:** `assets/images/3a5-15.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La vela que se apaga bajo el vaso». Una vela encendida que se apaga sola cuando le tapamos el aire con un vaso. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-16` — El globo que se infla solo  ·  *Experimento*
- **Archivo:** `assets/images/3a5-16.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El globo que se infla solo». Un globo que se infla sin soplar, empujado por las burbujas de una mezcla mágica. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-17` — Semillas que germinan en algodón  ·  *Experimento*
- **Archivo:** `assets/images/3a5-17.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Semillas que germinan en algodón». Plantar porotos en algodón y descubrir cada día cómo les crece una raíz y una hojita. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-18` — El imán y sus tesoros escondidos  ·  *Experimento*
- **Archivo:** `assets/images/3a5-18.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El imán y sus tesoros escondidos». Un imán explorador que descubre cuáles objetos de la casa se pegan y cuáles no. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-19` — Un arcoíris con agua y espejo  ·  *Experimento*
- **Archivo:** `assets/images/3a5-19.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Un arcoíris con agua y espejo». Atrapar la luz del sol con un espejo dentro del agua y pintar la pared de colores. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-20` — Paseo para coleccionar tesoros de la naturaleza  ·  *Naturaleza*
- **Archivo:** `assets/images/3a5-20.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Paseo para coleccionar tesoros de la naturaleza». Salir con una canasta a juntar hojas, piedritas y palitos para armar una colección propia. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-21` — Pintura suavecita con espuma  ·  *Sensorial*
- **Archivo:** `assets/images/3a5-21.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Pintura suavecita con espuma». Pintar con nubes de espuma blandita que se sienten frías y mullidas en las manos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-22` — La búsqueda del tesoro en casa  ·  *Juego*
- **Archivo:** `assets/images/3a5-22.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La búsqueda del tesoro en casa». Seguir pistas por toda la casa hasta encontrar un tesoro escondido al final del camino. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-23` — El frasco de la calma  ·  *Conexión emocional*
- **Archivo:** `assets/images/3a5-23.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «El frasco de la calma». Un frasco con brillos que se mueven despacio y ayudan a respirar y calmarse cuando uno se enoja. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-24` — Cuadros con burbujas de colores  ·  *Arte y manualidades*
- **Archivo:** `assets/images/3a5-24.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «Cuadros con burbujas de colores». Soplar burbujas de colores que estallan sobre el papel y dejan dibujos sorprendentes. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-25` — La leche mágica de colores  ·  *Experimento*
- **Archivo:** `assets/images/3a5-25.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La leche mágica de colores». Los colores salen disparados y bailan solos sobre la leche apenas la tocas con jabón. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `3a5-26` — La pimienta que huye del jabón  ·  *Experimento*
- **Archivo:** `assets/images/3a5-26.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad preescolar (3-5 años) realizando la actividad «La pimienta que huye del jabón». La pimienta flota tranquila en el agua y arranca asustada apenas asomas un dedo con jabón. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```


### 6 a 8 años

#### `6a8-01` — La torre de líquidos mágica  ·  *Experimento*
- **Archivo:** `assets/images/6a8-01.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «La torre de líquidos mágica». Apila miel, agua y aceite en un mismo vaso y descubre por qué nunca se mezclan. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-02` — Cohete de globo por un hilo  ·  *Experimento*
- **Archivo:** `assets/images/6a8-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Cohete de globo por un hilo». Construye una pista invisible y haz que un globo salga disparado como un cohete. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-03` — Mandala de sal de colores  ·  *Arte y manualidades*
- **Archivo:** `assets/images/6a8-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Mandala de sal de colores». Pinta la sal con tiza y crea un mosaico de colores que cabe en la palma de la mano. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-04` — La caja misteriosa al tacto  ·  *Sensorial*
- **Archivo:** `assets/images/6a8-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «La caja misteriosa al tacto». Mete la mano sin mirar y adivina qué objeto escondido estás tocando. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-05` — Circuito de obstáculos casero  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/6a8-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Circuito de obstáculos casero». Convierte el salón o el patio en una pista de saltos, túneles y equilibrio. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-06` — Bolos caseros con botellas  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/6a8-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Bolos caseros con botellas». Arma tu propia bolera con botellas y lanza para tumbarlas todas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-07` — Inventa tu juego de mesa  ·  *Juego*
- **Archivo:** `assets/images/6a8-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Inventa tu juego de mesa». Dibuja un tablero con tus propias reglas y rétate a llegar el primero a la meta. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-08` — Búsqueda del tesoro con pistas  ·  *Juego*
- **Archivo:** `assets/images/6a8-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Búsqueda del tesoro con pistas». Sigue un rastro de acertijos por la casa hasta encontrar el tesoro escondido. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-09` — El frasco de la calma  ·  *Conexión emocional*
- **Archivo:** `assets/images/6a8-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El frasco de la calma». Crea una galaxia de purpurina en un frasco para tranquilizarte cuando te enojas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-10` — Títeres de cartón con teatro  ·  *Arte y manualidades*
- **Archivo:** `assets/images/6a8-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Títeres de cartón con teatro». Da vida a unos personajes de cartón y monta tu propia función de marionetas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-11` — Diario de exploradores de la naturaleza  ·  *Naturaleza*
- **Archivo:** `assets/images/6a8-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Diario de exploradores de la naturaleza». Sal a la calle con lupa y cuaderno y conviértete en un explorador de la naturaleza. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-12` — El globo con electricidad mágica  ·  *Experimento*
- **Archivo:** `assets/images/6a8-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El globo con electricidad mágica». Frota un globo en tu pelo y haz que mueva cosas sin tocarlas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-13` — Cristales de sal que crecen solos  ·  *Experimento*
- **Archivo:** `assets/images/6a8-13.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Cristales de sal que crecen solos». Prepara agua muy salada y observa cómo, en pocos días, nacen cristales brillantes de la nada. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-14` — Lámpara de lava casera  ·  *Experimento*
- **Archivo:** `assets/images/6a8-14.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Lámpara de lava casera». Mezcla aceite, agua y una pastilla efervescente para ver burbujas de color que suben y bajan como lava. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-15` — Mensajes secretos con tinta invisible  ·  *Experimento*
- **Archivo:** `assets/images/6a8-15.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Mensajes secretos con tinta invisible». Escribe un mensaje con jugo de limón y míralo aparecer como por arte de magia con un poco de calor. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-16` — La masa que es líquida y sólida a la vez  ·  *Experimento*
- **Archivo:** `assets/images/6a8-16.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «La masa que es líquida y sólida a la vez». Prepara una mezcla de maicena y agua que se endurece si la golpeas y se derrite si la dejas quieta. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-17` — Los colores escondidos de los plumones  ·  *Experimento*
- **Archivo:** `assets/images/6a8-17.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Los colores escondidos de los plumones». Descubre que un plumón negro guarda varios colores escondidos que el agua puede separar. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-18` — El reloj de sol del patio  ·  *Experimento*
- **Archivo:** `assets/images/6a8-18.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El reloj de sol del patio». Construye un reloj con un palo y la sombra, y aprende a decir la hora mirando el cielo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-19` — El puente de papel que aguanta peso  ·  *Experimento*
- **Archivo:** `assets/images/6a8-19.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El puente de papel que aguanta peso». Descubre cómo una simple hoja de papel doblada puede sostener monedas sin caerse. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-20` — La planta que busca la luz  ·  *Naturaleza*
- **Archivo:** `assets/images/6a8-20.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «La planta que busca la luz». Cultiva un poroto y observa cómo el tallo se inclina solo hacia la ventana para buscar el sol. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-21` — La carrera de las estatuas  ·  *Juego*
- **Archivo:** `assets/images/6a8-21.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «La carrera de las estatuas». Avancen sin que los pillen moviéndose: cuando la música pare, todos quedan congelados como estatuas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-22` — Estampados con verduras  ·  *Arte y manualidades*
- **Archivo:** `assets/images/6a8-22.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Estampados con verduras». Convierte una papa o una betarraga en un sello y llena el papel de figuras de colores. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-23` — El termómetro de las emociones  ·  *Conexión emocional*
- **Archivo:** `assets/images/6a8-23.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El termómetro de las emociones». Dibuja un termómetro especial para medir cómo te sientes y aprender a calmarte cuando subes mucho. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-24` — Adivina la textura con los ojos cerrados  ·  *Sensorial*
- **Archivo:** `assets/images/6a8-24.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #7E57A6. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «Adivina la textura con los ojos cerrados». Mete la mano en una caja secreta y descubre solo con el tacto qué objeto estás tocando. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-25` — El globo a prueba de fuego  ·  *Experimento*
- **Archivo:** `assets/images/6a8-25.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El globo a prueba de fuego». Acerca una llama a un globo con agua adentro y descubre por qué no explota como uno con solo aire. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `6a8-26` — El paracaídas de juguete  ·  *Experimento*
- **Archivo:** `assets/images/6a8-26.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un niño o niña en edad escolar (6-8 años) realizando la actividad «El paracaídas de juguete». Construye un paracaídas con una bolsa e hilo y descubre cómo el aire frena la caída de un muñeco. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```


### 9 a 12 años

#### `9a12-01` — Cromatografía con plumones  ·  *Experimento*
- **Archivo:** `assets/images/9a12-01.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Cromatografía con plumones». Descubre que el negro de un plumón esconde muchos colores ocultos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-02` — Reloj de agua casero  ·  *Experimento*
- **Archivo:** `assets/images/9a12-02.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Reloj de agua casero». Mide el tiempo como en la antigüedad, solo con agua y gravedad. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-03` — Mensajes en código secreto  ·  *Juego*
- **Archivo:** `assets/images/9a12-03.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Mensajes en código secreto». Crea tu propio cifrado y envía mensajes que solo tu equipo podrá leer. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-04` — Escape room casero  ·  *Juego*
- **Archivo:** `assets/images/9a12-04.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Escape room casero». Diseña una sala de enigmas en casa y reta a tu familia a escapar. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-05` — Inventa tu juego de estrategia  ·  *Juego*
- **Archivo:** `assets/images/9a12-05.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Inventa tu juego de estrategia». Diseña desde cero un juego de mesa con tablero, reglas y fichas propias. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-06` — Circuito de retos y equilibrio  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/9a12-06.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Circuito de retos y equilibrio». Convierte el patio o el pasillo en una pista de obstáculos que pone a prueba tu cuerpo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-07` — Fabrica y aprende malabares  ·  *Recreativa / Motriz*
- **Archivo:** `assets/images/9a12-07.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #E8744F. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Fabrica y aprende malabares». Hazte tus propias pelotas y domina el arte de los tres lanzamientos. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-08` — Cápsula del tiempo  ·  *Conexión emocional*
- **Archivo:** `assets/images/9a12-08.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Cápsula del tiempo». Guarda un mensaje para tu yo del futuro y ábrelo dentro de un año. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-09` — Frasco de grandes conversaciones  ·  *Conexión emocional*
- **Archivo:** `assets/images/9a12-09.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Frasco de grandes conversaciones». Preguntas para hablar de verdad y descubrir lo que cada uno piensa y siente. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-10` — Crea tu propio cómic  ·  *Arte y manualidades*
- **Archivo:** `assets/images/9a12-10.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Crea tu propio cómic». Inventa una historia con viñetas, globos de diálogo y un héroe a tu medida. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-11` — Flipbook: animación sin pantalla  ·  *Arte y manualidades*
- **Archivo:** `assets/images/9a12-11.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Flipbook: animación sin pantalla». Da vida a tus dibujos creando una película de bolsillo que se mueve al pasar las hojas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-12` — Tu huerto en macetero  ·  *Naturaleza*
- **Archivo:** `assets/images/9a12-12.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Tu huerto en macetero». Cultiva tus propias plantas aromáticas y observa cómo crecen día a día. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-13` — Indicador de pH con repollo morado  ·  *Experimento*
- **Archivo:** `assets/images/9a12-13.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Indicador de pH con repollo morado». Crea un líquido mágico que cambia de color y te dice si algo es ácido o básico. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-14` — Extrae el ADN de una frutilla  ·  *Experimento*
- **Archivo:** `assets/images/9a12-14.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Extrae el ADN de una frutilla». Saca con tus propias manos el hilo de ADN que guarda toda la información de una frutilla. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-15` — Electroimán casero  ·  *Experimento*
- **Archivo:** `assets/images/9a12-15.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Electroimán casero». Convierte un clavo en un imán que puedes encender y apagar con una pila. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-16` — Cohete de vinagre y bicarbonato  ·  *Experimento*
- **Archivo:** `assets/images/9a12-16.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Cohete de vinagre y bicarbonato». Lanza un cohete al aire usando solo una reacción química y mucha presión. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-17` — El huevo flotante y la densidad  ·  *Experimento*
- **Archivo:** `assets/images/9a12-17.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «El huevo flotante y la densidad». Haz que un huevo flote en el agua sin tocarlo, solo cambiando el líquido. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-18` — Circuitos en serie y en paralelo  ·  *Experimento*
- **Archivo:** `assets/images/9a12-18.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Circuitos en serie y en paralelo». Arma tus propios circuitos y descubre por qué unas ampolletas brillan más que otras. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-19` — El péndulo y su ritmo secreto  ·  *Experimento*
- **Archivo:** `assets/images/9a12-19.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «El péndulo y su ritmo secreto». Descubre qué hace que un péndulo vaya más rápido o más lento, como un detective de la física. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-20` — El puente que resiste más peso  ·  *Experimento*
- **Archivo:** `assets/images/9a12-20.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «El puente que resiste más peso». Ponte el casco de ingeniero y construye un puente de papel que aguante todo el peso posible. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-21` — Diario de naturaleza y aves  ·  *Naturaleza*
- **Archivo:** `assets/images/9a12-21.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #5B9E4A. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Diario de naturaleza y aves». Conviértete en explorador y registra las aves y plantas de tu barrio como un científico de campo. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-22` — Torneo de estrategia con tablero casero  ·  *Juego*
- **Archivo:** `assets/images/9a12-22.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #2E7D5B. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Torneo de estrategia con tablero casero». Diseña y juega un torneo de estrategia donde gana quien piensa mejor sus jugadas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-23` — Diseña tu identidad visual  ·  *Arte y manualidades*
- **Archivo:** `assets/images/9a12-23.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #F2A03D. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Diseña tu identidad visual». Crea tu propio logo, colores y tipo de letra como un verdadero diseñador de marcas. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-24` — Termómetro de emociones  ·  *Conexión emocional*
- **Archivo:** `assets/images/9a12-24.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #D24D6E. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Termómetro de emociones». Construye un termómetro para medir y entender lo que sientes, igual que mides la temperatura. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-25` — Filtro de agua casero por capas  ·  *Experimento*
- **Archivo:** `assets/images/9a12-25.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Filtro de agua casero por capas». Construye un filtro con capas de piedras y arena y mira cómo el agua sucia sale mucho más limpia. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

#### `9a12-26` — Levadura que infla un globo  ·  *Experimento*
- **Archivo:** `assets/images/9a12-26.png`
- **Prompt:**

```text
Ilustración plana (flat vector) estilo libro infantil, cálida, amigable y moderna. Formas redondeadas simples, sombras muy suaves, líneas limpias. Fondo crema #FBF7F0, color de acento principal #3E6E94. Paleta cálida y natural (verde #2E7D5B, azul #3E6E94, coral #E8744F, ámbar #F2A03D). Composición horizontal (banner apaisado) con márgenes generosos. Inclusiva y diversa, segura y tierna. SIN texto, SIN palabras, SIN letras, SIN números, SIN logotipos. Tema: un preadolescente (9-12 años) realizando la actividad «Levadura que infla un globo». Despierta a una levadura dormida con azucar y mira como infla un globo ella sola. Muestra la acción de forma clara y simpática, con los materiales caseros característicos de la actividad.
```

