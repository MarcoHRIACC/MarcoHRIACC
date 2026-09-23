# 💊 Sistema de Información para Gestión Farmacéutica

## 📌 Descripción

Proyecto académico orientado al diseño e implementación de un sistema de información para apoyar la gestión de productos, proveedores, compras, inventario y ventas de una empresa farmacéutica.

La propuesta busca reemplazar el control manual del inventario mediante hojas de cálculo por una solución basada en una base de datos relacional, permitiendo mejorar la organización, integridad y trazabilidad de la información.

## 🎯 Objetivo

Diseñar una solución de información que permita gestionar de manera estructurada:

- Productos y categorías.
- Proveedores.
- Compras y recepción de productos.
- Inventario y actualización de stock.
- Ventas.
- Usuarios y control de acceso.

## 🛠️ Tecnologías utilizadas

- SQL
- MySQL
- MySQL Workbench
- Visual Studio Code

## 🗄️ Modelo de datos

El sistema considera las siguientes entidades:

- CATEGORIA
- PRODUCTO
- PROVEEDOR
- PRODUCTO_PROVEEDOR
- USUARIO
- COMPRA
- DETALLE_COMPRA
- VENTA
- DETALLE_VENTA

## ⚙️ Funcionalidades

- Gestión de productos.
- Gestión de categorías.
- Gestión de proveedores.
- Registro de compras.
- Registro de ventas.
- Control de inventario.
- Actualización automática del stock.
- Relación entre productos y proveedores.
- Gestión de usuarios.
- Consultas SQL.

## 🔄 Automatización

Se implementan triggers para actualizar automáticamente el stock de los productos a partir de las operaciones de compra y venta.

## 🔐 Seguridad

El diseño considera mecanismos de control de acceso mediante perfiles y permisos de usuario, junto con principios de trazabilidad y protección de la información.

## 📷 Evidencias

Se incorporarán evidencias del modelo de datos, estructura de tablas, consultas SQL y resultados de las pruebas realizadas.

## 🎓 Contexto académico

Proyecto desarrollado como parte de la formación de **Ingeniería en Informática en IACC**.

## 👤 Autor

**Marco Hernández Riquelme**
