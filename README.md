# Automatización de Pruebas Funcionales con Selenium – S.C

Este repositorio contiene dos scripts de automatización funcional en Python utilizando Selenium.

## Scripts incluidos

### 1. test_ingreso_sin_registro.py
Simula un usuario que accede como visitante pulsando el botón "Ingresar sin registro".
- Valida que se accede correctamente a la app.
- Envía un evento de tracking simulado a una API externa.

### 2. test_hacerse_socio.py
Simula un usuario que hace clic en "Hacerse socio".
- Verifica la llegada al formulario de alta.
- Envía un evento `POST` como simulación de intención de conversión.

## Requisitos

- Python 3.x
- Selenium
- Requests
- ChromeDriver instalado y en el PATH

## Instalación

```bash
pip install selenium requests
```

## Ejecución

```bash
python test_ingreso_sin_registro.py
python test_hacerse_socio.py
```

> ⚠️ Cambia las URLs a tu entorno real o de prueba.
