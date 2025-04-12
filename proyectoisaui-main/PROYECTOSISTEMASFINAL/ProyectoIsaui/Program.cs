using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ProyectoIsaui
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()//primer metodo que se ejecuta cuando inicia la app.
        {
            Application.EnableVisualStyles();//habilita los estilos visuales
            Application.SetCompatibleTextRenderingDefault(false);//representa texto en la app
            //   Application.Run(new Form1());
            //Application.Run(new FrmProducto());
            Application.Run(new FrmPrincipal());//se define el form de inicio y permite al usuario interactuar con la ventana principal.
        }
    }
}
