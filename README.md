# PPS05 - Procesamiento de Cadenas de Texto

## 1. Información General

Este proyecto consiste en el desarrollo de un módulo en Python para el procesamiento de 
cadenas de texto. Su funcionalidad principal es determinar la cadena más larga dentro de una 
lista de palabras.

En caso de empate entre varias cadenas con la misma longitud, el sistema devuelve la primera 
en orden alfabético. Además, se incluyen validaciones de entrada para garantizar que los 
datos proporcionados sean correctos.

El proyecto incorpora también pruebas unitarias para verificar el correcto funcionamiento de 
la lógica implementada.

### Tecnologías utilizadas

- Python 3.x  
- Biblioteca estándar `typing`  
- Framework de pruebas `unittest`  
- Git (control de versiones)  
- Sistema operativo: macOS  

---

## 2. Guía de despliegue

### Requisitos previos

- Tener instalado Python 3  

### Ejecución del programa

1. Acceder al directorio del proyecto:


    cd pps05-tarea

2. Ejecutar el programa:


    python3 mychar.py

El programa solicitará al usuario la introducción de varias palabras y devolverá la cadena 
más larga según los criterios definidos.

### Ejecución de pruebas unitarias

    python3 test_mychar.py

Este comando ejecuta los tests definidos para validar el comportamiento de la función 
principal.

---

## 3. Tabla de trazabilidad

| Fecha       | Versión | Descripción                                      |
|------------|--------|--------------------------------------------------|
| 2025-10-05 | v1.0   | Desarrollo inicial del módulo                    |
| 2026-04-19 | v1.1   | Inicialización del repositorio Git               |
| 2026-04-19 | v1.2   | Implementación de estrategia de ramas            |
| 2026-04-19 | v1.3   | Fusión de cambios (merge)                        |
| 2026-04-19 | v1.4   | Creación del README y documentación técnica      |

---

## 4. Checklist de seguridad

### Archivos y elementos a proteger o ignorar

- `*.log`  
  Evita la exposición de información de depuración  

- `.venv/`, `env/`  
  Evita incluir entornos virtuales innecesarios  

- `__pycache__/`  
  Evita almacenar archivos compilados de Python  

- `*.sqlite3`  
  Evita subir bases de datos locales con posible información sensible  

### Justificación técnica

La exclusión de estos elementos permite:

- Reducir el riesgo de fuga de información sensible  
- Mantener el repositorio limpio y organizado  
- Evitar la exposición de datos temporales o de depuración  
- Mejorar la seguridad en procesos de despliegue  

---

## 5. Autor

José María García Moreno  
Curso de Especialización en Ciberseguridad  
Puesta en Producción Segura
