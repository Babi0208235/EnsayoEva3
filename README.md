# EnsayoEva3
Ensayo para evaluacion de fundamentos de programacion 
# ✈️ Registro de Equipaje - VuelosChile

Este es un script interactivo en Python desarrollado para automatizar y validar el proceso de registro y clasificación de equipaje para los vuelos de **VuelosChile**. El programa asegura que los datos ingresados (cantidad de equipaje, códigos de ticket y pesos) cumplan con los estándares operativos y de seguridad antes de generar el manifiesto de carga final.

---

## 🚀 Características Principales

* **Validación Robusta de Entradas:** Controla errores de ingreso (como textos en lugar de números) utilizando bloques `try-except`.
* **Control de Calidad en Tickets:** Verifica que los códigos de ticket tengan una longitud mínima de 5 caracteres y no contengan espacios intermedios.
* **Clasificación Automática de Equipaje:** Determina el destino del equipaje según su peso:
    * **Equipaje de Cabina:** Pesos menores o iguales a 10 kg.
    * **Equipaje de Bodega:** Pesos superiores a 10 kg.
* **Resumen Automático:** Genera un manifiesto de carga consolidado al finalizar todo el proceso de registro.

---

## 🛠️ Requisitos

* **Python 3.x** instalado en tu sistema.

---

## 💻 Cómo Ejecutar el Proyecto

1. **Clona este repositorio** en tu máquina local:
   ```bash
   git clone [https://github.com/tu-usuario/registro-equipaje-vueloschile.git](https://github.com/tu-usuario/registro-equipaje-vueloschile.git)
