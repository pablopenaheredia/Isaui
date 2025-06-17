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
import type { Product, ProductFormData, FormErrors } from '../types/Products';

interface ProductDialogProps {
  open: boolean;
  editingIndex: number | null;
  formData: ProductFormData;
  setFormData: (data: ProductFormData) => void;
  errors: FormErrors;
  setErrors: (errors: FormErrors) => void;
  onClose: () => void;
  onSave: (productData: Product) => void;
}

const ProductDialog: React.FC<ProductDialogProps> = ({
  open,
  editingIndex,
  formData,
  setFormData,
  errors,
  setErrors,
  onClose,
  onSave,
}) => {
  useEffect(() => {
    if (editingIndex === null) {
      setFormData({ nombre: '', precio: '', stock: '' });
    }
    setErrors({});
  }, [editingIndex, setFormData, setErrors]);

  const validateForm = (): boolean => {
    const newErrors: FormErrors = {};

    if (!formData.nombre.trim()) {
      newErrors.nombre = 'El nombre es requerido';
    } else if (formData.nombre.trim().length < 2) {
      newErrors.nombre = 'El nombre debe tener al menos 2 caracteres';
    } else if (formData.nombre.trim().length > 30) {
      newErrors.nombre = 'El nombre no puede exceder los 30 caracteres';
    }

    if (!formData.precio.trim()) {
      newErrors.precio = 'El precio es requerido';
    } else {
      const precio = parseFloat(formData.precio);
      if (isNaN(precio) || precio <= 0) {
        newErrors.precio = 'El precio debe ser mayor a 0';
      }
    }

    if (!formData.stock.trim()) {
      newErrors.stock = 'El stock es requerido';
    } else {
      const stock = parseInt(formData.stock);
      if (isNaN(stock) || stock < 0) {
        newErrors.stock = 'El stock no puede ser negativo';
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = () => {
    if (validateForm()) {
      const productData: Product = {
        nombre: formData.nombre.trim(),
        precio: parseFloat(formData.precio),
        stock: parseInt(formData.stock),
      };
      onSave(productData);
    }
  };

  const handleChange = (field: keyof ProductFormData, value: string) => {
    setFormData({ ...formData, [field]: value });
    if (errors[field]) {
      setErrors({ ...errors, [field]: undefined });
    }
  };

  // RegExp patterns más estrictos
  const pricePattern = /^[0-9]*\.?[0-9]*$/;  // Solo números y un punto decimal
  const stockPattern = /^[0-9]*$/;           // Solo números enteros

  // Función para manejar input con RegExp - SOLO permite caracteres válidos
  const handleNumericInput = (value: string, pattern: RegExp, field: keyof ProductFormData) => {
    if (value === '' || pattern.test(value)) {
      handleChange(field, value);
    }
    // Si no pasa la validación, NO actualiza el estado (bloquea el input)
  };

  return (
    <Dialog 
      open={open} 
      onClose={onClose} 
      maxWidth="sm" 
      fullWidth
      PaperProps={{ sx: { borderRadius: 3, padding: 2 } }}
    >
      <DialogTitle sx={{ textAlign: 'center', fontSize: '1.5rem', fontWeight: 'bold' }}>
        {editingIndex !== null ? 'Editar Producto' : 'Nuevo Producto'}
      </DialogTitle>
      
      <DialogContent>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3, mt: 2 }}>
          <TextField
            label="Nombre del Producto"
            value={formData.nombre}
            onChange={(e) => handleChange('nombre', e.target.value)}
            error={!!errors.nombre}
            helperText={errors.nombre || `${formData.nombre.length}/30 caracteres`}
            fullWidth
            inputProps={{ maxLength: 30 }}
          />
          
          <TextField
            label="Precio"
            type="text"
            value={formData.precio}
            onChange={(e) => handleNumericInput(e.target.value, pricePattern, 'precio')}
            error={!!errors.precio}
            helperText={errors.precio}
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
            value={formData.stock}
            onChange={(e) => handleNumericInput(e.target.value, stockPattern, 'stock')}
            error={!!errors.stock}
            helperText={errors.stock}
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
        <Button onClick={onClose} variant="outlined" fullWidth>
          Cancelar
        </Button>
        <Button onClick={handleSubmit} variant="contained" fullWidth>
          {editingIndex !== null ? 'Actualizar' : 'Crear'}
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default ProductDialog;