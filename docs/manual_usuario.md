# Manual de Usuario - Asistente de Enfermería para Insuficiencia Cardíaca

Este manual proporciona instrucciones detalladas para el uso efectivo del Asistente de Enfermería para Insuficiencia Cardíaca.

## Índice

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Descripción de la Interfaz](#descripción-de-la-interfaz)
5. [Funcionalidades](#funcionalidades)
6. [Guía Paso a Paso](#guía-paso-a-paso)
7. [Generación de Informes](#generación-de-informes)
8. [Solución de Problemas](#solución-de-problemas)
9. [Consideraciones Clínicas](#consideraciones-clínicas)
10. [Contacto y Soporte](#contacto-y-soporte)

## Introducción

El Asistente de Enfermería para Insuficiencia Cardíaca es una herramienta diseñada para facilitar el seguimiento telefónico de pacientes con insuficiencia cardíaca. Permite estructurar la consulta, recopilar datos clínicos relevantes y generar informes estandarizados para el registro en la historia clínica.

## Requisitos del Sistema

- **Sistema Operativo**: Windows 10/11, macOS 10.14 o superior, o Linux con entorno gráfico
- **Python**: Versión 3.6 o superior si se ejecuta desde Python.
- **Espacio en Disco**: Mínimo 10 MB libres
- **RAM**: Mínimo 256 MB disponibles
- **Resolución de Pantalla**: Recomendado 1280x720 o superior

## Instalación y ejecución desde Python.

1. Asegúrese de tener Python instalado:
   - Windows: Descargue Python desde [python.org](https://www.python.org/downloads/)
   - macOS: Instale a través de Homebrew con `brew install python`
   - Linux: Use su gestor de paquetes (ej: `sudo apt install python3`)

2. Descargue la aplicación:
   - Directamente desde GitHub
   - O mediante Git: `git clone https://github.com/su-usuario/asistente-enfermeria-ic.git`

3. Ejecute la aplicación:
   - Navegue hasta la carpeta del programa
   - Ejecute `python Asistente_Enfermeria_IC_v_1_2.py`

## Instalación y ejecución mediante programa ejecutable:
1. Descargue el archivo Asistente_Enfermeria_IC_1_2.exe
2. Ejecútelo.

## Descripción de la Interfaz

La interfaz se divide en cinco secciones principales:

### Situación Actual
Recoge datos básicos como estado general, clase funcional NYHA, constantes vitales y peso.

### Autocuidados
Evalúa el cumplimiento de las medidas recomendadas: control de peso, ingesta de líquidos, restricción de sal, adherencia al tratamiento, etc.

### Signos de Alarma
Registra la presencia de síntomas de descompensación: aumento de peso, edemas, disnea, etc.

### Tratamiento y Observaciones
Documenta el tratamiento diurético actual, posibles causas desencadenantes y observaciones adicionales.

### Botones de Acción
Permiten generar el informe o limpiar el formulario.

## Funcionalidades

### Recopilación de Datos
- Selección mediante menús desplegables
- Botones de radio para respuestas Sí/No/No Sabe
- Campos de texto para información adicional

### Gestión de Informes
- Generación automática de informes estructurados
- Copia al portapapeles
- Guardado como archivo de texto en el escritorio

## Guía Paso a Paso

### 1. Inicio de la Aplicación
- Ejecute el archivo `Asistente_Enfermeria_IC_v_1_2.py`
- Se abrirá la ventana principal con el formulario

### 2. Completar el Formulario
- **Situación Actual**: Registre estado general, clase NYHA, constantes y peso
- **Autocuidados**: Marque Sí/No/NS según corresponda para cada ítem
- **Signos de Alarma**: Indique la presencia o ausencia de signos de descompensación
- **Tratamiento**: Documente el tratamiento diurético actual
- **Observaciones**: Añada información adicional relevante

### 3. Generar Informe
- Haga clic en "Crear Informe"
- Revise el informe generado
- Utilice las opciones para copiar o guardar

## Generación de Informes

### Estructura del Informe
El informe generado incluye:
- Título y encabezado
- Sección de situación actual
- Resumen de autocuidados (positivos y negativos)
- Signos y síntomas presentes y ausentes
- Tratamiento actual
- Valoración y observaciones

### Opciones de Exportación
- **Copiar al portapapeles**: Para pegar en la historia clínica electrónica
- **Guardar como archivo**: Crea un archivo txt en el escritorio con el nombre "Consulta_IC_[fecha]_[hora].txt"

## Solución de Problemas

### Problemas Comunes
- **La aplicación no se inicia**: Verifique la instalación de Python y tkinter si se ejecuta desde Python.
- **Error al guardar el informe**: Compruebe los permisos de escritura en el escritorio
- **Interfaz incompleta**: Asegúrese de tener una resolución de pantalla adecuada

### Contacto para Soporte
Si encuentra problemas, contacte con [alejandro2196vr@gmail.com](mailto:alejandro2196vr@gmail.com)

## Consideraciones Clínicas

Esta herramienta está diseñada como apoyo a la consulta telefónica de enfermería, pero no sustituye el juicio clínico del profesional. Los criterios para determinar la necesidad de valoración médica deben basarse en los protocolos específicos de cada centro.

## Contacto y Soporte

Para consultas, sugerencias o notificación de errores:
- Email: [alejandro2196vr@gmail.com](mailto:alejandro2196vr@gmail.com)
- GitHub: Abra un issue en el repositorio