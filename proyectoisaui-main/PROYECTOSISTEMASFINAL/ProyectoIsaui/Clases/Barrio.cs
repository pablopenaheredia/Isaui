using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoIsaui.Clases
{
    public class Barrio
    {
        
        public DataTable getbarrios()
        {
            string sql = "select codbarrio,nombre from barrio order by nombre";
            return Db.Select(sql);
        }
    }
}
