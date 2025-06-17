import type { Product } from '../types/Products';

export class ProductService {
  static formatPrice = (price: number): string => `$${price.toFixed(2)}`;

  static getStockStatus = (stock: number): 'error' | 'warning' | 'success' => 
    stock === 0 ? 'error' : stock <= 10 ? 'warning' : 'success';

  static getStockLabel = (stock: number): string => 
    stock === 0 ? 'Sin Stock' : stock <= 10 ? 'Stock Bajo' : 'En Stock';

  static validateProductData(data: Product): boolean {
    return (
      data.nombre.trim().length >= 2 &&
      data.precio > 0 &&
      data.stock >= 0
    );
  }
}