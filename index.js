// Node.js Express backend entry point
const express = require('express');
const app = express();
const PORT = 3001;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('PrediKing Backend Running!');
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
