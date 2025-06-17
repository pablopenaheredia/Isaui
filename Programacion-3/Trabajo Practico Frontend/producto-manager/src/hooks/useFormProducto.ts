import { useState } from 'react';
import type { Producto, InfoFormulario, ErroresForm } from '../types/Productos';

const useFormProducto = () => {
  const [ventanaAbierta, setVentanaAbierta] = useState(false);
  const [editandoIndice, setEditandoIndice] = useState<number | null>(null);
  const [datosForm, setDatosForm] = useState<InfoFormulario>({
    nombre: "",
    precio: "",
    stock: "",
  });
  const [errores, setErrores] = useState<ErroresForm>({});

  const abrirVentana = (producto?: Producto, indice?: number) => {
    if (producto && indice !== undefined) {
      setEditandoIndice(indice);
      setDatosForm({
        nombre: producto.nombre,
        precio: producto.precio.toString(),
        stock: producto.stock.toString(),
      });
    } else {
      setEditandoIndice(null);
      setDatosForm({ nombre: "", precio: "", stock: "" });
    }
    setErrores({});
    setVentanaAbierta(true);
  };

  const cerrarVentana = () => {
    setVentanaAbierta(false);
    setEditandoIndice(null);
    setDatosForm({ nombre: "", precio: "", stock: "" });
    setErrores({});
  };

  return {
    ventanaAbierta,
    editandoIndice,
    datosForm,
    errores,
    setDatosForm,
    setErrores,
    abrirVentana,
    cerrarVentana,
  };
};

export default useFormProducto;