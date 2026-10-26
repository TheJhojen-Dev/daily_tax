# Daily Tax

Módulo para **Odoo 18** que muestra en la barra superior de Odoo la tasa oficial del día del **dólar** y el **euro** en bolívares (BCV).

## De dónde vienen las tasas

El módulo consulta la API de [dolarapi.com](https://ve.dolarapi.com) (`/v1/dolares/oficial` y `/v1/euros/oficial`), que devuelve la tasa oficial del BCV.

Se usa la API en lugar de hacer *scraping* (leer el HTML de la página del BCV) por tres razones:

- **Es más estable**: no depende del diseño de la web, así que no se rompe cada vez que cambian la página.
- **No hay riesgo de baneo**: consultar la API es justamente lo que el sitio ofrece para hacer; si se leen sus páginas como si fueras un robot, pueden bloquear la IP.
- **Los datos llegan listos**: la API ya devuelve la tasa en número, sin tener que sacarla de un texto.

La consulta se hace desde el servidor de Odoo, no desde el navegador.

## Dónde se ven las tasas

En la **barra superior**, en la esquina superior derecha, junto a los demás íconos de Odoo (notificaciones, actividad, etc.).

- El ícono muestra la tasa del dólar en bolívares.
- Al hacer clic se abre un panel con el **dólar** y el **euro**, y un botón de recarga para actualizar las tasas en el momento.

Como el ícono se registra en la barra superior de Odoo, aparece en **todas las pantallas**, sin importar en qué menú o formulario estés.

## Cómo instalarlo

1. Reiniciar el contenedor de Odoo para que reconozca el módulo:

   ```bash
   docker compose restart web
   ```

2. En Odoo, entrar a **Apps**, hacer clic en el menú de tres puntos (⋮) y elegir **Update Apps List**.
3. Buscar **"Daily Tax"** en el buscador y hacer clic en **Install**.
4. Recargar el navegador (Ctrl + F5) para que carguen los estilos del ícono.

## Requisitos

- Odoo 18
- El servidor debe tener conexión a internet para poder consultar la API.

## Nota

El módulo es independiente: no necesita ningún otro addon instalado
