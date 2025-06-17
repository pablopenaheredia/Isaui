import { useState } from 'react';
import {
  Container,
  Typography,
  Button,
  Box,
  Alert,
} from '@mui/material';
import { Add as AddIcon } from '@mui/icons-material';
import ProductTable from './ProductTable';
import ProductDialog from './ProductDialog'; 
import ConfirmDeleteDialog from './ConfirmDeleteDialog';
import type { Product } from '../types/Products';
import useProducts from '../hooks/useProducts';
import useProductForm from '../hooks/useProductForm';

export default function AdmProductos() {
  const { products, addProduct, updateProduct, deleteProduct } = useProducts();
  const [deleteIndex, setDeleteIndex] = useState<number | null>(null);
  
  const {
    open,
    editingIndex,
    formData,
    errors,
    setFormData,
    setErrors,
    openDialog,
    closeDialog,
  } = useProductForm();

  const handleSaveProduct = (productData: Product) => {
    if (editingIndex !== null) {
      updateProduct(editingIndex, productData);
    } else {
      addProduct(productData);
    }
    closeDialog();
  };

  const handleDeleteClick = (index: number) => {
    setDeleteIndex(index);
  };

  const handleConfirmDelete = () => {
    if (deleteIndex !== null) {
      deleteProduct(deleteIndex);
      setDeleteIndex(null);
    }
  };

  const handleCloseDeleteDialog = () => {
    setDeleteIndex(null);
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
            onClick={() => openDialog()}
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
          {products.length === 0 ? (
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
            <ProductTable 
              products={products}
              onEdit={openDialog}
              onDelete={handleDeleteClick}
            />
          )}
        </Box>

        <ProductDialog
          open={open}
          editingIndex={editingIndex}
          formData={formData}
          setFormData={setFormData}
          errors={errors}
          setErrors={setErrors}
          onClose={closeDialog}
          onSave={handleSaveProduct}
        />

        <ConfirmDeleteDialog
          open={deleteIndex !== null}
          productName={deleteIndex !== null ? (products[deleteIndex]?.nombre || '') : ''}
          onClose={handleCloseDeleteDialog}
          onConfirm={handleConfirmDelete}
        />
      </Container>
    </Box>
  );
}