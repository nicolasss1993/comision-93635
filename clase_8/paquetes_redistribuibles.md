# *Crear un Paquete Redistribuible en Python*

## *📌 1. Estructura del Proyecto*

*Organiza tu código en una estructura adecuada:*

```
mi_paquete/
│── mi_paquete/
│   ├── __init__.py
│   ├── modulo1.py
│   ├── modulo2.py
│── setup.py
```

---

## *📌 2. Escribir el Código del Paquete*

*Ejemplo de un módulo (**``**):*

```python
def hola_mundo():
    return "¡Hola, mundo!"
```

*Asegúrate de incluir **``** en **``** para que Python lo reconozca como paquete.*

```python
# mi_paquete/__init__.py
from .modulo1 import hola_mundo
```

---

## *📌 3. Agregar un **``** (Opcional, Usar **``** Preferiblemente)*

*Si quieres usar **``**, crea un archivo en la raíz:*

```python
from setuptools import setup, find_packages

setup(
    name="mi_paquete",
    version="0.1.0",
    packages=find_packages(),
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Un paquete de ejemplo en Python",
    python_requires=">=3.6",
)
```


---
## *📌 5.1 Construcción del Paquete*

*Desde la raíz del proyecto, ejecuta:*

```sh
python setup.py sdist
```

*Esto generará los archivos **``** y **``** en la carpeta **``**.*

---

<!-- ## *📌 5.2 Construcción del Paquete*

*Desde la raíz del proyecto, instala **``** y ejecuta:*

```sh
pip install build
python -m build
```

*Esto generará los archivos **``** y **``** en la carpeta **``**.*

---

## *📌 6. Subir el Paquete a PyPI*

*1️⃣ Instala **``** si no lo tienes:*

```sh
pip install twine
```

*2️⃣ Sube el paquete a ****TestPyPI**** (para pruebas):*

```sh
twine upload --repository testpypi dist/*
```

*3️⃣ O súbelo a ****PyPI**** (para distribución real):*

```sh
twine upload dist/*
```

---

## *📌 7. Instalar tu Paquete*

*Si lo subiste a TestPyPI:*

```sh
pip install --index-url https://test.pypi.org/simple/ mi_paquete
```

*Si está en PyPI:*

```sh
pip install mi_paquete
```

---

¡Con esto, tu paquete ya es redistribuible y cualquiera lo puede instalar con `pip` desde PyPI 🚀! -->
