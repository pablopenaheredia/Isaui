export interface Product {
  nombre: string;
  precio: number;
  stock: number;
}
export interface ProductFormData {
  nombre: string;
  precio: string;
  stock: string;
}

export interface FormErrors {
  nombre?: string;
  precio?: string;
  stock?: string;
}