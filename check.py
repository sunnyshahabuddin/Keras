const Service = require('node-windows').Service;

// Create a new service object
const svc = new Service({
  name: 'MyNodeService',
  description: 'My Node.js Service',
  script: 'C:\\Path\\To\\Your\\NodeApp\\server.js',
});

// Listen for the "install" event, which indicates that the service is being installed
svc.on('install', () => {
  svc.start();
});

// Install the service
svc.install();
