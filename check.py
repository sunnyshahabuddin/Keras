const request = require('request');
const kerberos = require('kerberos');

const url = 'http://localhost:5000/api/v1.0/kerberos';
const auth = new kerberos.HTTPKerberosAuth();

const options = {
  url: url,
  auth: auth,
  verify: 'C:\Users\user\Documen\ca-7.pem'
};

request.get(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(body);
  }
});
