db = db.getSiblingDB('appdb');

db.createUser({
  user: 'appuser',
  pwd: 'apppassword',
  roles: [
    {
      role: 'readWrite',
      db: 'appdb'
    }
  ]
});

db.users.insertMany([
  {
    name: 'Jonathan Marin',
    email: 'jonathan@gmail.com',
    createdAt: new Date()
  }
]);
