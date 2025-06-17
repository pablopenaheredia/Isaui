import { useState } from 'react';
import type { Producto } from '../types/Productos';

const useFormProducto = () => {
  const [ventanaAbierta, setVentanaAbierta] = useState(false);
  const [productoEditar, setProductoEditar] = useState<Producto | undefined>();

  const abrirCrear = () => {
    setProductoEditar(undefined);
    setVentanaAbierta(true);
  };

  const abrirEditar = (producto: Producto) => {
    setProductoEditar(producto);
    setVentanaAbierta(true);
  };

  const cerrar = () => {
    setVentanaAbierta(false);
    setProductoEditar(undefined);
  };

  return {
    ventanaAbierta,
    productoEditar,
    abrirCrear,
    abrirEditar,
    cerrar,
  };
};

export default useFormProducto;