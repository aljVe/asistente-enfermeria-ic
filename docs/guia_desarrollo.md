# Guía de Desarrollo - Asistente de Enfermería para Insuficiencia Cardíaca

Este documento proporciona información técnica sobre la estructura y el funcionamiento interno de la aplicación, dirigida a desarrolladores que deseen entender, modificar o ampliar el código.

## Estructura del Código

La aplicación está desarrollada en Python utilizando el framework tkinter para la interfaz gráfica. El código sigue un patrón de diseño orientado a objetos con una clase principal `AplicacionInsuficienciaCardiaca` que gestiona toda la lógica de la aplicación.

### Clase Principal

```python
class AplicacionInsuficienciaCardiaca:
    def __init__(self, root):
        # Inicialización de la ventana principal y configuración
```

### Métodos Principales

| Método | Descripción |
|--------|-------------|
| `__init__(self, root)` | Constructor que inicializa la aplicación |
| `crear_variables(self)` | Crea las variables de control para los campos del formulario |
| `crear_interfaz(self)` | Construye los elementos visuales de la interfaz |
| `limpiar_formulario(self)` | Restablece todos los campos a sus valores predeterminados |
| `generar_informe(self)` | Inicia el proceso de generación del informe |
| `crear_texto_informe(self)` | Construye el texto estructurado del informe |
| `mostrar_informe(self, informe)` | Muestra el informe en una ventana modal |

## Flujo de Trabajo

1. **Inicialización**: Al ejecutar la aplicación, se crea una instancia de `Tk()` y se pasa a la clase principal.
2. **Configuración de la Interfaz**: Se configuran estilos, variables y se construye la interfaz gráfica.
3. **Interacción del Usuario**: El usuario completa los campos del formulario.
4. **Generación de Informe**: Al hacer clic en "Crear Informe", se recopilan los datos y se genera un texto estructurado.
5. **Visualización y Exportación**: El informe se muestra en una ventana modal con opciones para copiar o guardar.

## Gestión de Datos

### Variables de Control

La aplicación utiliza `StringVar` de tkinter para controlar los campos del formulario:

```python
def crear_variables(self):
    # Datos básicos
    self.estado_general_var = tk.StringVar()
    self.clase_nyha_var = tk.StringVar()
    # ...
```

### Estructura de la Interfaz

La interfaz se organiza en secciones mediante LabelFrames:

```python
# Marco para situación actual
situacion_frame = ttk.LabelFrame(self.scrollable_frame, text="Situación Actual")
situacion_frame.grid(row=1, column=0, columnspan=6, padx=10, pady=5, sticky="ew")
```

## Personalización y Extensión

### Añadir Nuevos Campos

Para añadir un nuevo campo al formulario:

1. Añada una nueva variable en `crear_variables()`
2. Cree los widgets correspondientes en `crear_interfaz()`
3. Incluya la lógica para procesar el nuevo campo en `crear_texto_informe()`

### Modificar la Estructura del Informe

El método `crear_texto_informe()` define la estructura y el contenido del informe generado. Para modificar el formato:

```python
def crear_texto_informe(self):
    # Inicio del informe
    informe = f"CONSULTA TELEFÓNICA DE ENFERMERÍA - INSUFICIENCIA CARDÍACA\n\n"
    
    # Personalice aquí el formato y contenido
```

## Mejores Prácticas

### Estilo de Código

- Siga las convenciones de PEP 8 para Python
- Utilice nombres descriptivos para variables y métodos
- Añada comentarios para explicar la lógica compleja

### Patrón de Diseño

La aplicación utiliza un patrón de diseño básico MVC (Modelo-Vista-Controlador):
- **Modelo**: Variables `StringVar` que mantienen el estado
- **Vista**: Widgets de la interfaz gráfica
- **Controlador**: Métodos que gestionan la lógica de la aplicación

### Consideraciones para Contribuciones

- Mantenga la coherencia con el diseño existente
- Pruebe exhaustivamente cualquier modificación
- Actualice la documentación correspondiente

## Roadmap para Futuras Versiones

### Posibles Mejoras

1. **Base de Datos**: Implementar almacenamiento persistente para historial de consultas
2. **Exportación Avanzada**: Añadir opciones para exportar a formatos como PDF o integrarse con HCE
3. **Análisis de Tendencias**: Permitir visualización de la evolución de parámetros
4. **Alertas Automáticas**: Implementar sistema de alertas basado en parámetros críticos
5. **Validación de Datos**: Añadir validación más robusta para los campos numéricos

## Depuración

Para facilitar la depuración, puede añadir mensajes de registro:

```python
import logging

# Configurar registro
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   filename='app_debug.log')

# Usar en el código
logging.debug('Valor de variable X: %s', self.variable_x)
```

## Contacto para Desarrollo

Para consultas técnicas o contribuciones al código:
- Email: [alejandro2196vr@gmail.com](mailto:alejandro2196vr@gmail.com)
- GitHub: Abra un issue en el repositorio