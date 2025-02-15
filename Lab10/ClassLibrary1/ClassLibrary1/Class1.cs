using Microsoft.SqlServer.Server;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Mail;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{
    public class Class1
    {
        [SqlProcedure]
        public static void SendEmailOnDelete()
        {
            try
            {

                string semail = "vlad.lemeshok@gmail.com";
                string uemail = "ibuypowerclub@gmail.com";
                string upass = "abap wjhp scve smmi";
                MailAddress to = new MailAddress(semail);
                MailAddress from = new MailAddress(uemail);
                MailMessage message = new MailMessage(from, to)
                {
                    Subject = "LAB 10",
                    IsBodyHtml = false,
                    Body = $"Данные в таблице маршрутов успешно удалены!"
                };
                SmtpClient smtp = new SmtpClient("smtp.gmail.com", 587)
                {
                    Credentials = new NetworkCredential(uemail, upass),
                    EnableSsl = true
                };
                smtp.Send(message);
            }
            catch (Exception ex)
            {
                SqlContext.Pipe.Send("Ошибка отправки email: " + ex.Message);
            }
        }
    }
}
