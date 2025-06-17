import { useState } from 'react';
import type { Product, ProductFormData, FormErrors } from '../types/Products';

const useProductForm = () => {
  const [open, setOpen] = useState(false);
  const [editingIndex, setEditingIndex] = useState<number | null>(null);
  const [formData, setFormData] = useState<ProductFormData>({
    nombre: "",
    precio: "",
    stock: "",
  });
  const [errors, setErrors] = useState<FormErrors>({});

  const openDialog = (product?: Product, index?: number) => {
    if (product && index !== undefined) {
      setEditingIndex(index);
      setFormData({
        nombre: product.nombre,
        precio: product.precio.toString(),
        stock: product.stock.toString(),
      });
    } else {
      setEditingIndex(null);
      setFormData({ nombre: "", precio: "", stock: "" });
    }
    setErrors({});
    setOpen(true);
  };

  const closeDialog = () => {
    setOpen(false);
    setEditingIndex(null);
    setFormData({ nombre: "", precio: "", stock: "" });
    setErrors({});
  };

  return {
    open,
    editingIndex,
    formData,
    errors,
    setFormData,
    setErrors,
    openDialog,
    closeDialog,
  };
};

export default useProductForm;