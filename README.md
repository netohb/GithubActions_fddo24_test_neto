# GithubActions_fddo24
Este repositorio contiene el proyecto de github actions para la materia de Fuentes de Datos Otoño 2024.

## Integrantes
- Alberto Márquez
- Ernesto Bernal
- Andre Herrera

## Instrucciones para correr el proyecto
###  Hacer un Fork del repostorio
Haz clic en el botón Fork ubicado en la esquina superior derecha del repositorio en GitHub. Esto es necesario para que puedas subir tu tarea. A continuación, elige un nombre para tu fork (te recomendamos utilizar pGithubActions_fddo24_test_tuusuario) y selecciona la opción para copiar únicamente la rama master o main. De esta manera, tendrás una copia (fork) de nuestro repositorio en tu cuenta de GitHub, desde la cual podrás clonar el proyecto y realizar un pull request para enviar tu tarea.

### Clonar el repositorio desde GitHub
Dirigete a la carpeta donde deseas guardar el proyecto y clona tu fork con: 
```bash
glit clone git@github.com:AlbertoMarquez794/GithubActions_fddo24_test_tusuario.git
```
Sustituye "tuusuario" por el nombre. 
Ahora accede a tu carpeta
```bash
cd GithubActions_fddo24_test_tusuario
```
Recomendamos configurar el upstreaam para poder traer los últimos cambios. 
```bash
git remote add upstream git@github.com:AlbertoMarquez794/GithubActions_fddo24_test.git
```
Tendrás todos los documentos listos para la presentación.
## Estructura del Proyecto
```plaintext
GithubActions_ffdo24_test/
├── .github/workflows        # Contiene el código de los workflows
├── documentacion/           # Contiene el material para la explicación de sphinx
├── testing                  # Carpeta para probar un workflow de testeo
├── verificacion             # Contiene el material para la explicación de cómo funciona el flake8
├── README.md                # Documentación, instrucciones.
└── requirements.txt         # Requerimientos para sphinx y flake8.
```
## Tarea
