const axios = require('axios');
const https = require('https');
const fs = require('fs');

const url = 'http://localhost:5000/api/v1.0/kerberos';
const agent = new https.Agent({
  ca: fs.readFileSync('C:\\Users\\user\\Documen\\ca-7.pem')
});

axios.get(url, { httpsAgent: agent })
  .then(response => {
    const token = response.data;
    console.log(token);
  })
  .catch(error => {
    console.error(error);
  });
