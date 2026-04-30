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

## 14) 2026-04-29 20:07 (UTC+2) - Validaciones en opción 4 (Asociar contrato)

**Pregunta:** Si selecciono la opción 4 y pongo un ID de empleado que no existe, no debería pedir fechas; debería mostrar "Empleado no encontrado.". Tampoco debe dejar introducir fechas no válidas y el error debe saltar antes de `could not convert string to float: 'x'`.  
**Respuesta:** Se corrigió `main.py` para validar primero si el empleado existe antes de solicitar fechas. También se añadió validación de fechas (`YYYY-MM-DD` y orden inicio/fin) antes de pedir o convertir el salario. Resultado: con ID inexistente muestra `Empleado no encontrado.`, y con fecha inválida muestra error de formato sin llegar al fallo de conversión de `float`.

## 15) 2026-04-30 06:39 (UTC+2) - Nueva opción de menú

**Pregunta:** Añade la opción "Listar contratos activos".  
**Respuesta:** Se actualizó `main.py` con la opción `6` para listar contratos activos y la salida pasó a opción `7`; también se añadió un test para `listar_contratos_activos()` y la suite quedó en `5 passed`.

## 16) 2026-04-30 06:41 (UTC+2) - Ejecutar skill de comentarios

**Pregunta:** Ejecuta `@.cursor/skills/update-code-comments/SKILL.md`.  
**Respuesta:** Se revisaron comentarios y docstrings de `act1`; no se necesitaron cambios porque ya eran claros, breves y no redundantes.

## 17) 2026-04-30 06:41 (UTC+2) - Ejecutar skill de documentación

**Pregunta:** Ejecuta `@.cursor/skills/update-documentation/SKILL.md`.  
**Respuesta:** Se actualizaron `act1/README.md` y `act1/README_es.md` para reflejar el estado actual: comando de pruebas recomendado (`py -m pytest`) y opciones de menú nuevas (`6` contratos activos, `7` salir).

## 18) 2026-04-30 06:42 (UTC+2) - Regenerar ZIP con archivos adicionales

**Pregunta:** Genera un nuevo ZIP, incluyendo `@act1/empleados.json` y `@README_es.md`.  
**Respuesta:** Se regeneró `act1/actmod2_nombre_apellido.zip` incluyendo ambos archivos de forma explícita y se verificó el contenido final.

