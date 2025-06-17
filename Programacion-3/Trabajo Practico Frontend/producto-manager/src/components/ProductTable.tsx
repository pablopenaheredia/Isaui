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
import type { Product } from '../types/Products';
import { ProductService } from '../services/ProductService';

interface ProductTableProps {
  products: Product[];
  onEdit: (product: Product, index: number) => void;
  onDelete: (index: number) => void;
}

const ProductTable: React.FC<ProductTableProps> = ({ products, onEdit, onDelete }) => {
  const getStockChip = (stock: number) => (
    <Chip 
      label={ProductService.getStockLabel(stock)} 
      color={ProductService.getStockStatus(stock)} 
      size="small" 
    />
  );

  const headerCellStyle = { color: "white", fontWeight: "bold" };

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
            <TableCell sx={headerCellStyle}>Nombre</TableCell>
            <TableCell sx={headerCellStyle} align="right">Precio</TableCell>
            <TableCell sx={headerCellStyle} align="center">Stock</TableCell>
            <TableCell sx={headerCellStyle} align="center">Estado</TableCell>
            <TableCell sx={headerCellStyle} align="center">Acciones</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {products.map((product, index) => (
            <TableRow key={index} hover>
              <TableCell>
                <Typography variant="body1" fontWeight="medium">
                  {product.nombre}
                </Typography>
              </TableCell>
              <TableCell align="right">
                <Typography variant="body1" color="primary" fontWeight="bold">
                  {ProductService.formatPrice(product.precio)}
                </Typography>
              </TableCell>
              <TableCell align="center">{product.stock}</TableCell>
              <TableCell align="center">{getStockChip(product.stock)}</TableCell>
              <TableCell align="center">
                <IconButton color="primary" onClick={() => onEdit(product, index)} size="small">
                  <EditIcon />
                </IconButton>
                <IconButton color="error" onClick={() => onDelete(index)} size="small">
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

export default ProductTable;