# 📘 Trabajo Práctico Integrador – Programación I  
## 🧠 Análisis de Eficiencia Algorítmica: Suma Iterativa vs Fórmula vs Recursiva

Este proyecto compara tres formas diferentes de resolver el mismo problema: **calcular la suma de los primeros _n_ números naturales**.  
El objetivo es **medir la eficiencia de cada algoritmo**, tanto en tiempo de ejecución como en simplicidad de implementación.

---
### 🎥 URL DE VIDEO EXPLICATIVO

```
📺 [Enlace al video explicativo!](https://sumar_cuando_termine_de_cargarse)

```
---

### 📂 Estructura del proyecto

```
trabajo-practico-integrador-programacion-i/
├── main.py                # Función principal que ejecuta las pruebas
├── algoritmos.py          # Contiene las funciones suma_iterativa, suma_formula, suma_recursiva
├── tiempo.py              # Función para medir tiempos de ejecución
├── analisis.py            # Compara los resultados y muestra el más eficiente
├──Archivos
    ├──PPT_Integrador_Programacion_I.pdf #PPT explicativa que se muestra en el video
    ├──TP_INTEGRADOR_PROGRAMACION_I.pdf #PDF con el trabajo practico teorico
```

---



### 📊 Algoritmos implementados

| Método            | Descripción                              | Complejidad |
|------------------|------------------------------------------|-------------|
| `suma_iterativa` | Usa un bucle `for` para sumar del 1 al n | O(n)        |
| `suma_formula`   | Aplica la fórmula `n(n+1)/2`              | O(1)        |
| `suma_recursiva` | Llama a sí misma hasta n = 0             | O(n) tiempo y espacio |

---

### ✅ Conclusiones

- Todos los algoritmos producen el mismo resultado.
- El método **más eficiente es el de fórmula**, porque su tiempo no depende del tamaño de entrada.
- La versión recursiva, aunque correcta, **es más lenta** y limitada por el máximo de llamadas recursivas de Python, propensa a generar errores de ejecución.

---

### 🧑‍💻 Autores:

Agustina Grille  - Alexis Borda
Universidad Tecnológica Nacional – Programación I  