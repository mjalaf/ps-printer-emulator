using Microsoft.AspNetCore.Mvc;
using System.IO.Ports;

[ApiController]
[Route("api/print")]
public class PrintController : ControllerBase
{
    [HttpPost]
    public IActionResult Post([FromBody] string content)
    {
        try
        {
            using var port = new SerialPort("COM3", 9600);
            port.Open();
            port.WriteLine(content);
            port.Close();
            return Ok("Impresión enviada correctamente");
        }
        catch (Exception ex)
        {
            return StatusCode(500, $"Error: {ex.Message}");
        }
    }
}