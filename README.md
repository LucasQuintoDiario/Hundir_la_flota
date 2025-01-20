# Hundir la Flota

¡Bienvenido a **Hundir la Flota**, una versión digital del clásico juego de estrategia naval!
En este proyecto, podrás enfrentarte contra el ordenador (Edward Thatch) en una batalla para hundir todos los barcos del oponente antes de que hundan los tuyos.

---

## Características del Juego

- **Tablero interactivo**: Visualiza tus barcos, los disparos acertados y fallidos.
- **Barcos personalizados**: Juega con 6 barcos diferentes:
  - 3 barcos de eslora 2.
  - 2 barcos de eslora 3.
  - 1 barco de eslora 4.
- **Turnos alternados**: Ataca introduciendo coordenadas mientras Edward responde con disparos aleatorios.
- **Visualización clara**: Observa el progreso en ambos tableros y sigue las pistas para mejorar tu estrategia.

---

## Tecnologías utilizadas

- **Python 3.9+**: Lenguaje de programación principal.
- **Módulos personalizados**: Implementados en el archivo `utils.py` para gestionar las lógicas del juego.
- **Módulo time**: Para mejorar la experiencia con pausas controladas.

---

## Requisitos previos

1. Tener instalado Python 3.9 o superior.
2. Asegurarte de que el archivo `utils.py` se encuentra en el mismo directorio que el archivo principal del juego.

---

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/LucasQuintoDiario/Hundir_la_flota.git
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd hundir-la-flota
   ```
3. Ejecuta el archivo principal del juego:
   ```bash
   python main.py
   ```

---

## Cómo jugar

1. **Inicio del juego**:
   - El programa creará dos tableros: uno para ti y otro para Edward.
   - Tus barcos serán colocados automáticamente.
2. **Turnos**:
   - Introduce las coordenadas para atacar el tablero enemigo.
   - El resultado del disparo aparecerá en el tablero del oponente.
   - El turno de Edward se realiza automáticamente.
3. **Final del juego**:
   - Gana el primero que logre hundir todos los barcos del oponente.

---

## Ejemplo de uso

### Tu tablero:
```
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
O O ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
O O O ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
O O O O ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
```

### Tablero del oponente (inicialmente oculto):
```
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
```

---

¡Buena suerte hundiendo los barcos de Edward Thatch!

