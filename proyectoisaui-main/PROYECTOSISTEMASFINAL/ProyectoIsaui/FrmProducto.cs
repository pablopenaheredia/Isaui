using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ProyectoIsaui.Clases;

namespace ProyectoIsaui
{
    public partial class FrmProducto : FrmBase
    {
        public FrmProducto()
        {
            InitializeComponent();
        }

        private void FrmProducto_Load(object sender, EventArgs e)
        {
            txtCodProducto.Text = FrmPrincipal.CodProducto;
            if (txtCodProducto.Text != "")
            {
                Int32 codproducto = Convert.ToInt32(txtCodProducto.Text);
                Producto pro = new Producto();
                DataTable dt = pro.BuscarPorID(codproducto);
                txtNombre.Text = dt.Rows[0]["Nombre"].ToString();
                txtprecio.Text = dt.Rows[0]["Precio"].ToString();
            }
        }

        private void btnguardar_Click(object sender, EventArgs e)
        {
            if(txtNombre.Text == "")
            {
                MessageBox.Show("Ingresar un nombre");
                return;
            }
            if (txtprecio.Text == "")
            {
                MessageBox.Show("Debe ingresar un precio");
                return;
            }
            if (txtmarca.Text == "")
            {
                MessageBox.Show("Debe ingresar una Marca");
                return;
            }
            string nombre = "";
            double precio = 0;
            string codbarra = "";
            int codproducto = 0;
            int stock = 0;
            string marca = "";
            nombre = txtNombre.Text;
            precio = Convert.ToDouble(txtprecio.Text);
            codbarra = txtcodbarra.Text;
            marca = txtmarca.Text;
            if (txtstock.Text != "")
            {
                stock = Convert.ToInt32(txtstock.Text);
            }
            string mensaje = "";
            //mensaje = "Producto: " + nombre + " Precio: " + precio.ToString();
            //MessageBox.Show(mensaje);
            Producto Pro = new Producto();
            if (txtCodProducto.Text == "")
            {
                Pro.Insertar(nombre, marca, precio, codbarra, stock);
            }
            else
            {
                codproducto = Convert.ToInt32(txtCodProducto.Text);
                Pro.Modificar(codproducto, marca, nombre, precio, stock);
            }
            MessageBox.Show("Datos grabados correctamente");
        }

        private void btncancelar_Click(object sender, EventArgs e)
        {
            txtNombre.Text = "";
            txtprecio.Text = "";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void GbProducto_Enter(object sender, EventArgs e)
        {

        }

        private void txtCodProducto_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtmarca_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
