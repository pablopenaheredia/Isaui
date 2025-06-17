import React, { useEffect } from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
  Box,
} from '@mui/material';
import type { Producto, InfoFormulario, ErroresForm } from '../types/Productos';

interface PropsVentanaProducto {
  ventanaAbierta: boolean;
  editandoIndice: number | null;
  datosForm: InfoFormulario;
  setDatosForm: (datos: InfoFormulario) => void;
  errores: ErroresForm;
  setErrores: (errores: ErroresForm) => void;
  alCerrar: () => void;
  alGuardar: (producto: Producto) => void;
}

const VentanaProducto: React.FC<PropsVentanaProducto> = ({
  ventanaAbierta,
  editandoIndice,
  datosForm,
  setDatosForm,
  errores,
  setErrores,
  alCerrar,
  alGuardar,
}) => {
  useEffect(() => {
    if (editandoIndice === null) {
      setDatosForm({ nombre: '', precio: '', stock: '' });
    }
    setErrores({});
  }, [editandoIndice, setDatosForm, setErrores]);

  const revisarForm = (): boolean => {
    const erroresEncontrados: ErroresForm = {};

    if (!datosForm.nombre.trim()) {
      erroresEncontrados.nombre = 'El nombre es requerido';
    } else if (datosForm.nombre.trim().length < 2) {
      erroresEncontrados.nombre = 'El nombre debe tener al menos 2 caracteres';
    } else if (datosForm.nombre.trim().length > 30) {
      erroresEncontrados.nombre = 'El nombre no puede exceder los 30 caracteres';
    }

    if (!datosForm.precio.trim()) {
      erroresEncontrados.precio = 'El precio es requerido';
    } else {
      const precio = parseFloat(datosForm.precio);
      if (isNaN(precio) || precio <= 0) {
        erroresEncontrados.precio = 'El precio debe ser mayor a 0';
      }
    }

    if (!datosForm.stock.trim()) {
      erroresEncontrados.stock = 'El stock es requerido';
    } else {
      const stock = parseInt(datosForm.stock);
      if (isNaN(stock) || stock < 0) {
        erroresEncontrados.stock = 'El stock no puede ser negativo';
      }
    }

    setErrores(erroresEncontrados);
    return Object.keys(erroresEncontrados).length === 0;
  };

  const enviarForm = () => {
    if (revisarForm()) {
      const productoCompleto: Producto = {
        nombre: datosForm.nombre.trim(),
        precio: parseFloat(datosForm.precio),
        stock: parseInt(datosForm.stock),
      };
      alGuardar(productoCompleto);
    }
  };

  const cambiarCampo = (campo: keyof InfoFormulario, valor: string) => {
    setDatosForm({ ...datosForm, [campo]: valor });
    if (errores[campo]) {
      setErrores({ ...errores, [campo]: undefined });
    }
  };

  //regexp
  const soloPrecios = /^[0-9]*\.?[0-9]*$/;  
  const soloEnteros = /^[0-9]*$/;           

  // uso de regexp en input stock y precio
  const manejarNumeros = (valor: string, patron: RegExp, campo: keyof InfoFormulario) => {
    if (valor === '' || patron.test(valor)) {
      cambiarCampo(campo, valor);
    }
  };

  return (
    <Dialog 
      open={ventanaAbierta} 
      onClose={alCerrar} 
      maxWidth="sm" 
      fullWidth
      PaperProps={{ sx: { borderRadius: 3, padding: 2 } }}
    >
      <DialogTitle sx={{ textAlign: 'center', fontSize: '1.5rem', fontWeight: 'bold' }}>
        {editandoIndice !== null ? 'Editar Producto' : 'Nuevo Producto'}
      </DialogTitle>
      
      <DialogContent>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3, mt: 2 }}>
          <TextField
            label="Nombre del Producto"
            value={datosForm.nombre}
            onChange={(e) => cambiarCampo('nombre', e.target.value)}
            error={!!errores.nombre}
            helperText={errores.nombre || `${datosForm.nombre.length}/30 caracteres`}
            fullWidth
            inputProps={{ maxLength: 30 }}
          />
          
          <TextField
            label="Precio"
            type="text"
            value={datosForm.precio}
            onChange={(e) => manejarNumeros(e.target.value, soloPrecios, 'precio')}
            error={!!errores.precio}
            helperText={errores.precio}
            fullWidth
            placeholder="0.00"
            inputProps={{ 
              inputMode: 'decimal',
              pattern: '[0-9]*[.]?[0-9]*'
            }}
          />
          
          <TextField
            label="Stock"
            type="text"
            value={datosForm.stock}
            onChange={(e) => manejarNumeros(e.target.value, soloEnteros, 'stock')}
            error={!!errores.stock}
            helperText={errores.stock}
            fullWidth
            placeholder="0"
            inputProps={{ 
              inputMode: 'numeric',
              pattern: '[0-9]*'
            }}
          />
        </Box>
      </DialogContent>
      
      <DialogActions sx={{ padding: 3, gap: 2 }}>
        <Button onClick={alCerrar} variant="outlined" fullWidth>
          Cancelar
        </Button>
        <Button onClick={enviarForm} variant="contained" fullWidth>
          {editandoIndice !== null ? 'Actualizar' : 'Crear'}
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default VentanaProducto;
