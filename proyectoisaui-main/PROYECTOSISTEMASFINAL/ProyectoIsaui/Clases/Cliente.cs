using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoIsaui.Clases
{
    public class Cliente
    {
     
        public void Insertar(string Nombre, string Apellido, string Telefono, string Documento, int codbarrio)
        {
            string sql = "insert into cliente (nombre, apellido,telefono,nrodoc,codbarrio)";
            sql = sql + "values (" + "'" + Nombre + "'";
            sql = sql + "," + "'" + Apellido + "'";
            sql = sql + "," + "'" + Telefono + "'";
            sql = sql + "," + "'" + Documento + "'";
            sql = sql + "," + "'" + codbarrio + "'";
            sql = sql + ")";
            Db.Guardar(sql);
        }
    }
}
