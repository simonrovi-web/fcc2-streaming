# FCC 2 · Fighting Championship Chile — Kit de transmisión OBS

Gráficos, transiciones y control en vivo para la transmisión de **FCC 2**
(17 de octubre de 2026 · Black House, General Jofré 254, Santiago Centro · 27 combates).

## Contenido

| Carpeta / archivo | Qué es |
|---|---|
| `CONTROL_EN_VIVO.html` | Control en tiempo real: reloj, nombres, cartelera, resultado, lower third, escenas. Se conecta a OBS por WebSocket e instala los gráficos solo. |
| `PANEL_DE_CONTROL.html` | Catálogo de todos los gráficos y transiciones con vista previa y botones para copiar rutas. |
| `Paneles/` | Gráficos 1920×1080 (fuente *Navegador* de OBS): Inicio, Pausa, VS, Ganador, Auspiciador, Final y overlays transparentes (Marcador, Replay, Lower third). Cada uno con su `.png`. |
| `Transiciones/` | Stingers `.webm` con transparencia y sonido, 4 s. Punto de transición: **2000 ms**. |
| `fuente/` | Archivos fuente para regenerar los gráficos (`python3 build.py`). |

## Uso rápido

1. Descarga el repo (**Code → Download ZIP**) y descomprímelo en una carpeta fija.
2. OBS → **Herramientas → Ajustes del servidor WebSocket** → Habilitar → copia la contraseña.
3. Abre `CONTROL_EN_VIVO.html` en Chrome, pega la contraseña y pulsa **CONECTAR**.
4. Pulsa **INSTALAR GRÁFICOS EN OBS** y luego **PROBAR**.

Más detalles en `Paneles/LEEME.txt`.

## Controlar desde otro PC

1. En el PC de OBS: abre `CONTROL_EN_VIVO.html` y pulsa **INSTALAR GRÁFICOS EN OBS** (una sola vez).
2. En OBS → Herramientas → Ajustes del servidor WebSocket → **Mostrar información de conexión**: anota la **IP** y la contraseña.
3. En el otro PC (misma red Wi‑Fi/cable): abre `CONTROL_EN_VIVO.html`, escribe esa IP en lugar de `localhost`, la contraseña, y **CONECTAR**.
4. Si no conecta: en el PC de OBS permite OBS en el **Firewall de Windows** (redes privadas) o el puerto **4455**.
