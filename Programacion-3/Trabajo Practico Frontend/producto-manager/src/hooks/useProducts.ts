import { useState, useEffect } from 'react';
import type { Product } from '../types/Products';

const initialProducts: Product[] = [
  { nombre: "Laptop HP", precio: 899.99, stock: 15 },
  { nombre: "Mouse Inalámbrico", precio: 25.5, stock: 50 },
  { nombre: "Teclado Mecánico", precio: 120.0, stock: 0 },
];

const STORAGE_KEY = 'products-manager';

const useProducts = () => {
  const [products, setProducts] = useState<Product[]>(() => {
    try {
      const savedProducts = localStorage.getItem(STORAGE_KEY);
      if (savedProducts) {
        return JSON.parse(savedProducts);
      }
    } catch (error) {
      console.error(error);
    }
    return initialProducts;
  });

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(products));
    } catch (error) {
      console.error(error);
    }
  }, [products]);

  const addProduct = (productData: Product) => {
    setProducts(prev => [...prev, productData]);
  };

  const updateProduct = (index: number, productData: Product) => {
    setProducts(prev => {
      const updatedProducts = [];
      for (let i = 0; i < prev.length; i++) {
        if (i === index) {
          updatedProducts.push(productData);
        } else {
          updatedProducts.push(prev[i]);
        }
      }
      return updatedProducts;
    });
  };

  const deleteProduct = (index: number) => {
    setProducts(prev => {
      const filteredProducts = [];
      for (let i = 0; i < prev.length; i++) {
        if (i !== index) {
          filteredProducts.push(prev[i]);
        }
      }
      return filteredProducts;
    });
  };

  return {
    products,
    addProduct,
    updateProduct,
    deleteProduct,
  };
};

export default useProducts;