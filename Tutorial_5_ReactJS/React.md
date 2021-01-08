React es una libreria de Javascript focalizada en el desarrollo de interfaces de usuario con el objetivo de facilitar el desarrollo de aplicaciones en una sola página. React sólo maneja la interfaz de usuario en una aplicación. React es la Vista en un contexto en el que se use el patrón MVC (Modelo-Vista-Controlador).

Para poder instalar React en tu computadora, se debe instalar previamente npm (Node Package Manager), la cual es una herramienta de gestión de dependencias para la aplicación de Javascript, que ayuda a instalar todas las bibliotecas y otras herramientas para apoyar el desarrollo de la aplicación JS.

Para instalar npm debemos ejecutar la siguiente linea de comando:

    sudo apt install npm

Podemos verificar la versión de npm installada escribiendo:

    npm -v

y además podremos ver la versión de node que se ha instalado escribiendo:

    node -v

En este caso la versión de Node debe ser mayor a la 10, y en caso de no ser así podemos upgradearla escribiendo el siguiente comando:

    sudo npm install -g npm@latest

Una vez instalado necesitaremos configurar herramientas como babel, webpack, etc, para el entorno de desarrollo productivo de React, para lo cual podemos encontrar varias herramientas que ayudarán a esto, pero entre ellas, create-react-app es la más fácil y mejor para configurar.

Podemos installar create-react-app utilizando npm. Para esto debemos escribir lo siguiente:

    sudo npm install -g create-react-app

Podemos ver también la versión que hemos instalado de create-react-app, a través del comando:

    create-react-app --version


Una vez instalado todo esto podemos crear nuestro primer proyecto de React, simplemente utilizando la siguiente linea de comando:

    create-react-app mi_primera_app

(cabe destacar que el nombre que elegimos fue "mi_primera_app", la cual considera que create-react-app no acepta letras mayúsculas en el nombre del proyecto)

Despues de ejecutar este comando (y luego de un tiempo relativamente extenso) tendremos una carpeta llamada "mi_primera_app", la cual tendrá todos los elementos básicos necesarios para que nuestra app pueda funcionar, esta incluye los archivos, configuraciones y librerias necesarias dentro de las carpetas que contiene.

Podemos observar (si es que todo se ha ejecutado correctamente) que se muestra lo siguiente:

    Success! Created mi_primera_app at /home/manuel/Escritorio/Universidad/INFO229/Tutoriales/Tutorial_5_ReactJS/mi_primera_app
    Inside that directory, you can run several commands:

    npm start
        Starts the development server.

    npm run build
        Bundles the app into static files for production.

    npm test
        Starts the test runner.

    npm run eject
        Removes this tool and copies build dependencies, configuration files
        and scripts into the app directory. If you do this, you can’t go back!

    We suggest that you begin by typing:

    cd mi_primera_app
    npm start

    Happy hacking!

dentro de la cual podemos ejecutar el comando:
    cd mi_primera_app
y ver el contenido de la carpeta escribiendo:
    ls

y si escribimos la siguiente linea de comando (y tenemos instalado visual studio code):
    code README.md
podremos ver las instrucciones que se sugieren para poder trabajar y configurar algunas cosas, especificando para qué sirve cada una de estas sentencias.

Para continuar y ver nuestra aplicación escribiremos:

    npm start

y veremos que en nuestro navegador predeterminado se ejecuta nuestra aplicación en localhost, en el puerto 3000, que es el que viene por defecto.

Podemos detener esta ejecución simplemente presionando CTRL+C en la consola.

Para poder crear nuestro "Hola mundo" debemos acceder a la carpeta src, que contiene todos los recursos que utiliza nuestra app, especificamente al archivo App.js.
Para lo cual ejecutaremos los siguientes comandos en otra terminal, para que no se deje de ejecutar nuestra app:

    cd src
    code App.js

Aqui podemos ver las componentes que se muestran en la aplicación que se encuentra ejecutandose en nuestro escritorio, en el cual debiesemos ver algo como esto:

    import logo from './logo.svg';
    import './App.css';

    function App() {
    return (
        <div className="App">
        <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
            Edit <code>src/App.js</code> and save to reload.
            </p>
            <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
            >
            Learn React
            </a>
        </header>
        </div>
    );
    }

    export default App;

Si utilizamos el inspector de elementos en el navegador podremos ver este mismo codigo. (CTRL+SHIFT+C)

Podemos ver que el logo que gira corresponde a la linea de código:
    <img src={logo} className="App-logo" alt="logo" />
la cual contiene una clase llamada "App-logo" que podemos encontrar en el fichero App.css, en donde se definen sus características y su movimiento, en las siguientes lineas:

    .App-logo {
    height: 40vmin;
    pointer-events: none;
    }

    @media (prefers-reduced-motion: no-preference) {
    .App-logo {
        animation: App-logo-spin infinite 20s linear;
    }
    }

podemos ver esto escribiendo en la consola:

    code App.css

pero lo que nos convoca en esta ocasión es el texto que contiene nuestra app, que según el inspector corresponde a las linea de codigo:

    <p>
        Edit <code>src/App.js</code> and save to reload.
    </p>

que se encuentran en App.js, las cuales podemos borrar y dejar de la siguiente forma:

    <p>
        ¡¡¡Hola mundo!!!
    </p>

y si guardamos presionando CTRL+S y vamos a nuestro navegador podemos ver que se ha actualizado el texto sin la necesidad de detener la ejecución de la app en el localhost:3000. Es por eso que se le ha dado el nombre de React a este framework, ya que "reacciona" a los cambios que se vayan haciendo, ejecutando inmediatamente estos, sin la necesidad de perder tiempo cargando todas las dependencias para su nueva ejecución.

Con esto tenemos nuestra app "Hola mundo!" y así finaliza este tutorial.

Se recomienda revisar otros elementos modificables y agregables en base a las necesidades que vayan surgiendo, destacando que este es un framework de FrontEnd, y por ende no puede profundizar mucho en la implementación de lógica o acceso a base de datos, para lo cual se recomienda conectarlo con el frontend Node.js.
