const fetch = require('node-fetch');
const { KerberosClient } = require('kerberos-client');

const url = 'http://localhost:5000/';
const caPath = 'path/to/ca-bundle.crt';

(async () => {
    try {
        const kerberosClient = new KerberosClient();
        const token = await fetch(url, {
            agent: await kerberosClient.agent(),
            ca: caPath ? require('fs').readFileSync(caPath) : undefined
        }).then(response => response.json());

        console.log(token);
    } catch (error) {
        console.error('Error:', error);
    }
})();

