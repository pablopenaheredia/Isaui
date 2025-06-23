import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, IconButton, Typography, Chip } from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon } from '@mui/icons-material';
import type { Producto } from '../types/Productos';
import { mostrarPrecio, estadoStock, textoStock } from '../services/ServicioProductos'; 

interface PropsTabla {
  productos: Producto[];
  alEditar: (producto: Producto) => void;
  alBorrar: (id: string) => void;
}

const estiloEncabezado = { color: "white", fontWeight: "bold" };

const TablaProductos: React.FC<PropsTabla> = ({ productos, alEditar, alBorrar }) => {
  const mostrarChipStock = (stock: number) => (
    <Chip label={textoStock(stock)} color={estadoStock(stock)} size="small" />
  );

  return (
    <TableContainer component={Paper} elevation={2} sx={{ backgroundColor: '#f5f5f5', '& .MuiTable-root': { backgroundColor: 'white' } }}>
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
          {productos.map((producto) => (
            <TableRow key={producto.id} hover>
              <TableCell>
                <Typography variant="body1" fontWeight="medium">{producto.nombre}</Typography>
              </TableCell>
              <TableCell align="right">
                <Typography variant="body1" color="primary" fontWeight="bold">
                  {mostrarPrecio(producto.precio)}
                </Typography>
              </TableCell>
              <TableCell align="center">{producto.stock}</TableCell>
              <TableCell align="center">{mostrarChipStock(producto.stock)}</TableCell>
              <TableCell align="center">
                <IconButton color="primary" onClick={() => alEditar(producto)} size="small">
                  <EditIcon />
                </IconButton>
                <IconButton color="error" onClick={() => alBorrar(producto.id)} size="small">
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