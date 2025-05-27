const express = require('express');
const { SerialPort } = require('serialport');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.text({ type: '*/*' }));

const COM_PORT = 'COM5';
const BAUD_RATE = 9600;

app.post('/print', async (req, res) => {
  const content = req.body;

  try {
const port = new SerialPort({ path: COM_PORT, baudRate: BAUD_RATE });

  port.write(content, (err) => {
    if (err) {
      console.error('Error al imprimir:', err.message);
      return res.status(500).send('Error al enviar a la impresora');
    }

    console.log('Contenido enviado a la impresora');

    // Cerramos el puerto después de escribir
    port.close((err) => {
      if (err) {
        console.error('Error al cerrar el puerto:', err.message);
      } else {
        console.log('Puerto cerrado correctamente');
      }
    });

    return res.send('Impresión enviada correctamente');
  });
  } catch (error) {
    console.error('Excepción:', error.message);
    return res.status(500).send('Excepción: ' + error.message);
  }
});

app.listen(PORT, () => {
  console.log(`Servicio de impresión escuchando en http://localhost:${PORT}`);
});
