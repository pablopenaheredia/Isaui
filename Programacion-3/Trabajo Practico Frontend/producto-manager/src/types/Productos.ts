export interface Producto {
  id: string;
  nombre: string;
  precio: number;
  stock: number;
}

export interface InfoFormulario {
  nombre: string;
  precio: string;//tanto precio como son strings ya que se manejan como texto en el formulario
  stock: string;
}

export interface ErroresForm {
  nombre?: string;
  precio?: string;
  stock?: string;
}