import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  IconButton,
  Typography,
  Chip,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon } from '@mui/icons-material';
import type { Producto } from '../types/Productos';
import { ServicioProducto } from '../services/ServicioProductos';  

interface PropsTabla {
  productos: Producto[];
  alEditar: (producto: Producto, indice: number) => void;
  alBorrar: (indice: number) => void;
}

const TablaProductos: React.FC<PropsTabla> = ({ productos, alEditar, alBorrar }) => {
  const mostrarChipStock = (stock: number) => (
    <Chip 
      label={ServicioProducto.textoStock(stock)}   
      color={ServicioProducto.estadoStock(stock)}   
      size="small" 
    />
  );

  const estiloEncabezado = { color: "white", fontWeight: "bold" };

  return (
    <TableContainer 
      component={Paper} 
      elevation={2}
      sx={{ 
        backgroundColor: '#f5f5f5',
        '& .MuiTable-root': { backgroundColor: 'white' }
      }}
    >
      <Table>
        <TableHead>
          <TableRow sx={{ backgroundColor: "primary.main" }}>
            <TableCell sx={estiloEncabezado}>Nombre</TableCell>
            <TableCell sx={estiloEncabezado} align="right">Precio</TableCell>
            <TableCell sx={estiloEncabezado} align="center">Stock</TableCell>
            <TableCell sx={estiloEncabezado} align="center">Estado</TableCell>
            <TableCell sx={estiloEncabezado} align="center">Acciones</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {productos.map((producto, indice) => (
            <TableRow key={indice} hover>
              <TableCell>
                <Typography variant="body1" fontWeight="medium">
                  {producto.nombre}
                </Typography>
              </TableCell>
              <TableCell align="right">
                <Typography variant="body1" color="primary" fontWeight="bold">
                  {ServicioProducto.mostrarPrecio(producto.precio)}
                </Typography>
              </TableCell>
              <TableCell align="center">{producto.stock}</TableCell>
              <TableCell align="center">{mostrarChipStock(producto.stock)}</TableCell>
              <TableCell align="center">
                <IconButton 
                  color="primary" 
                  onClick={() => alEditar(producto, indice)} 
                  size="small"
                >
                  <EditIcon />
                </IconButton>
                <IconButton 
                  color="error" 
                  onClick={() => alBorrar(indice)} 
                  size="small"
                >
                  <DeleteIcon />
                </IconButton>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default TablaProductos;