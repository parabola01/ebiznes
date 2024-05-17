const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const { createUser, findUserByUsername } = require('../models/user');
const router = express.Router();

router.post('/register', (req, res) => {
  const { username, password } = req.body;

  createUser(username, password, (err, result) => {
    if (err) {
      return res.status(400).send({ error: 'User registration failed' });
    }
    res.status(201).send({ message: 'User registered successfully' });
  });
});

router.post('/login', (req, res) => {
  const { username, password } = req.body;

  findUserByUsername(username, async (err, user) => {
    if (err || !user) {
      return res.status(400).send({ error: 'Invalid credentials' });
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(400).send({ error: 'Invalid credentials' });
    }

    const token = jwt.sign({ id: user.id }, 'your_jwt_secret', { expiresIn: '1h' });
    res.send({ token, user: { id: user.id, username: user.username } });
  });
});

module.exports = router;
