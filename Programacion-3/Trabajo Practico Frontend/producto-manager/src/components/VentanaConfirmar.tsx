import React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Typography,
} from '@mui/material';

interface PropsConfirmar {
  ventanaAbierta: boolean;
  nombreProducto: string;
  alCerrar: () => void;
  alConfirmar: () => void;
}

const VentanaConfirmar: React.FC<PropsConfirmar> = ({
  ventanaAbierta,
  nombreProducto,
  alCerrar,
  alConfirmar,
}) => (
  <Dialog 
    open={ventanaAbierta} 
    onClose={alCerrar} 
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
        ¿Eliminar "{nombreProducto}"?
      </Typography>
    </DialogContent>
    
    <DialogActions sx={{ padding: 2, gap: 1 }}>
      <Button 
        onClick={alCerrar} 
        variant="outlined" 
        fullWidth
        sx={{ borderRadius: 2 }}
      >
        Cancelar
      </Button>
      <Button 
        onClick={alConfirmar} 
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

export default VentanaConfirmar;