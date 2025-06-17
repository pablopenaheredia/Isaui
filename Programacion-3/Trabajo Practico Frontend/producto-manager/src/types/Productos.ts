export interface Producto {
  nombre: string;
  precio: number;
  stock: number;
}

export interface InfoFormulario {
  nombre: string;
  precio: string;
  stock: string;
}

export interface ErroresForm {
  nombre?: string;
  precio?: string;
  stock?: string;
}