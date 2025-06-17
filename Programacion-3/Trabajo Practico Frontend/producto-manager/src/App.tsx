import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import AdministradorProductos from './components/AdministradorProductos';

const theme = createTheme();

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AdministradorProductos />
    </ThemeProvider>
  );
}