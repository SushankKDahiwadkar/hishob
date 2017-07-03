/**
 * 
 */
package com.sushank.hishob.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.sushank.hishob.model.User;
import com.sushank.hishob.service.UserService;

/**
 * @author sdahiwadkar
 *
 */
@RestController
@RequestMapping("/user")
public class UserController {
	
	@Autowired
	UserService userService;
	
	@RequestMapping(method = RequestMethod.GET)
	public List<User> getUsers() {
		return userService.getAllUsers();
	}
	
	@RequestMapping(method = RequestMethod.POST)
	public void createUser(@RequestBody User user) {
		userService.createUser(user);
	}
	
}
