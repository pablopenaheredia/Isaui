import React from 'react';
import {Dialog, DialogTitle, DialogContent, DialogActions, Button, Typography} from '@mui/material';

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
  <Dialog open={ventanaAbierta} onClose={alCerrar}>
    <DialogTitle>Eliminar Producto</DialogTitle>
    <DialogContent>
      <Typography>¿Eliminar "{nombreProducto}"?</Typography>
    </DialogContent>
    <DialogActions>
      <Button onClick={alCerrar}>Cancelar</Button>
      <Button onClick={alConfirmar} color="error">Eliminar</Button>
    </DialogActions>
  </Dialog>
);

export default VentanaConfirmar;