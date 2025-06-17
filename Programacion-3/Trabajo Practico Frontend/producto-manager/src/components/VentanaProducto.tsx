import React, { useState, useEffect } from 'react';
import { Dialog, DialogTitle, DialogContent, DialogActions, TextField, Button, Box } from '@mui/material';
import type { Producto, ErroresForm } from '../types/Productos';

interface PropsVentana {
  ventanaAbierta: boolean;
  productoEditar?: Producto; //por defecto undefined
  alCerrar: () => void;
  alGuardar: (producto: Omit<Producto, 'id'>) => void;
}

const VentanaProducto: React.FC<PropsVentana> = ({
  ventanaAbierta,
  productoEditar,
  alCerrar,
  alGuardar,
}) => {
  const [nombre, setNombre] = useState('');
  const [precio, setPrecio] = useState('');
  const [stock, setStock] = useState('');
  const [errores, setErrores] = useState<ErroresForm>({});

  const soloPrecios = /^[0-9]*\.?[0-9]*$/;
  const soloEnteros = /^[0-9]*$/;

  useEffect(() => {
    if (ventanaAbierta) {
      if (productoEditar) {
        setNombre(productoEditar.nombre);
        setPrecio(productoEditar.precio.toString());
        setStock(productoEditar.stock.toString());
      } else {
        setNombre('');
        setPrecio('');
        setStock('');
      }
      setErrores({});
    }
  }, [ventanaAbierta, productoEditar]);

  const revisarForm = (): boolean => {
    const erroresEncontrados: ErroresForm = {};

    if (!nombre.trim()) {
      erroresEncontrados.nombre = 'El nombre es requerido';
    } else if (nombre.trim().length < 2) {
      erroresEncontrados.nombre = 'El nombre debe tener al menos 2 caracteres';
    } else if (nombre.trim().length > 30) {
      erroresEncontrados.nombre = 'El nombre no puede exceder los 30 caracteres';
    }

    if (!precio.trim()) {
      erroresEncontrados.precio = 'El precio es requerido';
    } else {
      const precioNum = parseFloat(precio);
      if (isNaN(precioNum) || precioNum <= 0) {
        erroresEncontrados.precio = 'El precio debe ser mayor a 0';
      }
    }

    if (!stock.trim()) {
      erroresEncontrados.stock = 'El stock es requerido';
    } else {
      const stockNum = parseInt(stock);
      if (isNaN(stockNum) || stockNum < 0) {
        erroresEncontrados.stock = 'El stock no puede ser negativo';
      }
    }

    setErrores(erroresEncontrados);
    return Object.keys(erroresEncontrados).length === 0;
  };

  const enviarForm = () => {
    if (revisarForm()) {
      const productoCompleto = {
        nombre: nombre.trim(),
        precio: parseFloat(precio),
        stock: parseInt(stock),
      };
      alGuardar(productoCompleto);
      alCerrar();
    }
  };

  const cambiarInput = (input: string, valor: string) => {
    if (input === 'nombre') {
      setNombre(valor);
    } else if (input === 'precio') {
      setPrecio(valor);
    } else if (input === 'stock') {
      setStock(valor);
    }

    if (errores[input as keyof ErroresForm]) {
      setErrores({ ...errores, [input]: undefined });
    }
  };

  const manejarNumeros = (valor: string, patron: RegExp, input: string) => {
  if (valor === '' || valor.match(patron)) {
    cambiarInput(input, valor);
  }
};

  const siEdito = productoEditar !== undefined;

  return (
    <Dialog 
      open={ventanaAbierta} 
      onClose={alCerrar} 
      maxWidth="sm" 
      fullWidth
      PaperProps={{ sx: { borderRadius: 3, padding: 2 } }}
    >
      <DialogTitle sx={{ textAlign: 'center', fontSize: '1.5rem', fontWeight: 'bold' }}>
        {siEdito ? 'Editar Producto' : 'Nuevo Producto'}
      </DialogTitle>
      
      <DialogContent>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3, mt: 2 }}>
          <TextField
            label="Nombre del Producto"
            value={nombre}
            onChange={(e) => cambiarInput('nombre', e.target.value)}
            error={!!errores.nombre}
            helperText={errores.nombre || `${nombre.length}/30 caracteres`}
            fullWidth
            slotProps={{
              htmlInput: { maxLength: 30 }
            }}
          />
          
          <TextField
            label="Precio"
            type="text"
            value={precio}
            onChange={(e) => manejarNumeros(e.target.value, soloPrecios, 'precio')}
            error={!!errores.precio} // doble ! lo convierte a booleano
            helperText={errores.precio}
            fullWidth
            placeholder="0.00"
            slotProps={{
              htmlInput: { 
                inputMode: 'decimal',
                pattern: '[0-9]*[.]?[0-9]*'
              }
            }}
          />
          
          <TextField
            label="Stock"
            type="text"
            value={stock}
            onChange={(e) => manejarNumeros(e.target.value, soloEnteros, 'stock')}
            error={!!errores.stock}
            helperText={errores.stock}
            fullWidth
            placeholder="0"
            slotProps={{
              htmlInput: { 
                inputMode: 'decimal',
                pattern: '[0-9]*[.]?[0-9]*'
              }
            }}
          />
        </Box>
      </DialogContent>
      
      <DialogActions sx={{ padding: 3, gap: 2 }}>
        <Button onClick={alCerrar} variant="outlined" fullWidth>
          Cancelar
        </Button>
        <Button onClick={enviarForm} variant="contained" fullWidth>
          {siEdito ? 'Actualizar' : 'Crear'}
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default VentanaProducto;