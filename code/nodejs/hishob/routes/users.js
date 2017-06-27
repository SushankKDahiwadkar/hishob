var express = require('express');
var router = express.Router();
var user = require('../models/user');

/* GET users listing. */
router.get('/', function(req, res, next) {
    user.getAllUsers(function(error, result) {
        if (error) {
            res.json(error);
        } else {
            res.json(result);
        }
    });
});

/* GET user by userId. */
router.get('/:userId', function(req, res, next) {
    user.getUserById(req.params.userId, function(error, result) {
        if (error) {
            res.json(error);
        } else {
            res.json(result);
        }
    });
});

/* Create new User */
router.post('/', function(req, res, next){
    user.createUser(req.body, function (error, result){
        if (error) {
            res.json(error);
        } else {
            res.json(req.body);
        }
    });
});

/* Edit User by userId */
router.put('/:userId', function(req, res, next){
    user.updateUser(req.params.userId, req.body, function(error, result){
        if (error) {
            res.json(error);
        } else {
            res.json(req.body);
        }
    });
});

module.exports = router;