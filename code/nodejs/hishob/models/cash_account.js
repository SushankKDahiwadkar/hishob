var db = require('../config/dbconnection');
var uuid = require('node-uuid');

var cashAccount = {
    getCashAccounts : function () {
        return new Promise((resolve, reject) => {
            db.query("SELECT * FROM cash_account", function(error, result) {
                if (error) {
                    return reject(error);    
                } else {
                    return resolve(result);
                }
            });
        })
    },
    getCashAccountByCashAccountId : function (cashAccountId) {
        return new Promise((resolve, reject) => {
        var abc = db.query("SELECT * FROM cash_account WHERE cash_account_id = ?", [cashAccountId]);
        abc().then(function(data){
            resolve
        }, function(err){
            reject
        })
        })
    },
    createCashAccount : function (userUserId) {
        return new Promise((resolve, reject) => {
            db.query("INSERT INTO cash_account (uuid, user_id, created, modified) values (?, ?, ?, ?)",
            [uuid.v4(), userUserId.userId, Date.now(), Date.now()], 
            function (error, result) {
                if (error) {
                    reject(error);
                } else {
                    return resolve(result.insertId);
                }
            });
        })
    }
};

module.exports = cashAccount;