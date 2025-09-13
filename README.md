<h1 align="center">👋 &nbsp;¡Hola soy Mauro Echeverría! &nbsp;✨ </h1> 

<h2>Por que elegí VS Code &nbsp;😏</h2>

💡 &nbsp; Lo elegí por que es un editor de código muy recomendable por varias razones. Primero, es ligero y rápido, lo que significa que arranca casi al instante y consume pocos recursos de tu computadora, incluso con proyectos grandes. Su amplia colección de extensiones te permite personalizarlo para casi cualquier lenguaje de programación, framework o tarea, desde depuradores y linters hasta herramientas de gestión de bases de datos. Además, la integración con Git y GitHub está incorporada, haciendo que el control de versiones sea una parte fluida de tu flujo de trabajo. La terminal integrada es increíblemente útil, permitiéndote ejecutar comandos sin tener que cambiar de ventana. Finalmente, es completamente gratuito y de código abierto, con una comunidad masiva que contribuye a su mejora constante y a la creación de nuevas extensiones.

<h1>Paso para configuración de Proyecto U3</h1>

<h2>👨🏻‍💻 &nbsp; Crear repo local y rama de trabajo 😃</h2>

```
✍ Yo ya poseo una cuenta en GitHub por tal motivo lo cree por ese medio.

# Clone el repo y me situé en la rama de trabajo
▪git clone <URL-del-repo> u3-echeverria-mauro
▪cd u3-echeverria-mauro

# Creé la rama
▪git switch -c feat/u3-entregable
```

<h2>👨🏻‍💻 &nbsp; Comandos para reproducir el entorno &nbsp;😃</h2>
Para mi proyecto decidí utilizar <strong>venv</strong> ya que es recomendado si no necesitas binarios pesados.<br><br>

```
✍ Estas lineas de código se ejecutan en la terminal de PowerShell, en la ubicación del proyecto, en mi caso particular.

📒 C:\xampp\htdocs\GIT\u3-echeverria-mauro

▪ python -m venv u3-echeverria

# Activar en Windows PowerShell
▪ .\u3-echeverria\Scripts\Activate.ps1

▪ pip install --upgrade pip
▪ pip install numpy pandas matplotlib scikit-learn ipykernel pytest ruff black isort pre-commit nbstripout

# Registro de kernel -> Se adjunta captura de pantalla
▪ python -m ipykernel install --user --name "u3-echeverria" --display-name "Python 3.11 (u3-echeverria)"
```
📷 &nbsp; Captura de pantalla como evidencia. &nbsp;🔍
<img src="https://i.postimg.cc/FHBV4r2k/Screenshot-1.png" align="center" width = 400px/><br><br>
<img src="https://i.postimg.cc/RVGTgQdR/Screenshot-2.png" align="center" width = 400px/>


<h2>👨🏻‍💻 &nbsp; Gestión de dependencias 😃</h2>
Para ello elegí la opción de PIP Básico con el uso del archivo <strong>requirements.txt</strong><br>

```
✍ Dependencias en requirements.txt

numpy==2.3.*
pandas==2.3.*
matplotlib==3.10.*
scikit-learn==1.5.*
ipykernel==6.30.*
pytest==7.1.*
ruff==0.5.*
black==25.1.*
isort==6.0.*
pre-commit==3.7.*
nbstripout==0.8.*
detect-secrets==1.5.*
scikit-learn==1.7.*

✍ Comandos para ejecución tanto para DEV y PROD

# PROD
▪ pip install -r requirements.txt

# DEV
▪ pip install -r dev-requirements.txt
```
📷 &nbsp; Captura de pantalla como evidencia. &nbsp;🔍
<img src="https://i.postimg.cc/FHRV8dnQ/Screenshot-3.png" align="center" width = 400px/>


<h2>👨🏻‍💻 &nbsp; Ejecución de Pruebas 😃</h2>
Se realizaron los pasos indicados y se ejecutaron dos pruebas, se adjunta captura
📷 &nbsp; Captura de pantalla como evidencia. &nbsp;🔍
<img src="https://i.postimg.cc/qMpLcZsq/Screenshot-4.png" align="center" width = 400px/>


<h2>👨🏻‍💻 &nbsp; Calidad local con pre-commit 😃</h2>
Se realizaron los pasos indicados y se ejecutaron dos pruebas, se adjunta captura

```
▪ pip install pre-commit
▪ pre-commit install
▪ pre-commit run --all-files
```

📷 &nbsp; Captura de pantalla como evidencia. &nbsp;🔍
<img src="https://i.postimg.cc/1zqbqjSX/Screenshot-5.png" align="center" width = 400px/><br><br>
<img src="https://i.postimg.cc/wTGVNKzp/Screenshot-6.png" align="center" width = 400px/><br><br>
<img src="https://i.postimg.cc/SjF58VJ6/Screenshot-7.png.png" align="center" width = 400px/><br><br>
<img src="https://i.postimg.cc/kGtzBLXM/Screenshot-8.png" align="center" width = 400px/><br><br>
<img src="https://i.postimg.cc/KzWCcmbs/Screenshot-10.png" align="center" width = 400px/>

<h2>👨🏻‍💻 &nbsp; BONUS...!!! PIP-TOOLS, Badge de Cobertura😃</h2>
Con el fin de obtener el bonus de los 5pts, se logró realizar el uso de pip-tools y sus dependencias, se muestra lineas de codigo y capturas.

```
▪ pip install pip-tools
▪ pip install jupytext
▪ pip install mypy
▪ mypy src/
▪ pip install coverage pytest-cov
▪ pytest --cov=src --cov-report=xml

▪ Crea cuenta en https://about.codecov.io/ y conecta tu repo.
▪ Añadi este paso en .github/workflows/ci.yml después de pytest:
    - name: Run tests with coverage
        run: pytest --cov=src --cov-report=xml

    - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml

▪ Restart / Run All
```
📷 &nbsp; Captura de pantalla como evidencia. &nbsp;🔍<br><br>
**<ins>Importante:</ins> Se indica que se tuvo que colocar el repositorio de GIT como publico con el fin de poder tener acceso tanto al Bange de cobertura con al ambiente WEB Coverage**.<br><br>
<img src="https://github.com/MauroEcheverria/u3-echeverria-mauro/actions/workflows/ci.yml/badge.svg" align="center" width = 300px/>

<h3>🛠 &nbsp;Fue una tarea muy bien planteada pero larga y densa 😅</h3>

<img src="https://raw.githubusercontent.com/AVS1508/AVS1508/master/assets/Night-Coding.gif" width = 400px>