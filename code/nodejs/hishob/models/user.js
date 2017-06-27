var db = require('../config/dbconnection');
var uuid = require('node-uuid');

var user = {
    getAllUsers : function (callback) {
        return db.query("SELECT * FROM user", callback);
    },
    getUserById : function (userId, callback) {
        console.log(userId);
        return db.query("SELECT * FROM user WHERE user_id = ?", [userId], callback);
    },
    createUser : function (user, callback) {
        return db.query("INSERT INTO user (uuid, first_name, last_name, middle_name, user_name, email, mobile_number, created, modified) values (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [uuid.v4(), user.firstName, user.lastName, user.middleName, user.userName, user.email, user.mobileNumber, Date.now(), Date.now()], 
            callback);
    },
    updateUser : function (userId, user, callback) {
        return db.query("UPDATE user SET first_name = ?, last_name = ?, middle_name = ?,  user_name = ?, email = ?, mobile_number = ?, modified = ? WHERE user_id = ?",
            [user.firstName, user.lastName, user.middleName, user.userName, user.email, user.mobileNumber, Date.now(), userId], 
            callback);
    }
};

module.exports = user;