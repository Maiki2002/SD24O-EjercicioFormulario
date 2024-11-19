# Actividad de clase

### Descripción
Este proyecto es una API creada con **FastAPI** que permite gestionar fotos de usuarios. Los usuarios pueden enviar sus datos y una fotografía, y esta se almacena en carpetas específicas según si el usuario es VIP o no.

### Requisitos previos
- **Python 3.8 o superior**
- **Pip** (administrador de paquetes de Python)
- Un entorno virtual recomendado: conda
- **FastAPI**
- **Uvicorn** para ejecutar el servidor

```
pip install fastapi uvicorn
```

Para ejecutar este programa se necesita crear dos carpetas en la ruta raíz:
 - fotos-usuarios
 - fotos-usuarios-vip

### Ejecución del programa
```
uvicorn api:app --reload 
```
