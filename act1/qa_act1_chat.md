# Preguntas y respuestas sobre act1 (orden cronológico)

## 1) 2026-04-26 16:35 (UTC+2) - Ejecutar el plan de `act1`

**Pregunta:** Ejecuta `@act1/plan/plan.md`.  
**Respuesta:** Ejecuté el plan completo en `act1`, creé los módulos, datos, tests y README, y validé con `pytest` (`4 passed`).

## 2) 2026-04-26 16:38 (UTC+2) - Contenido del ZIP de entrega

**Pregunta:** Dime qué archivos debe contener `actmod2_nombre_apellido.zip` en `@act1/`.  
**Respuesta:** Te indiqué incluir: `gestor_empleados.py`, `gestor_contratos.py`, `main.py`, `empleados.json`, `README.md` y `tests/test_gestor_empleados.py`; no incluir `act1.docx` ni `plan/plan.md`.

## 3) 2026-04-26 16:47 (UTC+2) - README en español y enlaces cruzados

**Pregunta:** Crea `README_es.md` y que `README.md` tenga enlace al mismo en la primera línea, y viceversa.  
**Respuesta:** Creé `act1/README_es.md` y añadí enlaces cruzados en la primera línea de ambos archivos.

## 4) 2026-04-26 16:48 (UTC+2) - Estilo de mensajes en consola

**Pregunta:** Añade estilo verde para mensajes de éxito y rojo para mensajes de error en consola, con icono; también información si hace falta.  
**Respuesta:** Actualicé `main.py` con helpers de salida para éxito/error/info usando color ANSI e iconos (`✅`, `❌`, `ℹ️`).

## 5) 2026-04-26 16:49 (UTC+2) - Aplicación de cambios en ejecución

**Pregunta:** ¿Tengo que reiniciar para verlo? ¿Cómo?  
**Respuesta:** Te indiqué que no hace falta reiniciar PC ni Cursor; solo relanzar `python main.py` (o cerrar el proceso actual con opción `6` / `Ctrl + C` y volver a ejecutar).

## 6) 2026-04-26 16:50 (UTC+2) - Opción inválida sin formato

**Pregunta:** Si selecciono una opción que no existe, dice opción no válida, sin color/icono.  
**Respuesta:** Hice la salida más robusta en Windows inicializando `colorama` y añadiendo prefijos `[SUCCESS]`, `[ERROR]`, `[INFO]` para que siempre se distingan los mensajes.

## 7) 2026-04-26 16:52 (UTC+2) - Validación de criterios de rúbrica

**Pregunta:** Confirma si se cumplen estos criterios (gestor empleados, gestor contratos, fichero de entrada + terminal, pruebas, README).  
**Respuesta:** Confirmé que los 5 criterios se cumplen y señalé los archivos correspondientes en `act1`.

## 8) 2026-04-26 17:03 (UTC+2) - ZIP de entrega y exclusión en Git

**Pregunta:** Genera `@act1/actmod2_nombre_apellido.zip` solo con los ficheros necesarios y añádelo a `.gitignore`.  
**Respuesta:** Generé el ZIP con solo los archivos requeridos y añadí `act1/actmod2_nombre_apellido.zip` a `.gitignore`.

## 9) 2026-04-26 17:33 (UTC+2) - Comando para lanzar tests

**Pregunta:** Dime qué comando debo ejecutar para lanzar los tests.  
**Respuesta:** Desde la carpeta `act1`, ejecuta:

```bash
pytest
```

Si `pytest` no está en `PATH`, usa:

```bash
py -m pytest
```

## 10) 2026-04-26 17:36 (UTC+2) - Error al ejecutar `pytest` desde `act1/`

**Pregunta:** `pytest` desde `act1/` da error.  
**Respuesta:** Se reprodujo un error de imports con `pytest` directo en el entorno. Comando recomendado:

```bash
py -m pytest
```

Resultado verificado: tests pasando (`4 passed`). Opcional para evitar warning de caché:

```bash
py -m pytest -p no:cacheprovider
```

## 11) 2026-04-26 17:36 (UTC+2) - Ubicación de `test_gestor_empleados.py`

**Pregunta:** ¿Da igual que `test_gestor_empleados.py` esté en carpeta `tests` o no?  
**Respuesta:** No da igual. Aunque puede funcionar fuera, la convención recomendada es mantener los tests en `tests/` para facilitar descubrimiento, ejecución y mantenimiento. En `act1`, dejar `test_gestor_empleados.py` en `act1/tests/` es lo correcto.

## 12) 2026-04-28 19:34 (UTC+2) - Añadir preguntas e instrucciones anteriores

**Pregunta:** Crea un fichero .md en `@act1` con preguntas y peticiones relacionadas con act1 que te he hecho y tus respuestas.  
**Respuesta:** Se creo el fichero `act1/qa_act1_chat.md` con tus preguntas sobre act1 y mis respuestas en formato Q&A.

## 13) 2026-04-28 19:35 (UTC+2) - Orden cronológico con fecha/hora

**Pregunta:** Ordénalo cronológicamente con fecha/hora en cada entrada.  
**Respuesta:** Documento reorganizado en orden cronológico y cada entrada etiquetada con fecha y hora.

