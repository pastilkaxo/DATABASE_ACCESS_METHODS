using Microsoft.SqlServer.Server;
using System;
using System.Collections.Generic;
using System.Data.SqlTypes;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{
    [Serializable]
    [SqlUserDefinedType(Format.Native)]
    [StructLayout(LayoutKind.Sequential)]
    public struct RouteType : INullable
    {
        private int _value;
        private bool _isNull;

        public bool IsNull => _isNull;

        public static RouteType Null
        {
            get
            {
                RouteType h = new RouteType();
                h._isNull = true;
                return h;
            }
        }

        public override string ToString()
        {
            return _isNull ? "NULL" : _value.ToString();
        }

        public static RouteType Parse(SqlString s)
        {
            if (s.IsNull || !int.TryParse(s.Value, out int result))
            {
                throw new ArgumentException("Invalid routeId Must be an integer.");
            }

            RouteType routeId = new RouteType
            {
                _value = result,
                _isNull = false
            };
            return routeId;
        }

        public int GetValue() => _value;

    }
}
