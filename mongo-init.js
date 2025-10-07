// mongo-init.js
db = db.getSiblingDB("news");

// Create a user for this database
db.createUser({
  user: "mongo_username",
  pwd: "mongo_password",
  roles: [
    {
      role: "readWrite",
      db: "news",
    },
  ],
});

// Optionally create collections
db.createCollection("economic");
db.createCollection("sports");
