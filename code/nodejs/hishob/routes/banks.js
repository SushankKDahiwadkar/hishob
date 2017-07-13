var express = require('express');
var router = express.Router();
var bank = require('../models/bank');

/* GET users listing. */
router.get('/', function(req, res, next) {
    bank.getBanks()
        .then(data => {
            res.json(data);
        })
        .catch(err => {
            res.json(err);
        })
});

/* GET user by userId. */
router.get('/:bankId', function(req, res, next) {
    bank.getBankById(req.params.bankId)
        .then(data => {
            res.json(data);
        })
        .catch(err => {
            res.json(err);
        })
});

/* Create new User */
router.post('/', function(req, res, next){
    bank.createBank(req.body)
        .then(data => {
            res.json({ bank_id : data});
        })
        .catch(err => {
            res.json(err);
        })
});

module.exports = router;