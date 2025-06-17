import { useState } from 'react';
import {
  Container,
  Typography,
  Button,
  Box,
  Alert,
} from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';
import TablaProductos from './TablaProductos';
import VentanaProducto from './VentanaProducto'; 
import VentanaConfirmar from './VentanaConfirmar';
import type { Producto } from '../types/Productos';
import useProductos from '../hooks/useProductos';
import useFormProducto from '../hooks/useFormProducto';

export default function AdministradorProductos() {
  const { productos, agregarProducto, editarProducto, borrarProducto } = useProductos();
  const [indiceBorrar, setIndiceBorrar] = useState<number | null>(null);
  
  const {
    ventanaAbierta,
    editandoIndice,
    datosForm,
    errores,
    setDatosForm,
    setErrores,
    abrirVentana,
    cerrarVentana,
  } = useFormProducto();

  const guardarProducto = (nuevoProducto: Producto) => {
    if (editandoIndice !== null) {
      editarProducto(editandoIndice, nuevoProducto);
    } else {
      agregarProducto(nuevoProducto);
    }
    cerrarVentana();
  };

  const clickBorrar = (indice: number) => {
    setIndiceBorrar(indice);
  };

  const confirmarBorrar = () => {
    if (indiceBorrar !== null) {
      borrarProducto(indiceBorrar);
      setIndiceBorrar(null);
    }
  };

  const cancelarBorrar = () => {
    setIndiceBorrar(null);
  };

  const obtenerNombre = (): string => {
    return indiceBorrar !== null 
      ? (productos[indiceBorrar]?.nombre || '') 
      : '';
  };

  return (
    <Box 
      sx={{
        minHeight: '100vh',
        width: '100vw',
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        py: 4,
        position: 'fixed',
        top: 0,
        left: 0
      }}
    >
      <Container 
        maxWidth="lg" 
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          width: '100%'
        }}
      >
        <Box 
          sx={{ 
            mb: 4, 
            display: "flex", 
            justifyContent: "space-between", 
            alignItems: "flex-start",
            gap: 2,
            width: '100%',
            maxWidth: '1200px'
          }}
        >
          <Typography 
            variant="h4" 
            component="h1" 
            sx={{ 
              mb: 0,
              color: 'white',
              fontWeight: 'bold',
              textShadow: '2px 2px 4px rgba(0,0,0,0.3)'
            }}
          >
            Administrador de Productos
          </Typography>
          <Button
            variant="contained"
            startIcon={<AddIcon />}
            onClick={() => abrirVentana()}
            sx={{ 
              flexShrink: 0,
              backgroundColor: 'white',
              color: 'primary.main',
              '&:hover': { backgroundColor: 'rgba(255,255,255,0.9)' }
            }}
          >
            Nuevo Producto
          </Button>
        </Box>

        <Box sx={{ width: '100%', maxWidth: '1200px' }}>
          {productos.length === 0 ? (
            <Alert 
              severity="info" 
              sx={{ 
                backgroundColor: 'rgba(255,255,255,0.9)',
                fontSize: '1.1rem',
                borderRadius: 2,
                boxShadow: 2
              }}
            >
              No tienes productos en tu inventario.
            </Alert>
          ) : (
            <TablaProductos 
              productos={productos}
              alEditar={abrirVentana}
              alBorrar={clickBorrar}
            />
          )}
        </Box>

        <VentanaProducto
          ventanaAbierta={ventanaAbierta}
          editandoIndice={editandoIndice}
          datosForm={datosForm}
          setDatosForm={setDatosForm}
          errores={errores}
          setErrores={setErrores}
          alCerrar={cerrarVentana}
          alGuardar={guardarProducto}
        />

        <VentanaConfirmar
          ventanaAbierta={indiceBorrar !== null}
          nombreProducto={obtenerNombre()}
          alCerrar={cancelarBorrar}
          alConfirmar={confirmarBorrar}
        />
      </Container>
    </Box>
  );
}