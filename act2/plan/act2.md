# Actividad 2. Implementación de un *chatbot* inteligente con Azure OpenAI

## Objetivos
*   Con esta actividad vas a conseguir **implementar un *chatbot* funcional** que utilice las API (interfaces de programación de aplicaciones) de inteligencia artificial generativa de Azure OpenAI.
*   A través de esta actividad podrás **configurar un entorno de desarrollo en Python** y conectar aplicaciones locales con servicios en la nube.
*   Podrás **personalizar las interacciones del *chatbot*** ajustando los parámetros de comportamiento (*temperature, max_tokens, top_p*, etc.).
*   Comprenderás cómo **optimizar el consumo de recursos y costes** mediante una gestión eficiente de tokens.

## Enunciado
Crea un archivo llamado `chatbot.py` en tu entorno de desarrollo local.

Implementa un *chatbot* que interactúe con el usuario utilizando la API de Azure OpenAI. El *chatbot* debe:
*   Configurarse con tu *endpoint* y clave API.
*   Permitir la entrada de texto del usuario en un bucle, respondiendo con base en el modelo configurado.
*   Terminar la ejecución si el usuario escribe «salir».

## Pautas de elaboración

### Configurar el entorno de Azure:
*   Accede al portal de Azure e inicia sesión.
*   Crea un recurso de Azure OpenAI y obtén las credenciales necesarias (clave API y *endpoint*).
*   Asigna un modelo (por ejemplo, GPT-3.5-turbo o GPT-4).

### Preparar el entorno de desarrollo:
*   Instala Python y Visual Studio Code.
*   Configura un entorno virtual (`python -m venv venv`) y actívalo.
*   Instala la biblioteca oficial de OpenAI (`pip install openai`).

### Desarrollar el *chatbot*:
*   Crea un archivo `chatbot.py` e implementa el código para conectarte a Azure OpenAI.
*   Define los roles del *chatbot* (*system, user, assistant*) en el código.
*   Personaliza los parámetros como *temperature, max_tokens* y *top_p*.

### Ejecutar pruebas:
*   Realiza diferentes consultas al *chatbot* y observa cómo los parámetros afectan las respuestas.
*   Documenta al menos **tres casos de uso diferentes** (por ejemplo: recomendaciones de libros, respuestas técnicas, generación creativa).

### Optimización y análisis de costes:
*   Usa herramientas como el calculador de precios de Azure para estimar el coste de las operaciones.
*   Propón estrategias para reducir los costes optimizando el uso de tokens.

## Extensión y formato
*   **Extensión:** mínimo cinco páginas.
*   **Formato:** fuente Calibri, tamaño 11, interlineado 1,5.
*   **Entrega:** en formato PDF.

## Rúbrica

| Implementación de un *chatbot* inteligente con Azure OpenAI | Descripción | Puntuación máxima (puntos) | Peso % |
| :--- | :--- | :---: | :---: |
| **Configuración correcta del entorno** | Azure configurado correctamente y claves API obtenidas. | 2 | 10 % |
| **Implementación técnica del *chatbot*** | Código funcional que incluye llamadas a Azure OpenAI y personalización de parámetros. | 3 | 20 % |
| **Documentación de pruebas** | Incluye al menos tres escenarios con capturas de pantalla y análisis de resultados. | 2 | 20 % |
| **Optimización de recursos** | Uso de herramientas para estimar costes y propuestas de optimización. | 2 | 20 % |
| **Formato y claridad** | El informe o las diapositivas cumplen con los requisitos de formato, claridad y organización. | 1 | 30 % |
| **TOTAL** | | **10** | **100 %** |
