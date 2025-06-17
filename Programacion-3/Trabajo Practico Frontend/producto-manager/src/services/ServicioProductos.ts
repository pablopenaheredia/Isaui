import type { Producto } from '../types/Productos';

export class ServicioProducto {  
  static mostrarPrecio = (precio: number): string => `$${precio.toFixed(2)}`;

  static estadoStock = (stock: number): 'error' | 'warning' | 'success' => 
    stock === 0 ? 'error' : stock <= 10 ? 'warning' : 'success';

  static textoStock = (stock: number): string => 
    stock === 0 ? 'Sin Stock' : stock <= 10 ? 'Stock Bajo' : 'En Stock';

  static validarProducto(producto: Producto): boolean {
    return (
      producto.nombre.trim().length >= 2 &&
      producto.precio > 0 &&
      producto.stock >= 0
    );
  }
}
