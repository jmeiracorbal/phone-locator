# Phone Locator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![uv](https://img.shields.io/badge/uv-managed-blue.svg)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](https://github.com/jmeiracorbal/phone-locator)

Una herramienta de línea de comandos para obtener información detallada sobre números de teléfono. Descubre ubicación, operador, zona horaria y otros detalles de cualquier número telefónico.

## Características

- **Análisis de números telefónicos** - Información completa sobre cualquier número
- **Detección de país y región** - País, región, ciudad y coordenadas
- **Detalles del operador** - Operador móvil e información del proveedor
- **Identificación de zona horaria** - Encuentra automáticamente la zona horaria correcta
- **Validación de números** - Verifica si los números son válidos y posibles
- **Conversión de formatos** - Formatos internacional, nacional, E.164
- **Interfaz limpia** - Salida en terminal con colores

## Instalación

### Opción 1: Instalar como comando

Instalar directamente desde el repositorio:

```bash
pip install git+https://github.com/jmeiracorbal/phone-locator.git
```

O clonar e instalar localmente:

```bash
git clone https://github.com/jmeiracorbal/phone-locator.git
cd phone-locator
pip install .
```

Después de la instalación, ejecutar desde cualquier lugar:

```bash
phone-locator
```

### Opción 2: Descargar ejecutable pre-compilado

1. Ve a [Releases](https://github.com/jmeiracorbal/phone-locator/releases)
2. Descarga el ejecutable para tu plataforma:
   - **Linux**: `phone-locator` (binario)
   - **macOS**: `phone-locator` (binario)
   - **Windows**: `phone-locator.exe` (ejecutable)
3. Ejecuta directamente sin instalación

**Linux/macOS:**

```bash
chmod +x phone-locator
./phone-locator
```

**Windows:**

```cmd
phone-locator.exe
```

### Opción 3: Ejecutar con uv (para desarrollo)

```bash
git clone https://github.com/jmeiracorbal/phone-locator.git
cd phone-locator
uv run python main.py
```

## Uso

Después de la instalación o ejecutar el binario, ingresa un código de país y número telefónico para obtener información detallada incluyendo ubicación, operador, zona horaria y validez.

## Requisitos

- Python 3.8 o superior
- Conexión a Internet (para búsqueda de operador)

## Fuente de Datos

Esta herramienta utiliza la librería `phonenumbers` de Google para analizar y validar números telefónicos con metadatos completos.

## Contribuir

1. Haz fork del repositorio
2. Crea una rama de característica (`git checkout -b feature/caracteristica-increible`)
3. Haz commit de tus cambios (`git commit -m 'Agrega característica increíble'`)
4. Haz push a la rama (`git push origin feature/caracteristica-increible`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- **Autor original**: [HUNXBYTS](https://github.com/HUNXBYTS)
- **Modificado por**: [jmeiracorbal](https://github.com/jmeiracorbal)
- **Basado en**: Herramienta Ghost Tracker

## Soporte

Si encuentras algún problema o tienes preguntas:
- Crea un issue en GitHub
- Revisa la página de [Releases](https://github.com/jmeiracorbal/phone-locator/releases) para la última versión

---

**Nota**: Esta herramienta es para propósitos educativos y legítimos. Respeta la privacidad y úsala de manera responsable.
