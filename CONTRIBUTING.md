# Guía de Contribución

¡Gracias por su interés en contribuir al Asistente de Enfermería para Insuficiencia Cardíaca! Este documento proporciona las pautas y mejores prácticas para contribuir a este proyecto.

## Código de Conducta

Al participar en este proyecto, usted se compromete a mantener un comportamiento profesional y respetuoso con todos los colaboradores. No se tolerará ninguna forma de acoso o comportamiento inapropiado.

## Proceso de Contribución

### 1. Encontrar o Crear un Issue

Antes de realizar cambios, verifique si ya existe un issue relacionado con su contribución. Si no existe, puede crear uno nuevo describiendo el problema o la mejora que desea implementar.

### 2. Bifurcar el Repositorio (Fork)

Cree su propia copia del repositorio haciendo un "fork" a través de la interfaz de GitHub.

### 3. Crear una Rama (Branch)

Cree una rama específica para su contribución:

```bash
git checkout -b nombre-de-la-caracteristica
```

Utilice un nombre descriptivo que refleje los cambios que va a realizar.

### 4. Realizar Cambios

Implemente sus cambios siguiendo las convenciones de estilo del código existente:

- Utilice 4 espacios para la indentación
- Siga las [PEP 8](https://www.python.org/dev/peps/pep-0008/) para el código Python
- Incluya comentarios claros y concisos
- Actualice la documentación si es necesario

### 5. Probar los Cambios

Asegúrese de que sus cambios funcionan correctamente y no introducen nuevos problemas.

### 6. Commit y Push

Realice un commit de sus cambios con un mensaje descriptivo:

```bash
git commit -m "Añadir: funcionalidad X para resolver el problema Y"
```

Suba los cambios a su repositorio:

```bash
git push origin nombre-de-la-caracteristica
```

### 7. Crear un Pull Request

Vaya a su repositorio en GitHub y cree un Pull Request hacia el repositorio original. Proporcione una descripción clara de los cambios realizados y referencie cualquier issue relacionado.

## Pautas Específicas

### Cambios en la Interfaz de Usuario

- Mantenga la consistencia con el diseño actual
- Considere la usabilidad para el personal sanitario
- Asegúrese de que los nuevos elementos se adaptan al diseño responsivo

### Cambios en la Lógica de Negocio

- Cualquier cambio en la lógica clínica debe estar respaldado por referencias a guías clínicas actualizadas
- Documente la justificación de los cambios en los parámetros clínicos

### Seguridad y Privacidad

- No incluya datos reales de pacientes en ejemplos o pruebas
- Priorice siempre la seguridad y la privacidad en el diseño de nuevas características

## Proceso de Revisión

Todos los Pull Requests serán revisados por los mantenedores del proyecto. Durante este proceso:

1. Verificaremos que el código cumple con nuestras pautas
2. Probaremos la funcionalidad
3. Sugeriremos cambios si es necesario
4. Aprobaremos y fusionaremos el PR cuando esté listo

## Contacto

Si tiene preguntas o necesita ayuda, no dude en contactar con el autor principal a través de [alejandro2196vr@gmail.com](mailto:alejandro2196vr@gmail.com).

¡Gracias por contribuir a mejorar la atención de pacientes con insuficiencia cardíaca!