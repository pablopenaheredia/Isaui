import { useState, useEffect } from 'react';
import type { Producto } from '../types/Productos';

const productosBase: Producto[] = [
  { id: '1', nombre: "Laptop HP", precio: 899.99, stock: 15 },
  { id: '2', nombre: "Mouse Logitech", precio: 25.5, stock: 50 },
  { id: '3', nombre: "Ram", precio: 120.0, stock: 0 },
];

const CLAVE_STORAGE = 'mis-productos';
const CLAVE_CONTADOR = 'contador-productos';

const useProductos = () => {
  const [productos, setProductos] = useState<Producto[]>(() => {
    const productosGuardados = localStorage.getItem(CLAVE_STORAGE);
    return productosGuardados ? JSON.parse(productosGuardados) //convierte un json en un array de objetos
    : productosBase;
  });

  const [contador, setContador] = useState(() => {
    const contadorGuardado = localStorage.getItem(CLAVE_CONTADOR);
    return contadorGuardado ? parseInt(contadorGuardado) : 4;
  });

  useEffect(() => {
    localStorage.setItem(CLAVE_STORAGE, JSON.stringify(productos)); //convierte string a .json
    localStorage.setItem(CLAVE_CONTADOR, contador.toString());
  }, [productos, contador]);

  
  const generateId = (): string => {
    const nuevoId = contador.toString();
    setContador(c => c + 1);
    return nuevoId;
  };

  const agregarProducto = (nuevoProducto: Omit<Producto, 'id'>) => {
    const productoConId: Producto = {...nuevoProducto, id: generateId()
    };
    setProductos(productos => [...productos, productoConId]);
  };

  const editarProducto = (id: string, productoEditado: Omit<Producto, 'id'>) => {
    setProductos(lista => 
      lista.map(producto => 
        producto.id === id ? { ...productoEditado, id } : producto
      )
    );
  };

  const borrarProducto = (id: string) => {
    setProductos(lista => lista.filter(producto => producto.id !== id));
  };//react no permite  borrar un elemento por como funciona el estado asi que se genera una nueva lista con .filter
  // sin el producto del id que se borra, solo detecta cambios con un array nuevo manteniendo todos excepto el del id que se borra

  return {productos, agregarProducto, editarProducto, borrarProducto};
};

export default useProductos;