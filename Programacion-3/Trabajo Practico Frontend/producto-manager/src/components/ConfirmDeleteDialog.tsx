import React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Typography,
} from '@mui/material';

interface ConfirmDeleteDialogProps {
  open: boolean;
  productName: string;
  onClose: () => void;
  onConfirm: () => void;
}

const ConfirmDeleteDialog: React.FC<ConfirmDeleteDialogProps> = ({
  open,
  productName,
  onClose,
  onConfirm,
}) => (
  <Dialog 
    open={open} 
    onClose={onClose} 
    maxWidth="xs" 
    fullWidth
    PaperProps={{
      sx: {
        borderRadius: 2,
        padding: 1
      }
    }}
  >
    <DialogTitle sx={{ textAlign: 'center', pb: 1 }}>
      <Typography variant="h6" fontWeight="bold">
        Eliminar Producto
      </Typography>
    </DialogTitle>
    
    <DialogContent sx={{ textAlign: 'center', py: 2 }}>
      <Typography variant="body1">
        ¿Eliminar "{productName}"?
      </Typography>
    </DialogContent>
    
    <DialogActions sx={{ padding: 2, gap: 1 }}>
      <Button 
        onClick={onClose} 
        variant="outlined" 
        fullWidth
        sx={{ borderRadius: 2 }}
      >
        Cancelar
      </Button>
      <Button 
        onClick={onConfirm} 
        variant="contained" 
        color="error" 
        fullWidth
        sx={{ borderRadius: 2 }}
      >
        Eliminar
      </Button>
    </DialogActions>
  </Dialog>
);

export default ConfirmDeleteDialog;