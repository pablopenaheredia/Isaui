import type { Producto } from '../types/Productos';

export const mostrarPrecio = (precio: number): string => `$${precio.toFixed(2)}`;

export const estadoStock = (stock: number): 'error' | 'warning' | 'success' => 
  stock === 0 ? 'error' : stock <= 10 ? 'warning' : 'success';
//error, warning y success viene de mui

export const textoStock = (stock: number): string => 
  stock === 0 ? 'Sin Stock' : stock <= 10 ? 'Stock Bajo' : 'En Stock';

export const validarProducto = (producto: Producto): boolean => (
  //devuelve un booleano para mostrar o no los errores en el form.
  producto.nombre.trim().length >= 2 && //trim elimina espacios vacios en inicio y fin
  producto.precio > 0 &&
  producto.stock >= 0
);