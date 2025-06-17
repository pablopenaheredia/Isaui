import { useState, useEffect } from 'react';
import type { Producto } from '../types/Productos';

const productosBase: Producto[] = [
  { nombre: "Laptop HP", precio: 899.99, stock: 15 },
  { nombre: "Mouse Logitech", precio: 25.5, stock: 50 },
  { nombre: "Ram", precio: 120.0, stock: 0 },
];

const CLAVE_STORAGE = 'mis-productos';

const useProductos = () => {
  const [productos, setProductos] = useState<Producto[]>(() => {
    try {
      const productosGuardados = localStorage.getItem(CLAVE_STORAGE);
      if (productosGuardados) {
        return JSON.parse(productosGuardados);
      }
    } catch (error) {
      console.error('Error cargando productos:', error);
    }
    return productosBase;
  });

  useEffect(() => {
    try {
      localStorage.setItem(CLAVE_STORAGE, JSON.stringify(productos));
    } catch (error) {
      console.error('Error guardando productos:', error);
    }
  }, [productos]);

  const agregarProducto = (nuevoProducto: Producto) => {
    setProductos(prev => [...prev, nuevoProducto]);
  };

  const editarProducto = (indice: number, productoEditado: Producto) => {
    setProductos(prev => {
      const nuevaLista = [];
      for (let i = 0; i < prev.length; i++) {
        if (i === indice) {
          nuevaLista.push(productoEditado);
        } else {
          nuevaLista.push(prev[i]);
        }
      }
      return nuevaLista;
    });
  };

  const borrarProducto = (indice: number) => {
    setProductos(prev => {
      const listaFiltrada = [];
      for (let i = 0; i < prev.length; i++) {
        if (i !== indice) {
          listaFiltrada.push(prev[i]);
        }
      }
      return listaFiltrada;
    });
  };

  return {
    productos,
    agregarProducto,
    editarProducto,
    borrarProducto,
  };
};

export default useProductos;