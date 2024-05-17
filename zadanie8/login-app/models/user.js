const db = require('../config');
const bcrypt = require('bcryptjs');

const createUser = async (username, password, callback) => {
  const hashedPassword = await bcrypt.hash(password, 10);
  const sql = 'INSERT INTO users (username, password) VALUES (?, ?)';
  db.query(sql, [username, hashedPassword], (err, result) => {
    if (err) {
      return callback(err);
    }
    callback(null, result);
  });
};

const findUserByUsername = (username, callback) => {
  const sql = 'SELECT * FROM users WHERE username = ?';
  db.query(sql, [username], (err, result) => {
    if (err) {
      return callback(err);
    }
    callback(null, result[0]);
  });
};

module.exports = {
  createUser,
  findUserByUsername
};
