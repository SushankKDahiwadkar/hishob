var mysql=require('mysql');
var connection=mysql.createPool({
    host:'localhost',
    user:'root',
    password:'root',
    database:'hishob'
});

module.exports=connection;