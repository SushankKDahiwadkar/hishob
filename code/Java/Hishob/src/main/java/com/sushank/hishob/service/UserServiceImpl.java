/**
 * 
 */
package com.sushank.hishob.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.sushank.hishob.dao.UserDAO;
import com.sushank.hishob.model.User;

/**
 * @author sdahiwadkar
 *
 */
@Service
@Transactional
public class UserServiceImpl implements UserService{
	
	@Autowired
	UserDAO userDAO;
	
	public UserServiceImpl() {
		super();
		System.out.println("UserServiceImpl constructor");
	}

	public long createUser(User user) {
		return userDAO.createUser(user);
	}

	public User updateUser(User user) {
		return userDAO.updateUser(user);
	}

	public void deleteUser(long userId) {
		userDAO.deleteUser(userId);
	}

	public List<User> getAllUsers() {
		return userDAO.getAllUsers();
	}

	public User getUser(long userId) {
		return userDAO.getUser(userId);
	}

	public List<User> getAllUsers(String userName) {
		return userDAO.getAllUsers(userName);
	}

}
