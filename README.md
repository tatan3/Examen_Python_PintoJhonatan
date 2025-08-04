# Examen_Python_PintoJhonatan
# 🍔 Sistema de Gestión de Inventario para la Cafetería Campuslands

## 📘 Descripción General

Este proyecto tiene como objetivo desarrollar un sistema de gestión de inventario para la cafetería de **Campuslands**, facilitando a los Chefs el control eficiente de ingredientes, la preparación de hamburguesas, y el mantenimiento de una operación de cocina ordenada, sostenible y rentable.

Actualmente, la cafetería enfrenta dificultades críticas derivadas de una gestión ineficiente de ingredientes, lo cual puede ocasionar:

- Faltantes inesperados en la cocina.
- Pérdida de productos por vencimiento o mala planificación.
- Inconsistencia en los pedidos y experiencia del cliente.
- Pérdida de ingresos y aumento en costos operativos.

Con este sistema, se busca automatizar y optimizar todos los procesos relacionados al control de stock, registros de hamburguesas, especialidades de chefs, y reportes analíticos sobre el inventario.

---

## 🎯 Objetivos del Sistema

- Proporcionar una plataforma funcional para gestionar ingredientes, chefs, categorías y hamburguesas.
- Controlar el inventario en tiempo real.
- Facilitar la toma de decisiones con reportes automáticos.
- Reducir el desperdicio y los costos.
- Mejorar la experiencia del cliente a través de una operación de cocina más organizada.

---

## 🗃️ Estructura de Datos

El sistema trabaja con archivos JSON para almacenar la información. A continuación se presentan los modelos propuestos:

### 🧂 Ingredientes (`ingredientes.json`)
```json
[
  {
    "nombre": "Pan",
    "descripcion": "Pan de hamburguesa clásico",
    "precio": 2.5,
    "stock": 500
  },
  ...
]
