app.get('/dashboard', (req, res) => {
  const response = {};

  // Execute the first query: SELECT AVG(sm_component_value) FROM table1
  connection.query('SELECT AVG(sm_component_value) AS average_value FROM table1', (err, results) => {
    if (err) {
      console.error('Error executing the first query:', err);
      res.status(500).json({ error: 'Internal Server Error' });
      return;
    }

    // Add the result of the first query to the response
    response.value1 = results[0].average_value;

    // Execute the second query: SELECT sm_component FROM table1
    connection.query('SELECT sm_component FROM table1', (err, secondResults) => {
      if (err) {
        console.error('Error executing the second query:', err);
        res.status(500).json({ error: 'Internal Server Error' });
        return;
      }

      // Add the result of the second query to the response
      response.value2 = secondResults.map(result => result.sm_component);

      // Execute the third query, and so on...
      connection.query('SELECT ...', (err, thirdResults) => {
        if (err) {
          console.error('Error executing the third query:', err);
          res.status(500).json({ error: 'Internal Server Error' });
          return;
        }

        // Add the result of the third query to the response
        response.value3 = thirdResults;

        // Execute the fourth query, and so on...
        connection.query('SELECT ...', (err, fourthResults) => {
          if (err) {
            console.error('Error executing the fourth query:', err);
            res.status(500).json({ error: 'Internal Server Error' });
            return;
          }

          // Add the result of the fourth query to the response
          response.value4 = fourthResults;

          // Execute the fifth query, and so on...
          connection.query('SELECT ...', (err, fifthResults) => {
            if (err) {
              console.error('Error executing the fifth query:', err);
              res.status(500).json({ error: 'Internal Server Error' });
              return;
            }

            // Add the result of the fifth query to the response
            response.value5 = fifthResults;

            // At this point, all queries have completed, and you can send the final JSON response
            res.json(response);
          });
        });
      });
    });
  });
});
