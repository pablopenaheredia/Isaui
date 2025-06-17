import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import AdmProductos from './components/AdmProductos';

const theme = createTheme();

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AdmProductos />
    </ThemeProvider>
  );
}