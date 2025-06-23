import { useState } from 'react';
import { Container, Typography, Button, Box, Alert } from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';
import TablaProductos from './TablaProductos';
import VentanaProducto from './VentanaProducto'; 
import VentanaConfirmar from './VentanaConfirmar';
import type { Producto } from '../types/Productos';
import useProductos from '../hooks/useProductos';
import useFormProducto from '../hooks/useFormProducto';

// ✨ SIMPLIFICADO: Estilos como constantes
const containerWidth = { width: '100%', maxWidth: '1200px' };

const gradientBackground = {
  minHeight: '100vh',
  width: '100vw',
  background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  py: 4,
  position: 'fixed' as const,
  top: 0,
  left: 0
};

export default function AdministradorProductos() {
  const { productos, agregarProducto, editarProducto, borrarProducto } = useProductos();
  const { ventanaAbierta, productoEditar, abrirCrear, abrirEditar, cerrar } = useFormProducto();
  const [productoABorrar, setProductoABorrar] = useState<Producto | null>(null);

  const guardarProducto = (nuevoProducto: Omit<Producto, 'id'>) => {
    if (productoEditar) {
      editarProducto(productoEditar.id, nuevoProducto);
    } else {
      agregarProducto(nuevoProducto);
    }
    cerrar();
  };
  const clickBorrar = (id: string) => {
    const producto = productos.find(p => p.id === id);
    if (producto) {
      setProductoABorrar(producto);
    }
  };

  const confirmarBorrar = () => {
    if (productoABorrar) {
      borrarProducto(productoABorrar.id);
      setProductoABorrar(null);
    }
  };
  
  const cancelarBorrar = () => setProductoABorrar(null);

  return (
    <Box sx={gradientBackground}>
      <Container maxWidth="lg" sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', width: '100%' }}>
        <Box sx={{ mb: 4, display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: 2, ...containerWidth }}>
          <Typography variant="h4" component="h1" sx={{ mb: 0, color: 'white', fontWeight: 'bold', textShadow: '2px 2px 4px rgba(0,0,0,0.3)' }}>
            Administrador de Productos
          </Typography>
          <Button
            variant="contained"
            startIcon={<AddIcon />}
            onClick={abrirCrear}
            sx={{ flexShrink: 0, backgroundColor: 'white', color: 'primary.main', '&:hover': { backgroundColor: 'rgba(255,255,255,0.9)' } }}
          >
            Nuevo Producto
          </Button>
        </Box>

        <Box sx={containerWidth}>
          {productos.length === 0 ? (
            <Alert severity="info" sx={{ backgroundColor: 'rgba(255,255,255,0.9)', fontSize: '1.1rem', borderRadius: 2, boxShadow: 2 }}>
              No tienes productos en tu inventario.
            </Alert>
          ) : (
            <TablaProductos productos={productos} alEditar={abrirEditar} alBorrar={clickBorrar} />
          )}
        </Box>

        <VentanaProducto
          ventanaAbierta={ventanaAbierta}
          productoEditar={productoEditar}
          alCerrar={cerrar}
          alGuardar={guardarProducto}
        />

        <VentanaConfirmar
          ventanaAbierta={productoABorrar !== null}
          nombreProducto={productoABorrar?.nombre || ''}
          alCerrar={cancelarBorrar}
          alConfirmar={confirmarBorrar}
        />
      </Container>
    </Box>
  );
}