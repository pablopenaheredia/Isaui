using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;
using System.Data;
namespace ProyectoIsaui.Clases
{
    public static class Db
    {
        public static string GetCadena()
        {
            string Cadena = "datasource=localhost;port=3306;User Id=root;database=isaui;Password='';SSL Mode=None;";
            return Cadena;
        }

        public static void Guardar(string sql)
        {
            string Cadena = GetCadena();//cadena de conexion:info del servidor,nombre de bd y datos de acceso. 
            MySqlConnection con = new MySqlConnection(Cadena);//utiliza cadena como argumento para conexion a la bd.
            MySqlCommand cmd = new MySqlCommand();//ejecuta comandos sql en la bd.
            cmd.CommandText = sql;//consulta sql que se ejecutatara en la bd.
            cmd.Connection = con;//conexion que se establece con el objeto cmd.
            con.Open();//abre conexion a la bd en el objeto con.
            cmd.ExecuteNonQuery();//insertar,actualizar y eliminar
            con.Close();
        }

        public static DataTable Select(string sql)
        {
            string Cadena = GetCadena();
            MySqlConnection con = new MySqlConnection(Cadena);
            MySqlCommand comand = new MySqlCommand();
            comand.CommandText = sql;
            comand.Connection = con;
            MySqlDataAdapter da = new MySqlDataAdapter();//recupera datos de la bd
            da.SelectCommand = comand;//se declara el comando que se utiliza para recuperar los datos.
            DataSet ds = new DataSet();//almacena los datos de la consulta
            da.Fill(ds);//se usa el metodo fill del objeto da para ejecutar consulta y llenar el dataset.
            return ds.Tables[0];//devuelve la tabla con resultados de la busqueda.
        }
    }
}
