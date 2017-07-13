var express = require('express');
var router = express.Router();
var cashAccount = require('../models/cash_account');

/* GET users listing. */
router.get('/', function(req, res, next) {
    cashAccount.getCashAccounts()
        .then(data => {
            res.json(data);
        })
        .catch(err => {
            res.json(err);
        })
});

/* GET user by userId. */
router.get('/:cashAccountId', function(req, res, next) {
    cashAccount.getCashAccountByCashAccountId(req.params.cashAccountId)
        .then(data => {
            res.json(data);
        })
        .catch(err => {
            res.json(err);
        })
});

/* Create new User */
router.post('/', function(req, res, next){
    cashAccount.createCashAccount(req.body)
        .then(data => {
            res.json({cashAccount : data});
        })
        .catch(err => {
            res.json(err);
        })
});

/*/* Edit User by userId
router.put('/:userId', function(req, res, next){
    user.updateUser(req.params.userId, req.body, function(error, result){
        if (error) {
            res.json(error);
        } else {
            res.json(req.body);
        }
    });
});*/

module.exports = router;