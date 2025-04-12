using ProyectoIsaui.Clases;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace ProyectoIsaui
{
    public partial class FrmCliente : FrmBase
    {

        public FrmCliente()
        {
            InitializeComponent();
        }
        

        private void FrmCliente_Load(object sender, EventArgs e)
        {
            string sql = "select * from cliente";
            DataTable tbcliente = Db.Select(sql);
            cargarBarrios();
        }
        
        private void cargarBarrios()
        {
            Barrio b = new Barrio();
            DataTable tb = b.getbarrios();
            cmbBarrio.DataSource = tb;
            cmbBarrio.DisplayMember = "nombre";
            cmbBarrio.ValueMember = "codBarrio";
            cmbBarrio.SelectedIndex = -1;
        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {
            if (txtNombre.Text == "")
            {
                MessageBox.Show("Ingresar un nombre");
                return;
            }
            if (txtApellido.Text == "")
            {
                MessageBox.Show("Ingresar apellido");
                return;
            }
            if (txtTelefono.Text == "")
            {
                MessageBox.Show("Ingresar telefono");
                return;
            }
            if (txtDocumento.Text == "")
            {
                MessageBox.Show("Ingresar Documento");
                return;
            }
            string nombre = "";
            string apellido = "";
            string telefono = "";
            string documento = "";
            nombre = txtNombre.Text;
            apellido = txtApellido.Text;
            telefono = txtTelefono.Text;
            documento = txtDocumento.Text;
            int codbarrio = Convert.ToInt32(cmbBarrio.SelectedValue);
            string mensaje = "";
            //mensaje = "Producto: " + nombre + " Precio: " + precio.ToString();
            //MessageBox.Show(mensaje);
            Cliente cli = new Cliente();
            cli.Insertar(nombre, apellido, telefono, documento,codbarrio);
            MessageBox.Show("Datos grabados correctamente");
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            txtNombre.Text = "";
            txtApellido.Text = "";
            txtDocumento.Text = "";
            txtTelefono.Text = "";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnGuardar_Click_1(object sender, EventArgs e)
        {
            if (txtNombre.Text == "")
            {
                MessageBox.Show("Ingresar un nombre");
                return;
            }
            if (txtApellido.Text == "")
            {
                MessageBox.Show("Ingresar apellido");
                return;
            }
            if (txtTelefono.Text == "")
            {
                MessageBox.Show("Ingresar telefono");
                return;
            }
            if (txtDocumento.Text == "")
            {
                MessageBox.Show("Ingresar Documento");
                return;
            }
            
            string nombre = txtNombre.Text;
            string apellido = txtApellido.Text;
            string telefono = txtTelefono.Text;
            string documento = txtDocumento.Text;
            int codbarrio = Convert.ToInt32(cmbBarrio.SelectedValue);
            Cliente cli = new Cliente();
            cli.Insertar(nombre, apellido, telefono, documento,codbarrio);
            MessageBox.Show("Datos guardados correctamente");
        }

        private void btnCancelar_Click_1(object sender, EventArgs e)
        {
            txtNombre.Text = "";
            txtApellido.Text = "";
            txtDocumento.Text = "";
            txtTelefono.Text = "";
        }

        private void lblApellido_Click(object sender, EventArgs e)
        {

        }
    }
}
