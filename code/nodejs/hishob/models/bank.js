var db = require('../config/dbconnection');
var uuid = require('node-uuid');

var bank = {
    getBanks : function () {
        return new Promise((resolve, reject) => {
            db.query("SELECT * FROM bank", function(error, result) {
                if (error) {
                    return reject(error);
                } else {
                    return resolve(result);
                }
            });
        })
    },
    getBankById : function (bankId) {
        return new Promise((resolve, reject) => {
            db.query("SELECT * FROM bank WHERE bank_id = ?", [bankId], function(error, result) {
                if (error) {
                    return reject(error);
                } else {
                    return resolve(result);
                }
            });
        })
    },
    createBank : function (bank) {
        return new Promise((resolve, reject) => {
            db.query("INSERT INTO bank (uuid, bank_name) values (?, ?)", [uuid.v4(), bank.bankName], function(error, result) {
                if (error) {
                    return reject(error);
                } else {
                    return resolve(result.insertId);
                }
            });
        })
    }
};

module.exports = bank;