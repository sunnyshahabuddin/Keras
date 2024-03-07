const https = require('https');
const fs = require('fs');

// Load the PEM certificate
const cert = fs.readFileSync('/path/to/certificate.pem');

// Options for the HTTPS request
const options = {
  hostname: 'nam-auth.client.narlcaycorp.com',
  port: 443,
  path: '/authn/authenticate',
  method: 'GET',
  cert: cert // Include the PEM certificate
};

// Make the HTTPS request
const req = https.request(options, (res) => {
  console.log('statusCode:', res.statusCode);
  console.log('headers:', res.headers);

  res.on('data', (d) => {
    process.stdout.write(d);
  });
});

// Handle any errors that occur during the request
req.on('error', (e) => {
  console.error(e);
});

// End the request
req.end();
